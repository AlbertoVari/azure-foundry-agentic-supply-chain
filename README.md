# Agentic Supply Chain Workflow

**Microsoft Azure AI Foundry – Multi-Agent System**

## Overview

This repository contains an **end-to-end agentic supply chain workflow** built using **Microsoft Azure AI Foundry**.
The project demonstrates how to design and orchestrate a **multi-agent system** using **prompt engineering and cloud configuration only**, without writing complex application logic.

The workflow automates a real-world **procurement and inventory management process**, moving from product demand to supplier purchase orders through coordinated AI agents.

---

## Architecture

The solution implements a **two-layer agentic architecture**:

### 1. Orchestration Layer

* **Orchestrator Agent (GPT-4.1)**

  * Acts as the workflow manager
  * Routes tasks to worker agents in a fixed execution order
  * Collects and validates structured JSON outputs
  * Halts execution if any agent returns an error or missing-data signal

### 2. Worker Agent Layer

Four specialized agents perform discrete supply-chain tasks:

| Agent                          | Model        | Responsibility                                                         |
| ------------------------------ | ------------ | ---------------------------------------------------------------------- |
| **BOM Generation Agent**       | GPT-4.1 Mini | Extracts Bill of Materials (BOM) from unstructured Sales Kit documents |
| **Inventory Evaluation Agent** | GPT-4.1 Mini | Queries Azure AI Search to validate inventory availability             |
| **Supplier Analysis Agent**    | GPT-4.1      | Matches missing materials with approved suppliers                      |
| **Purchase Order Agent**       | GPT-4.1 Mini | Generates formatted purchase orders using a Python Code Interpreter    |

---

## Automated Workflow

The system executes the following deterministic pipeline:

1. User submits a product build request
2. BOM is extracted from Sales Kit documentation
3. Inventory is checked against warehouse stock
4. Material shortages are identified
5. Approved suppliers are selected
6. Purchase orders are generated if required

If any step fails (e.g., missing Sales Kit or material not found), the orchestrator **halts the workflow** to prevent error propagation.

---

## Cloud Resources Used

* **Azure AI Foundry**

  * Agent Services
  * Model deployments (GPT-4.1 & GPT-4.1 Mini)
* **Azure Storage Table**

  * Raw material inventory data
* **Azure AI Search**

  * Inventory index and indexer
* **Knowledge Files**

  * Sales Kits (PDF)
  * Supplier List (PDF)
* **Code Interpreter Tool**

  * Python script for dynamic date insertion in purchase orders

---

## Configuration Highlights

* **Deterministic agents** (BOM, Inventory, Orders) use **Temperature = 0**
* **Analytical agents** (Supplier Analysis) use **higher temperature**
* **Orchestrator** uses **high temperature** for flexible routing logic
* All agent communication uses **strict JSON schemas**
* Validation and halt logic is enforced at each stage

---

## Testing Strategy

The project includes **five required test scenarios**:

### Partial (Unit-Style) Tests

1. BOM extraction validation
2. Inventory lookup via Azure AI Search
3. Supplier knowledge retrieval
4. Purchase order generation with Code Interpreter

### End-to-End Test

5. Full workflow execution from user request → purchase order

All tests produce:

* Structured intermediate JSON outputs
* Human-readable summaries
* Traceable agent execution order

---

## Key Concepts Demonstrated

* Agentic AI system design
* Multi-agent orchestration patterns
* Prompt chaining and routing
* Knowledge-augmented agents
* Cloud-native AI workflows
* Validation gates and halt conditions

---

## Project Goal

The primary objective of this project is to demonstrate how **agentic AI workflows** can improve supply chain resilience, reduce manual coordination, and enable adaptive decision-making using modern cloud-based AI services.

---

## Notes

* The system is designed to run **entirely within Azure AI Foundry**
* No local environment setup is required
* All configuration is done via Foundry UI and prompt engineering
* Screenshots and chat logs are used for validation and assessment



