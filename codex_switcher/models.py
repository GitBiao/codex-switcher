# Copyright 2025 GitBiao
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Load and manage model presets from switcher_config.json."""

import json
import os
from pathlib import Path
from typing import Any

_DEFAULT_CONFIG_PATH = Path(__file__).parent / "switcher_config.json"

REASONING_EFFORTS = ["low", "medium", "high", "xhigh"]


def load_switcher_config(path: str | Path | None = None) -> dict[str, Any]:
    path = Path(path) if path else _DEFAULT_CONFIG_PATH
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_switcher_config(data: dict[str, Any], path: str | Path | None = None) -> None:
    path = Path(path) if path else _DEFAULT_CONFIG_PATH
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def get_models(config: dict[str, Any]) -> list[dict[str, str]]:
    """Return only enabled models (for menubar display)."""
    return [m for m in config.get("models", []) if m.get("enabled", True)]


def get_all_models(config: dict[str, Any]) -> list[dict[str, str]]:
    """Return all models including disabled ones (for dashboard)."""
    return config.get("models", [])


def get_provider(config: dict[str, Any]) -> dict[str, str]:
    return config.get("provider", {})


def get_default_reasoning_effort(config: dict[str, Any]) -> str:
    return config.get("default_reasoning_effort", "high")
