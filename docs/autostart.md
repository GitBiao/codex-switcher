# 开机自启动

通过 macOS LaunchAgent 可以实现开机自动启动 Codex Switcher。

## 创建 plist 文件

将以下内容保存到 `~/Library/LaunchAgents/com.codex-switcher.plist`：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.codex-switcher</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/local/bin/python3</string>
        <string>-m</string>
        <string>codex_switcher.app</string>
    </array>
    <key>WorkingDirectory</key>
    <string>/path/to/codex-switcher</string>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <false/>
</dict>
</plist>
```

> **注意**: 请将 `WorkingDirectory` 替换为项目实际路径，将 `ProgramArguments` 中的 Python 路径替换为 `which python3` 的输出。

## 加载服务

```bash
launchctl load ~/Library/LaunchAgents/com.codex-switcher.plist
```

## 卸载服务

```bash
launchctl unload ~/Library/LaunchAgents/com.codex-switcher.plist
```

## 查看状态

```bash
launchctl list | grep codex-switcher
```

## 查看日志

如需调试，可在 plist 中添加日志输出：

```xml
<key>StandardOutPath</key>
<string>/tmp/codex-switcher.stdout.log</string>
<key>StandardErrorPath</key>
<string>/tmp/codex-switcher.stderr.log</string>
```
