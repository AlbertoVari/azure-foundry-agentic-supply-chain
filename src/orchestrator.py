from __future__ import annotations
import json
from dataclasses import dataclass
from typing import Any, Dict, List, Union, Callable

HaltableOutput = Union[Dict[str, Any], str]

@dataclass
class StepResult:
    agent: str
    output: HaltableOutput

def should_halt(output: HaltableOutput) -> str | None:
    """Implements the project halt rules."""
    if isinstance(output, str):
        txt = output.strip()
        if txt == "Sales Kit not found":
            return "Sales Kit not found"
        if "Error" in txt:
            return txt
        return None

    # dict output
    if any(k.lower() == "error" for k in output.keys()):
        return "Error"
    dumped = json.dumps(output)
    if "Material not found" in dumped:
        return "Material not found"
    return None

def orchestrate(
    *,
    bom_fn: Callable[[str], HaltableOutput],
    inventory_fn: Callable[[HaltableOutput], HaltableOutput],
    supplier_fn: Callable[[HaltableOutput], HaltableOutput],
    po_fn: Callable[[HaltableOutput], HaltableOutput],
    user_request: str,
) -> Dict[str, Any]:
    steps: List[StepResult] = []

    bom_out = bom_fn(user_request)
    steps.append(StepResult("BOM_Generation_Agent", bom_out))
    reason = should_halt(bom_out)
    if reason:
        return {"workflow_status": "HALTED", "reason": reason, "steps": [s.__dict__ for s in steps]}

    inv_out = inventory_fn(bom_out)
    steps.append(StepResult("Inventory_Evaluation_Agent", inv_out))
    reason = should_halt(inv_out)
    if reason:
        return {"workflow_status": "HALTED", "reason": reason, "steps": [s.__dict__ for s in steps]}

    sup_out = supplier_fn(inv_out)
    steps.append(StepResult("Supplier_Analysis_Agent", sup_out))
    reason = should_halt(sup_out)
    if reason:
        return {"workflow_status": "HALTED", "reason": reason, "steps": [s.__dict__ for s in steps]}

    po_out = po_fn(sup_out)
    steps.append(StepResult("Purchase_Order_Agent", po_out))
    reason = should_halt(po_out)
    if reason:
        return {"workflow_status": "HALTED", "reason": reason, "steps": [s.__dict__ for s in steps]}

    return {"workflow_status": "SUCCESS", "reason": "OK", "steps": [s.__dict__ for s in steps]}
