# **Project Submission Template**

Student Name: \[Your Name Here\]  
Date: \[Date\]

## **Part 1: Azure Resource Deployment**

*Instructions: Verify creation and configuration of all required Azure resources, including a successful indexer run and wildcard search.*

### **1.1 AI Foundry & Project**

\[Paste Screenshot of AI Foundry Project Home Screen\]  
Must show project name finalProjectC1.

### **1.2 Model Deployments**

\[Paste Screenshot of "Deployments" page\]  
Must show gpt-4 (or 4.1) and gpt-4o-mini (or 4.1 mini) deployments.

### **1.3 Storage & Search**

\[Paste Screenshot of Storage Table "RawMaterialInventory"\]  
Must show the columns/properties matching the project instructions.  
\[Paste Screenshot of Azure AI Search "Indexer" Status\]  
Must show the indexer run was "Success".  
\[Paste Screenshot of Azure AI Search "Search Explorer"\]  
Must show a search for \* (wildcard) returning results (JSON).

## **Part 2: Orchestrator Agent**

*Instructions: Verify configuration, temperature=1, connection to workers, and correct "Halt" behavior.*

### **2.1 Configuration**

\[Paste Screenshot of Orchestrator Agent "Code/Configuration" view\]  
Must show:

* *Name: Orchestrator*  
* *Model: GPT-4/4.1*  
* *Temperature: 1*  
* *Connections to all 4 worker agents*  
* *System Instructions visible*

### **2.2 Execution Trace (Successful Run)**

\[Paste Screenshot of a successful run trace\]  
Must show the correct order: BOM \-\> Inventory \-\> Supplier \-\> Orders.

### **2.3 Execution Trace (Halted Run)**

\[Paste Screenshot of a "Halted" run\]  
Must show the workflow stopping early (e.g., when a Sales Kit is not found).

## **Part 3: Worker Agents**

*Instructions: Verify configuration, models, temperature settings, and knowledge connections.*

### **3.1 BOM Agent**

\[Paste Screenshot of BOM Agent Configuration\]  
Must show Model (Mini), Knowledge Base (sales\_kits.pdf), and Temperature (Low).

### **3.2 Inventory Check Agent**

\[Paste Screenshot of Inventory Agent Configuration\]  
Must show Connection to Azure AI Search Index.

### **3.3 Supplier Analysis Agent**

\[Paste Screenshot of Supplier Analysis Agent Configuration\]  
Must show Model (Standard/GPT-4), Knowledge Base (suppliers.pdf), and Temperature (Higher/Analysis).

### **3.4 Supplier Orders Agent**

\[Paste Screenshot of Supplier Orders Agent Configuration\]  
Must show Code Interpreter enabled (with date.py) and specific instructions.

## **Part 4: Workflow Testing (The 5 Prompts)**

*Instructions: Demonstrate end-to-end and partial workflow execution using 5 distinct prompts. Paste the final output or a screenshot of the chat log.*

### **Prompt 1: BOM Generation (Partial Workflow)**

User Prompt: "What are the materials required to produce two combustion section repair kits?"  
Output:  
\[Paste the JSON Output here\]

### **Prompt 2: Inventory Check (Unit/Partial Context)**

User Prompt: "Check inventory for: Ti-6Al-4V titanium alloy (40 units)."  
Output:  
\[Paste the Agent Response here\]

### **Prompt 3: Supplier Analysis (Unit/Partial Context)**

User Prompt: "Find suppliers for: Inconel 718 and Inconel X-750."  
Output:  
\[Paste the Agent Response here\]

### **Prompt 4: Purchase Order Generation (Unit/Partial Context)**

User Prompt: "Generate a purchase order for Haynes International for 50 units of Inconel 718."  
Output:  
\[Paste the formatted Order Form here\]

### **Prompt 5: End-to-End Workflow (Full Run)**

User Prompt: "To produce a compressor section repair kit, will a Haynes International order form be required?"  
Evidence:  
\[Paste Screenshot of the Chat Log showing the full sequence of agents\]