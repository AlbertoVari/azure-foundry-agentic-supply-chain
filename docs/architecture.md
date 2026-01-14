```mermaid
flowchart LR
  U[User] --> O[Orchestrator (GPT-4.1)]
  O --> B[BOM Agent (GPT-4.1 Mini)]
  B --> I[Inventory Agent (GPT-4.1 Mini + AI Search)]
  I --> S[Supplier Agent (GPT-4.1)]
  S --> P[PO Agent (GPT-4.1 Mini + Code Interpreter)]
  P --> O
  O --> R[Final Response]
```
