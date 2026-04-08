# Codex Model Switcher

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10+-green.svg)](https://www.python.org)
[![macOS](https://img.shields.io/badge/Platform-macOS-lightgrey.svg)](https://www.apple.com/macos)

[中文](README.md) | **English**

A macOS menubar tool for switching [OpenRouter](https://openrouter.ai/) models in [Codex Desktop](https://openai.com/index/introducing-codex/) with one click.

## Why

When Codex Desktop uses a custom provider (e.g. OpenRouter), its main UI does not show a model selector. Switching models requires manually editing `~/.codex/config.toml` and restarting the app. This tool wraps that workflow into a single menubar click.

## Screenshots

<table>
  <tr>
    <td align="center"><b>Menubar</b></td>
    <td align="center"><b>Switch to GPT-4o</b></td>
    <td align="center"><b>Switch to Sonnet 4.6</b></td>
  </tr>
  <tr>
    <td><img src="public/switcher_main.png" width="280"/></td>
    <td><img src="public/desc_gpt4o.png" width="280"/></td>
    <td><img src="public/desc_sonnet4.6.png" width="280"/></td>
  </tr>
</table>

## Quick Start

**1. Clone & install**

```bash
git clone https://github.com/GitBiao/codex-switcher.git
cd codex-switcher
pip3 install -r requirements.txt
```

**2. Set environment variable**

```bash
export OPENROUTER_API_KEY="sk-or-..."
```

**3. Run**

```bash
# Option A: run the module directly
python3 -m codex_switcher.app

# Option B: use the launcher script (auto-installs deps)
./run.sh
```

## Features

- **One-click model switching** -- pick a model from the menubar, config is updated and Codex restarts automatically
- **Reasoning Effort control** -- choose from low / medium / high / xhigh
- **Quick edit** -- open the model presets or config.toml directly
- **Auto-start** -- supports macOS LaunchAgent for login startup

## Project Structure

```
codex-switcher/
├── codex_switcher/              # Core Python package
│   ├── __init__.py
│   ├── app.py                   # Menubar app entry point
│   ├── config_manager.py        # config.toml read/write
│   ├── models.py                # Model preset management
│   ├── process_manager.py       # Codex process lifecycle
│   └── switcher_config.json     # Model preset config
├── docs/                        # Documentation
│   ├── installation.md / installation_en.md
│   ├── usage.md / usage_en.md
│   ├── configuration.md / configuration_en.md
│   └── autostart.md / autostart_en.md
├── public/                      # Screenshots
│   ├── desc_gpt4o.png           # GPT-4o switch screenshot
│   ├── desc_sonnet4.6.png       # Sonnet 4.6 switch screenshot
│   └── switcher_main.png        # Menubar screenshot
├── LICENSE                      # Apache License 2.0
├── README.md                    # Documentation (Chinese)
├── README_EN.md                 # Documentation (English)
├── requirements.txt             # Python dependencies
└── run.sh                       # Launcher script
```

## Documentation

| Document | Description |
|----------|-------------|
| [Installation](docs/installation_en.md) | Requirements, dependency setup, environment variables |
| [Usage](docs/usage_en.md) | Launch methods, menu operations, model switching |
| [Configuration](docs/configuration_en.md) | switcher_config.json & config.toml reference |
| [Auto-start](docs/autostart_en.md) | macOS LaunchAgent setup |

## Prerequisites

1. macOS with Python 3.10+
2. [Codex Desktop](https://openai.com/index/introducing-codex/) installed at `/Applications/Codex.app`
3. `OPENROUTER_API_KEY` environment variable set

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=GitBiao/codex-switcher&type=Date)](https://star-history.com/#GitBiao/codex-switcher&Date)

## License

This project is licensed under the [Apache License 2.0](LICENSE).
