# 配置详解

## switcher_config.json

位于 `codex_switcher/switcher_config.json`，定义了可切换的模型列表和 Provider 信息。

### 完整示例

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

### 字段说明

#### provider

| 字段 | 类型 | 说明 |
|------|------|------|
| `key` | string | Provider 标识符，写入 `config.toml` 的 `model_provider` |
| `name` | string | Provider 显示名称 |
| `base_url` | string | API 端点地址 |
| `env_key` | string | API Key 对应的环境变量名 |

#### models

数组，每个元素包含：

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 模型完整标识（如 `anthropic/claude-sonnet-4.6`） |
| `short_name` | string | 菜单栏显示的简称（如 `sonnet-4.6`） |
| `enabled` | boolean | 是否启用，`false` 时不出现在菜单栏（默认 `true`） |

#### default_reasoning_effort

默认推理强度，可选值：`low`、`medium`、`high`、`xhigh`。

### 自定义模型

在 `models` 数组中添加新条目即可。支持 [OpenRouter 上的所有模型](https://openrouter.ai/models)。

也可以通过菜单的 **Dashboard** 打开配置面板，可视化管理模型（添加、编辑、删除、启用/禁用）。

## config.toml

Codex Desktop 的配置文件，位于 `~/.codex/config.toml`。Switcher 会自动管理以下字段：

```toml
model = "anthropic/claude-sonnet-4.6"
model_provider = "openrouter"
model_reasoning_effort = "high"

[model_providers.openrouter]
name = "OpenRouter"
base_url = "https://openrouter.ai/api/v1"
env_key = "OPENROUTER_API_KEY"
```

> **注意**: Switcher 使用 `tomlkit` 进行增量更新，不会覆盖文件中的其他配置项和注释。
