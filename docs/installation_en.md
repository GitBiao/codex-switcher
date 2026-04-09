# Installation Guide

## Requirements

- **OS**: macOS (depends on the `rumps` menubar framework)
- **Python**: 3.10+
- **Codex Desktop**: installed at `/Applications/Codex.app`

## Install Dependencies

```bash
git clone https://github.com/GitBiao/codex-switcher.git
cd codex-switcher
pip3 install -r requirements.txt
```

Dependencies:

| Package | Purpose |
|---------|---------|
| [rumps](https://github.com/jaredks/rumps) | macOS menubar application framework |
| [tomlkit](https://github.com/sdispater/tomlkit) | Format-preserving TOML read/write |
| [pywebview](https://github.com/nicegui-org/pywebview) | Native window for the Dashboard |

## Set Environment Variable

Codex accesses models via OpenRouter, which requires an API key:

```bash
export OPENROUTER_API_KEY="sk-or-..."
```

It is recommended to add the above line to `~/.zshrc` or `~/.bashrc` for persistence.

## Verify Installation

```bash
python3 -c "import rumps, tomlkit, webview; print('OK')"
```

If it prints `OK`, the dependencies are installed correctly.

## Build macOS .app (Optional)

To package Codex Switcher as a standalone macOS application:

```bash
make app
```

The output is located at `dist/Codex Switcher.app` and can be dragged into `/Applications`.

> **Tip**: `py2app` is installed automatically during the build. Run `make clean` to remove build artifacts.
