from __future__ import annotations
import os
import json
from src.utils import load_env
from src.foundry_rest import FoundryRESTClient, FoundryRESTConfig
from src.orchestrator import orchestrate

TEST_PROMPTS = [
    ("BOM", "What are the materials required to produce two combustion section repair kits?"),
    ("Inventory", "Check inventory for: Ti-6Al-4V titanium alloy (40 units)."),
    ("Supplier", "Find suppliers for: Inconel 718 and Inconel X-750."),
    ("PO", "Generate a purchase order for Haynes International for 50 units of Inconel 718."),
    ("E2E", "To produce a compressor section repair kit, will a Haynes International order form be required?"),
]

def main() -> None:
    load_env()
    endpoint = os.environ.get("FOUNDRY_ENDPOINT")
    api_key = os.environ.get("FOUNDRY_API_KEY")
    if not endpoint:
        raise SystemExit("Set FOUNDRY_ENDPOINT in .env (see .env.example).")

    agent_bom = os.environ.get("AGENT_ID_BOM")
    agent_inv = os.environ.get("AGENT_ID_INVENTORY")
    agent_sup = os.environ.get("AGENT_ID_SUPPLIER")
    agent_po = os.environ.get("AGENT_ID_PO")

    client = FoundryRESTClient(FoundryRESTConfig(base_url=endpoint, api_key=api_key))

    def run(agent_id: str, text: str):
        resp = client.run_agent(agent_id=agent_id, user_input=text)
        # Adapt parsing to your tenant response shape:
        return resp.get("output", resp)

    print("=== Running partial tests (if agent IDs are set) ===")
    if agent_bom:
        print("\n[BOM]\n", run(agent_bom, TEST_PROMPTS[0][1]))
    if agent_inv:
        print("\n[Inventory]\n", run(agent_inv, TEST_PROMPTS[1][1]))
    if agent_sup:
        print("\n[Supplier]\n", run(agent_sup, TEST_PROMPTS[2][1]))
    if agent_po:
        print("\n[PO]\n", run(agent_po, TEST_PROMPTS[3][1]))

    print("\n=== Running E2E (code orchestrator) ===")
    if not (agent_bom and agent_inv and agent_sup and agent_po):
        print("Set AGENT_ID_BOM, AGENT_ID_INVENTORY, AGENT_ID_SUPPLIER, AGENT_ID_PO in .env to run E2E.")
        return

    result = orchestrate(
        bom_fn=lambda user_req: run(agent_bom, user_req),
        inventory_fn=lambda bom_json: run(agent_inv, json.dumps(bom_json)),
        supplier_fn=lambda inv_json: run(agent_sup, json.dumps(inv_json)),
        po_fn=lambda sup_json: run(agent_po, json.dumps(sup_json)),
        user_request=TEST_PROMPTS[4][1],
    )

    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
