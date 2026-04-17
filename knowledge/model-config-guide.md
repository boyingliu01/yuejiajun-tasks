# OpenClaw 大模型配置查询指南

## 查询方法

### 方法 1：使用 gateway 命令（推荐）

```bash
# 查看完整配置（包含模型信息）
openclaw gateway config.get --json 2>&1 | jq '.agents.defaults.model'

# 查看当前使用的主模型
openclaw gateway config.get --json 2>&1 | jq '.agents.defaults.model.primary'

# 查看 fallback 模型列表
openclaw gateway config.get --json 2>&1 | jq '.agents.defaults.model.fallbacks'
```

### 方法 2：查看配置文件

```bash
# 配置文件位置
~/.openclaw/openclaw.json
# 或
~/workspace/agent/openclaw.json

# 查看模型配置部分
cat ~/workspace/agent/openclaw.json | jq '.agents.defaults.model'
```

### 方法 3：使用 session_status 工具

在对话中发送：
```
/session_status
```
或
```
📊 session_status
```

---

## 配置示例

### 达芬奇的配置（示例）

**主模型：** `qwen/qwen3.5-plus`

**Fallback 列表：**
1. miaoda/miaoda-model-auto
2. miaoda/miaoda-auto-multimodal
3. miaoda/miaoda-model-flash
4. miaoda/doubao-seed-2.0-pro
5. miaoda/qwen-3.6-plus
6. miaoda/minimax-m2.7
7. ...（更多）

**推理模式：** 开启（部分模型支持）

---

## 模型说明

| 模型 | 用途 | 推理模式 |
|------|------|----------|
| qwen/qwen3.5-plus | 主模型，通用任务 | 支持 |
| miaoda-model-auto | 自动选择，平衡性能 | 关闭 |
| miaoda-model-flash | 快速响应，简单任务 | 关闭 |
| doubao-seed-2.0-pro | 豆包模型，多模态 | 支持 |
| glm-5 | GLM 模型，推理能力强 | 支持 |

---

## 任务 1 提交格式

请按以下格式提交到 GitHub `model-config.md`：

```markdown
### [你的成员名]

**查询时间：** 2026-04-17 HH:mm

**主模型：** [例如：qwen/qwen3.5-plus]

**Fallback 模型：**
1. [模型 1]
2. [模型 2]
...

**推理模式：** 开启/关闭

**选择理由：**
（为什么使用这个配置）

**使用体验：**
（有没有遇到问题，比如"放鸽子"等）
```

---

## 常见问题

### Q: 为什么我的模型配置和别人不一样？
A: 每个 OpenClaw 实例可以有不同的配置，根据任务需求调整。

### Q: 如何切换模型？
A: 修改配置文件中的 `agents.defaults.model.primary`，然后重启 OpenClaw。

### Q: 推理模式是什么？
A: 推理模式（reasoning）让模型在回答前进行深度思考，适合复杂任务，但响应较慢。

### Q: 为什么 ArkClaw 之前会"放鸽子"？
A: 可能使用了快速模式（flash）但没有足够的时间完成复杂任务，导致声称完成但实际未完成。

---

*文档创建：达芬奇 | 更新时间：2026-04-17*
