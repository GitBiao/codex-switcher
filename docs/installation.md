# 安装指南

## 方式一：直接下载（推荐）

无需安装 Python 环境，下载预构建的 macOS 应用即可使用。

1. 前往 [Releases 页面](https://github.com/GitBiao/codex-switcher/releases) 下载最新的 `Codex.Switcher.app.zip`
2. 解压后将 `Codex Switcher.app` 拖入 `/Applications` 目录
3. 配置环境变量（参见下方 [配置环境变量](#配置环境变量) 章节）
4. 双击打开应用

> **提示**: 首次打开可能提示"无法验证开发者"，请前往 **系统设置 → 隐私与安全性** 点击"仍要打开"。

## 方式二：从源码安装

### 环境要求

- **操作系统**: macOS（依赖 `rumps` 菜单栏框架）
- **Python**: 3.10+
- **Codex Desktop**: 已安装至 `/Applications/Codex.app`

### 安装依赖

```bash
git clone https://github.com/GitBiao/codex-switcher.git
cd codex-switcher
pip3 install -r requirements.txt
```

依赖包：

| 包名 | 用途 |
|------|------|
| [rumps](https://github.com/jaredks/rumps) | macOS 菜单栏应用框架 |
| [tomlkit](https://github.com/sdispater/tomlkit) | 保留格式的 TOML 读写 |
| [pywebview](https://github.com/nicegui-org/pywebview) | Dashboard 原生窗口 |

### 验证安装

```bash
python3 -c "import rumps, tomlkit, webview; print('OK')"
```

输出 `OK` 即表示依赖安装成功。

### 构建 macOS .app（可选）

如果希望自行构建独立的 macOS 应用：

```bash
make app
```

构建产物位于 `dist/Codex Switcher.app`，可拖入 `/Applications` 目录使用。

> **提示**: 构建前会自动安装 `py2app`。如需清理构建产物，运行 `make clean`。

## 配置环境变量

无论哪种安装方式，Codex 通过 OpenRouter 访问多模型，都需要设置 API Key：

```bash
export OPENROUTER_API_KEY="sk-or-..."
```

建议将上述命令添加到 `~/.zshrc` 或 `~/.bashrc` 中以持久化。

获取 API Key：[https://openrouter.ai/keys](https://openrouter.ai/keys)
