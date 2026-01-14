# Azure AI Foundry – Agentic Supply Chain (Udacity Project)

This repo contains a **reference implementation** (code-first) of the Udacity “Agentic Supply Chain” project.
It mirrors the required two-layer, five-agent architecture described in the project instructions. fileciteturn0file0

## Architecture

- **Orchestrator Agent (GPT-4.1, temp=1)**: routes and halts on failures.
- **BOM Generation Agent (GPT-4.1 Mini, temp=0)**: extracts BOM from Sales Kit PDFs.
- **Inventory Evaluation Agent (GPT-4.1 Mini, temp=0)**: checks stock via Azure AI Search (`rawmaterials` index).
- **Supplier Analysis Agent (GPT-4.1, temp>=0.7)**: finds suppliers from Suppliers PDF.
- **Purchase Order Agent (GPT-4.1 Mini, temp=0)**: formats PO and uses `date.py` via Code Interpreter.

> Note: In the Udacity lab you can implement the whole workflow in the Foundry UI via configuration.
> This repo is useful if you want to reproduce the same behavior programmatically.

## Repo layout

- `prompts/` – System prompts for each agent (ready to paste into Foundry).
- `data/` – Provided PDFs + `date.py` + inventory seed CSV.
- `src/` – Python scripts to create agents and run the 5 required test prompts.
- `submission_template.md` – Udacity submission template (copied from the assets zip).

## Prereqs

- Python 3.10+
- Install deps:
  ```bash
  pip install -r requirements.txt
  ```

## Configure

Copy `.env.example` to `.env` and fill values.

## Run

Create agents (optional, if you want code-first provisioning):
```bash
python -m src.create_agents
```

Run tests:
```bash
python -m src.run_tests
```

## Notes about Azure AI Foundry APIs

Azure AI Foundry/Agent Services APIs may differ by region/tenant and can evolve.
This repo includes:
- an SDK-based path (if available in your environment), and
- a REST fallback skeleton (so you can adapt quickly).

If the SDK import fails, use the REST path and fill the endpoints shown in `src/foundry_rest.py`.
