# Installation Guide

## Option A: Direct Download (Recommended)

No Python environment required — download the pre-built macOS application.

1. Go to the [Releases page](https://github.com/GitBiao/codex-switcher/releases) and download the latest `Codex.Switcher.app.zip`
2. Unzip and drag `Codex Switcher.app` into `/Applications`
3. Set the environment variable (see [Set Environment Variable](#set-environment-variable) below)
4. Double-click to launch

> **Tip**: On first launch macOS may show "cannot verify the developer". Go to **System Settings → Privacy & Security** and click "Open Anyway".

## Option B: Install from Source

### Requirements

- **OS**: macOS (depends on the `rumps` menubar framework)
- **Python**: 3.10+
- **Codex Desktop**: installed at `/Applications/Codex.app`

### Install Dependencies

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

### Verify Installation

```bash
python3 -c "import rumps, tomlkit, webview; print('OK')"
```

If it prints `OK`, the dependencies are installed correctly.

### Build macOS .app (Optional)

To build a standalone macOS application yourself:

```bash
make app
```

The output is located at `dist/Codex Switcher.app` and can be dragged into `/Applications`.

> **Tip**: `py2app` is installed automatically during the build. Run `make clean` to remove build artifacts.

## Set Environment Variable

Regardless of the installation method, Codex accesses models via OpenRouter, which requires an API key:

```bash
export OPENROUTER_API_KEY="sk-or-..."
```

It is recommended to add the above line to `~/.zshrc` or `~/.bashrc` for persistence.

Get your API Key: [https://openrouter.ai/keys](https://openrouter.ai/keys)
