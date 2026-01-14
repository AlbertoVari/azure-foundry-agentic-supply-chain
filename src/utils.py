from __future__ import annotations
from pathlib import Path
from dotenv import load_dotenv

REPO_ROOT = Path(__file__).resolve().parents[1]

def load_env() -> None:
    """Load environment variables from .env if present."""
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path)

def read_prompt(filename: str) -> str:
    """Read a prompt text file from prompts/."""
    p = REPO_ROOT / "prompts" / filename
    return p.read_text(encoding="utf-8")
