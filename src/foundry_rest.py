from __future__ import annotations
import json
import requests
from dataclasses import dataclass
from typing import Any, Dict, Optional

@dataclass
class FoundryRESTConfig:
    """
    REST configuration.

    NOTE:
    Azure AI Foundry / Agent Service endpoints vary by tenant/region and can evolve.
    In Foundry UI, look for an endpoint like:
      https://<your-project>.<region>.api.ai.azure.com

    If your environment uses a different base URL or requires a specific API version,
    update `base_url` and `api_version`.
    """
    base_url: str
    api_version: str = "2024-05-01-preview"
    api_key: Optional[str] = None

class FoundryRESTClient:
    def __init__(self, cfg: FoundryRESTConfig):
        self.cfg = cfg

    def _headers(self) -> Dict[str, str]:
        h: Dict[str, str] = {"Content-Type": "application/json"}
        if self.cfg.api_key:
            h["api-key"] = self.cfg.api_key
        return h

    # --- Skeleton methods (adapt to your Foundry tenant) ---------------------

    def create_agent(
        self,
        *,
        name: str,
        model_deployment: str,
        temperature: float,
        system_instructions: str,
        tools: Optional[list[dict]] = None,
        knowledge_files: Optional[list[str]] = None,
    ) -> Dict[str, Any]:
        """Create an agent. Adapt the URL/body to your Foundry agent service."""
        url = f"{self.cfg.base_url}/agents?api-version={self.cfg.api_version}"
        payload: Dict[str, Any] = {
            "name": name,
            "model": {"deployment": model_deployment},
            "temperature": temperature,
            "system_instructions": system_instructions,
        }
        if tools:
            payload["tools"] = tools
        if knowledge_files:
            payload["knowledge_files"] = knowledge_files

        r = requests.post(url, headers=self._headers(), data=json.dumps(payload), timeout=60)
        r.raise_for_status()
        return r.json()

    def run_agent(self, *, agent_id: str, user_input: str) -> Dict[str, Any]:
        """Run an agent with a single-turn input. Adapt response parsing as needed."""
        url = f"{self.cfg.base_url}/agents/{agent_id}:run?api-version={self.cfg.api_version}"
        payload = {"input": user_input}
        r = requests.post(url, headers=self._headers(), data=json.dumps(payload), timeout=120)
        r.raise_for_status()
        return r.json()
