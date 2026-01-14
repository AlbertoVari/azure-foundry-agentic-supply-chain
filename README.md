## 📦 Agentic Supply Chain Workflow using Microsoft Azure AI Foundry

### Project Description

This project implements an **end-to-end automated supply chain workflow** using **Agent Services in Microsoft Azure AI Foundry**.
The solution demonstrates how a **multi-agent, agentic architecture** can be designed and orchestrated entirely through **configuration and prompt engineering**, without relying on complex application code.

The goal of the system is to automate a real-world procurement workflow by enabling AI agents to **collaborate, reason, and act sequentially** to move from product demand to purchase order generation.

---

### 🧠 Architecture Overview

The solution follows a **two-layer agentic architecture** composed of one orchestrator agent and four specialized worker agents:

1. **Orchestrator Agent (GPT-4.1)**

   * Acts as the workflow manager
   * Routes tasks to agents in a fixed sequence
   * Captures structured JSON outputs from each agent
   * Halts execution if any agent returns an error or missing data signal

2. **BOM Generation Agent (GPT-4.1 Mini)**

   * Extracts a **Bill of Materials (BOM)** from unstructured Sales Kit documents
   * Outputs a deterministic JSON schema
   * Handles missing product definitions gracefully

3. **Inventory Evaluation Agent (GPT-4.1 Mini)**

   * Queries an **Azure AI Search index** connected to an Azure Storage Table
   * Compares BOM requirements against available stock
   * Identifies material shortages

4. **Supplier Analysis Agent (GPT-4.1)**

   * Uses a curated supplier knowledge base
   * Matches missing materials with approved suppliers
   * Performs analytical reasoning to map materials to vendors

5. **Purchase Order Agent (GPT-4.1 Mini)**

   * Generates professional purchase orders
   * Uses a Python Code Interpreter tool to insert the current date
   * Produces formatted, human-readable PO documents

---

### 🔄 Automated Workflow

The agentic workflow executes the following steps:

1. User submits a request to build a product
2. BOM is extracted from sales documentation
3. Inventory availability is checked
4. Missing materials are identified
5. Approved suppliers are selected
6. Purchase orders are generated when required

This mirrors real-world procurement and inventory management processes, improving **resilience, efficiency, and decision-making**.

---

### ☁️ Cloud-Native Implementation

* Built entirely in **Azure AI Foundry**
* Uses **Azure Storage Tables** and **Azure AI Search**
* Leverages **knowledge grounding**, **tools**, and **agent orchestration**
* Designed to run fully in the cloud with no local setup required

---

### ✅ Validation & Testing

The project includes:

* Partial agent tests (unit-style validation)
* Full end-to-end workflow execution
* Evidence captured via chat logs and screenshots
* Structured validation report aligned with the project rubric

---

### 🎯 Key Skills Demonstrated

* Agentic AI system design
* Multi-agent orchestration
* Prompt engineering & routing logic
* Knowledge-augmented AI agents
* Azure AI Foundry, Search, and Storage integration
* Iterative validation and error-handling workflows

## STACK

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
