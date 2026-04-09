# Usage

## Launch

```bash
# Option A: run the module directly
python3 -m codex_switcher.app

# Option B: use the launcher script (auto-detects and installs deps)
./run.sh

# Option C: use the built .app (requires make app first)
open "dist/Codex Switcher.app"
```

After launching, the current model's short name (e.g. `sonnet-4.6`) appears in the macOS menubar.

## Menu Items

Click the menubar icon to see the following options:

| Menu Item | Description |
|-----------|-------------|
| **Current: ...** | Shows the full name of the active model |
| **Model list** | All enabled models; the active one has a checkmark |
| **Reasoning Effort** | Submenu with `low` / `medium` / `high` / `xhigh` |
| **Dashboard** | Opens the Dashboard panel for visual model and provider management |
| **Open config.toml** | Opens the Codex config file directly |
| **Quit** | Exits the Switcher |

## Switching Models

1. Click the model short name in the menubar
2. Select the target model from the dropdown
3. The tool automatically:
   - Updates `model`, `model_provider`, and `model_reasoning_effort` in `~/.codex/config.toml`
   - Kills and restarts Codex Desktop

During the switch, the menubar title briefly shows `...` and updates to the new model's short name once complete.

## Adjusting Reasoning Effort

Use the **Reasoning Effort** submenu to change inference intensity without restarting Codex:

- `low` -- fastest response, suitable for simple tasks
- `medium` -- balanced speed and quality
- `high` -- default, suitable for most scenarios
- `xhigh` -- highest quality, suitable for complex reasoning

## Dashboard

Click **Dashboard** in the menu to open a native configuration window with the following capabilities:

- **Model management** -- add, edit, and delete models
- **Enable/disable** -- toggle whether a model appears in the menubar
- **Provider settings** -- modify the provider's Key, Name, Base URL, and Env Key
- **Default Reasoning Effort** -- select the default reasoning intensity

Changes made in the Dashboard are written to `switcher_config.json` immediately. The menubar checks for config changes every second and refreshes automatically.
