from __future__ import annotations
import os
from src.utils import load_env, read_prompt
from src.foundry_rest import FoundryRESTClient, FoundryRESTConfig

def main() -> None:
    load_env()

    endpoint = os.environ.get("FOUNDRY_ENDPOINT")
    if not endpoint:
        raise SystemExit("Set FOUNDRY_ENDPOINT in .env (see .env.example).")

    # Optional: if your tenant uses API keys for the Foundry endpoint
    api_key = os.environ.get("FOUNDRY_API_KEY")

    dep_gpt41 = os.environ.get("DEPLOYMENT_GPT41")
    dep_gpt41_mini = os.environ.get("DEPLOYMENT_GPT41_MINI")
    if not dep_gpt41 or not dep_gpt41_mini:
        raise SystemExit("Set DEPLOYMENT_GPT41 and DEPLOYMENT_GPT41_MINI in .env.")

    client = FoundryRESTClient(FoundryRESTConfig(base_url=endpoint, api_key=api_key))

    # Tools below are placeholders; adapt to your Foundry tool schema.
    search_tool = {
        "type": "azure_ai_search",
        "endpoint": os.environ.get("AZURE_SEARCH_ENDPOINT"),
        "index": os.environ.get("AZURE_SEARCH_INDEX", "rawmaterials"),
        "api_key": os.environ.get("AZURE_SEARCH_API_KEY"),
    }
    code_interpreter_tool = {"type": "code_interpreter"}

    print("Creating agents (you may need to adapt endpoints/tools for your tenant)...")

    orchestrator = client.create_agent(
        name="Orchestrator",
        model_deployment=dep_gpt41,
        temperature=1.0,
        system_instructions=read_prompt("orchestrator_system.txt"),
    )

    bom = client.create_agent(
        name="BOM_Generation_Agent",
        model_deployment=dep_gpt41_mini,
        temperature=0.0,
        system_instructions=read_prompt("bom_system.txt"),
        knowledge_files=[
            "data/sales_kits/CombustionSystemRepairKit.pdf",
            "data/sales_kits/CompressorSectionSystemRepairKit.pdf",
            "data/sales_kits/TurbineSectionSystemRepairKit.pdf",
        ],
    )

    inventory = client.create_agent(
        name="Inventory_Evaluation_Agent",
        model_deployment=dep_gpt41_mini,
        temperature=0.0,
        system_instructions=read_prompt("inventory_system.txt"),
        tools=[search_tool],
    )

    supplier = client.create_agent(
        name="Supplier_Analysis_Agent",
        model_deployment=dep_gpt41,
        temperature=0.7,
        system_instructions=read_prompt("supplier_system.txt"),
        knowledge_files=["data/suppliers/Suppliers.pdf"],
    )

    po = client.create_agent(
        name="Purchase_Order_Agent",
        model_deployment=dep_gpt41_mini,
        temperature=0.0,
        system_instructions=read_prompt("purchase_order_system.txt"),
        tools=[code_interpreter_tool],
        knowledge_files=["data/date.py"],
    )

    print("\nCreated agent IDs (save these into .env):")
    print("AGENT_ID_ORCHESTRATOR=", orchestrator.get("id"))
    print("AGENT_ID_BOM=", bom.get("id"))
    print("AGENT_ID_INVENTORY=", inventory.get("id"))
    print("AGENT_ID_SUPPLIER=", supplier.get("id"))
    print("AGENT_ID_PO=", po.get("id"))

if __name__ == "__main__":
    main()
