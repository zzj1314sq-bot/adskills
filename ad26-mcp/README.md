<div align="center">

# AD26 MCP

**协议清楚，准备有据，流程可接续。**

文档包 **1.0.1** · 原生协议 **26** · 原生命令 **47** · 标准 MCP 工具 **5**

[环境准备](docs/setup.md) · [通信协议](docs/protocol.md) · [能力 Pipeline](docs/pipeline.md) · [任务模板](templates/task.json)

</div>

> 这是文档与接口契约包，不是运行时安装包。克隆本仓库不会连接、启动或修改 AD。

## 从哪里开始

| 你的角色 / 目标 | 阅读路线 |
|---|---|
| 第一次使用 | 环境准备 → 验证范围 → 任务模板 |
| 开发适配器 | 通信协议 → Schema → 合成示例 → 命令目录 |
| 移植新能力 | Pipeline → 任务模板 → 按门禁收集证据 |
| 让 Agent 接续工作 | 接续提示 → 本项目自己的基线与 current-state |

## 三步复用

### 1. 准备本机基线

按 [环境准备](docs/setup.md) 确认自己的 Altium 版本、受认可实现、脚本指纹和测试副本。本包没有提供可部署的原生脚本或机器配置。

### 2. 明确本轮任务

从 [task.json](templates/task.json) 填写输入、允许修改的文件、是否允许保存、正反向判据和回滚步骤。按 [Pipeline](docs/pipeline.md) 选择只读、探针、安装或运行时分支。

### 3. 先跑离线校验

在仓库根目录运行：

```bash
python ad26-mcp/tools/validate_package.py
```

只用 Python 标准库，不调用 AD、MCP 或外部网络。通过后仍需在获准环境完成任务要求的原生验收。

## 看懂三层通信

```mermaid
flowchart LR
  A[Agent / MCP调用方] --> B[stdio MCP适配器]
  B --> C[受控 Python 客户端]
  C --> D[文件 IPC]
  D --> E[AD26 定时器与 handler]
```

- **标准 MCP 层**：工具发现与 tools/call；当前所检查实现暴露 5 个工具。
- **受控客户端层**：参数门禁、能力集、身份与文件指纹核验。
- **原生 IPC 层**：逐请求文件、协议 26、命令派发与匹配 ID 的响应。

47 个原生命令不会自动成为 47 个独立 MCP 工具。协议 26 也不是 MCP 标准版本号。[完整协议 →](docs/protocol.md)

## 内容索引

| 主题 | 入口 |
|---|---|
| 请求 / 响应信封、错误与单位 | [protocol.md](docs/protocol.md) |
| 已加载、聚焦、宿主与守护 | [setup.md](docs/setup.md) |
| CAP-0 至 CAP-8 执行门禁 | [pipeline.md](docs/pipeline.md) |
| 47 条原生命令 | [commands.md](docs/commands.md) / [机器清单](catalog/commands.json) |
| 已验证范围与尚缺能力 | [verification.md](docs/verification.md) |
| 请求、响应与几何数据 Schema | [request](schemas/request.schema.json) / [response](schemas/response.schema.json) / [geometry](schemas/geometry-data.schema.json) |
| 合成示例 | [请求](examples/request.ping.json) / [成功](examples/response.ping.json) / [拒绝](examples/response.error.json) / [几何](examples/response.geometry.json) |
| 任务与接续 | [task.json](templates/task.json) / [continuation.md](templates/continuation.md) |
| 更新与完整性 | [Changelog](CHANGELOG.md) / [publication.json](publication.json) |

## 当前交付与边界

| 已包含 | 未随包交付 |
|---|---|
| 协议、流程、Schema、任务模板 | Altium 原生 pas / PrjScr / DFM |
| 合成示例与离线校验器 | 安装器、机器 profile、可直接部署的客户端 |
| 历史验证范围摘要 | 真实工程、器件库、原始日志与运行凭据 |

`verified` 必须绑定源码、参数、前提与证据范围。封装创建探针不等于创建命令已加入清单，服务恢复不等于所有崩溃场景已验。

所有示例均为合成数据，路径仅用 `C:\AD26_TEST` 占位。上游运行实现需单独取得并审查许可，本包没有代为重分发。

[返回 AD Skills 首页 →](../README.md)
