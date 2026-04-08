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

"""Incrementally read/write ~/.codex/config.toml using tomlkit (preserves comments & formatting)."""

import os
from pathlib import Path

import tomlkit
from tomlkit import TOMLDocument


CODEX_HOME = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
CONFIG_PATH = CODEX_HOME / "config.toml"


def read_config() -> TOMLDocument:
    if CONFIG_PATH.exists():
        return tomlkit.parse(CONFIG_PATH.read_text(encoding="utf-8"))
    return tomlkit.document()


def write_config(doc: TOMLDocument) -> None:
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_PATH.write_text(tomlkit.dumps(doc), encoding="utf-8")


def get_current_model(doc: TOMLDocument) -> str | None:
    return doc.get("model")


def get_current_provider_key(doc: TOMLDocument) -> str | None:
    return doc.get("model_provider")


def get_current_reasoning_effort(doc: TOMLDocument) -> str | None:
    return doc.get("model_reasoning_effort")


def switch_model(
    model_id: str,
    provider_key: str,
    provider_name: str,
    base_url: str,
    env_key: str,
    reasoning_effort: str = "high",
) -> None:
    """Update config.toml: set model, provider, reasoning effort, and ensure provider block exists."""
    doc = read_config()

    doc["model"] = model_id
    doc["model_provider"] = provider_key
    doc["model_reasoning_effort"] = reasoning_effort

    providers = doc.get("model_providers")
    if providers is None:
        providers = tomlkit.table(is_super_table=True)
        doc["model_providers"] = providers

    if provider_key not in providers:
        provider_table = tomlkit.table()
        provider_table["name"] = provider_name
        provider_table["base_url"] = base_url
        provider_table["env_key"] = env_key
        providers[provider_key] = provider_table
    else:
        existing = providers[provider_key]
        existing["name"] = provider_name
        existing["base_url"] = base_url
        existing["env_key"] = env_key

    write_config(doc)


def set_reasoning_effort(effort: str) -> None:
    """Update only the reasoning effort field."""
    doc = read_config()
    doc["model_reasoning_effort"] = effort
    write_config(doc)
