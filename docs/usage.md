# 使用说明

## 启动方式

```bash
# 方式一：直接运行模块
python3 -m codex_switcher.app

# 方式二：使用启动脚本（自动检测并安装依赖）
./run.sh
```

启动后，macOS 菜单栏会出现当前模型的简称（如 `sonnet-4.6`）。

## 菜单功能

点击菜单栏图标可看到以下选项：

| 菜单项 | 说明 |
|--------|------|
| **Current: ...** | 显示当前使用的模型全名 |
| **模型列表** | 所有可切换的模型，当前模型前有 checkmark |
| **Reasoning Effort** | 子菜单，可选 `low` / `medium` / `high` / `xhigh` |
| **Edit Models...** | 打开 `switcher_config.json` 编辑模型预设 |
| **Open config.toml** | 直接编辑 Codex 配置文件 |
| **Quit** | 退出 Switcher |

## 切换模型

1. 点击菜单栏中的模型简称
2. 在下拉列表中选择目标模型
3. 工具自动完成以下操作：
   - 更新 `~/.codex/config.toml` 中的 `model`、`model_provider`、`model_reasoning_effort`
   - 关闭并重启 Codex Desktop

切换过程中菜单栏标题会短暂显示为 `...`，完成后自动更新为新模型的简称。

## 调整 Reasoning Effort

通过 **Reasoning Effort** 子菜单可以调整推理强度，无需重启 Codex：

- `low` -- 最快响应，适合简单任务
- `medium` -- 平衡速度与质量
- `high` -- 默认值，适合大多数场景
- `xhigh` -- 最高质量，适合复杂推理
