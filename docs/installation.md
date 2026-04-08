# 安装指南

## 环境要求

- **操作系统**: macOS（依赖 `rumps` 菜单栏框架）
- **Python**: 3.10+
- **Codex Desktop**: 已安装至 `/Applications/Codex.app`

## 安装依赖

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

## 配置环境变量

Codex 通过 OpenRouter 访问多模型，需要设置 API Key：

```bash
export OPENROUTER_API_KEY="sk-or-..."
```

建议将上述命令添加到 `~/.zshrc` 或 `~/.bashrc` 中以持久化。

## 验证安装

```bash
python3 -c "import rumps, tomlkit; print('OK')"
```

输出 `OK` 即表示依赖安装成功。
