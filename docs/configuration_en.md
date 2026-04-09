# Configuration Reference

## switcher_config.json

Located at `codex_switcher/switcher_config.json`. Defines the list of switchable models and provider information.

### Full Example

```json
{
  "provider": {
    "key": "openrouter",
    "name": "OpenRouter",
    "base_url": "https://openrouter.ai/api/v1",
    "env_key": "OPENROUTER_API_KEY"
  },
  "models": [
    { "id": "anthropic/claude-sonnet-4.6", "short_name": "sonnet-4.6", "enabled": true },
    { "id": "anthropic/claude-opus-4.6",   "short_name": "opus-4.6",   "enabled": true },
    { "id": "openai/gpt-5.4",             "short_name": "gpt-5.4",    "enabled": true },
    { "id": "openai/gpt-5.3-codex",       "short_name": "5.3-codex",  "enabled": true },
    { "id": "openai/gpt-4o-mini",          "short_name": "4o-mini",    "enabled": false },
    { "id": "deepseek/deepseek-v3.2",      "short_name": "ds-v3.2",   "enabled": true }
  ],
  "default_reasoning_effort": "high"
}
```

### Field Reference

#### provider

| Field | Type | Description |
|-------|------|-------------|
| `key` | string | Provider identifier, written to `model_provider` in config.toml |
| `name` | string | Provider display name |
| `base_url` | string | API endpoint URL |
| `env_key` | string | Environment variable name for the API key |

#### models

Array of objects, each containing:

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Full model identifier (e.g. `anthropic/claude-sonnet-4.6`) |
| `short_name` | string | Short name shown in the menubar (e.g. `sonnet-4.6`) |
| `enabled` | boolean | Whether the model is enabled; when `false` it is hidden from the menubar (defaults to `true`) |

#### default_reasoning_effort

Default reasoning intensity. Valid values: `low`, `medium`, `high`, `xhigh`.

### Custom Models

Add new entries to the `models` array. Any model available on [OpenRouter](https://openrouter.ai/models) is supported.

You can also open the **Dashboard** from the menu to visually manage models (add, edit, delete, enable/disable).

## config.toml

The Codex Desktop configuration file, located at `~/.codex/config.toml`. The Switcher automatically manages the following fields:

```toml
model = "anthropic/claude-sonnet-4.6"
model_provider = "openrouter"
model_reasoning_effort = "high"

[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"
```

> **Note**: The Switcher uses `tomlkit` for incremental updates and will not overwrite other config entries or comments in the file.
