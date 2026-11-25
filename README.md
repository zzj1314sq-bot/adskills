<div align="center">

# AD Skills

**把 AD26 自动化经验，整理成可验证、可复用的工程流程。**

A skill library based on Altium Designer

[![Docs validation](https://github.com/zzj1314sq-bot/adskills/actions/workflows/ad26-docs.yml/badge.svg)](https://github.com/zzj1314sq-bot/adskills/actions/workflows/ad26-docs.yml)
![Native commands](https://img.shields.io/badge/native_commands-47-2563eb)
![MCP tools](https://img.shields.io/badge/MCP_tools-5-0f766e)
![Package](https://img.shields.io/badge/package-docs_%26_pipeline-64748b)

[快速开始](#三步开始) · [协议说明](ad26-mcp/docs/protocol.md) · [复用 Pipeline](ad26-mcp/docs/pipeline.md) · [命令目录](ad26-mcp/docs/commands.md)

</div>

> 当前交付：**协议、流程、Schema 和任务模板**。不包含可直接安装运行的 Altium 服务端。

## 你可以用它做什么

- **看懂 AD26 MCP 的通信方式**：区分标准 MCP、Python 受控客户端和原生文件 IPC，知道请求如何进入 AD、结果如何返回。
- **复用一套稳定的能力开发流程**：从前提核验、探针、安装到验收、回滚和接续，避免每轮重新设计执行路线。
- **给下一次任务一个清晰起点**：用结构化模板记录授权、目标副本、精确判据和证据，不把口头结论当交付。
- **复用封装与原理图落地流程**：从手册参数、真实模型绑定到原图增量修改、限定转 PCB，区分设计要求和已经验证的能力。

## 三步开始

### 1. 选一个入口

| 我现在想做什么 | 从这里开始 |
|---|---|
| 第一次了解这个项目 | [AD26 文档包](ad26-mcp/README.md) |
| 接入自己的 AD26 环境 | [环境准备](ad26-mcp/docs/setup.md) |
| 移植或修复一条能力 | [Pipeline](ad26-mcp/docs/pipeline.md) |
| 查询命令与工具的区别 | [命令目录](ad26-mcp/docs/commands.md) |
| 设计封装、修改原理图并同步 PCB | [硬件设计流程](hardware-design/README.md) |
| 查看 AD26 单平台要求与当前缺口 | [平台要求](hardware-design/docs/platform-policy.md) |

### 2. 填一份任务模板

复制 [task.json](ad26-mcp/templates/task.json) 到自己的工作目录，填清允许修改的文件、测试副本、保存许可、请求参数和验收判据。

模板是被动数据，不会自行调用 AD。中文文档名、焦点和已加载状态等问题，按协议和准备流程处理。

### 3. 验证文档包

克隆或下载仓库后，在仓库根目录运行：

```bash
python ad26-mcp/tools/validate_package.py
```

无需启动 Altium、无需第三方 Python 依赖。它校验示例、Schema 子集、链接、参数规则和发布哈希；不执行原生 AD 验收。

## 一条可以接续的 Pipeline

```mermaid
flowchart LR
  A[准备与授权] --> B[契约与探针]
  B --> C[安装与验收]
  C --> D[持久化与运行时验证]
  D --> E[证据 回滚 接续]
```

只读取证、仅跑探针、安装验收、运行时收口各走对应分支。保存与重开需要独立授权；同源码、同前提的已验结果可以复用。

[查看 CAP-0 至 CAP-8 的完整阶段与门禁 →](ad26-mcp/docs/pipeline.md)

## 能力地图

| 命令族 | 原生命令数 | 主要覆盖 |
|---|---:|---|
| application | 7 | 健康、版本、文档、聚焦与进程派发 |
| project | 13 | 工程、统计、消息、网络和 BOM |
| generic | 10 | 原理图查询、限定编辑与几何提取 |
| library | 7 | 符号、模型来源、封装和焊盘 |
| pcb | 6 | PCB 统计、元件、叠层、机械层及专用丝印 |
| lo | 4 | 限定范围的同步相关接口 |

**47 条是原生命令登记数，标准 MCP 适配器目前只暴露 5 个工具。** 各项验证范围、写副作用和未覆盖场景见 [验证范围](ad26-mcp/docs/verification.md)。

## 文档导航

| 内容 | 文件 |
|---|---|
| 请求、响应、身份、错误与单位 | [协议](ad26-mcp/docs/protocol.md) |
| 本机基线、文档加载、维护与守护 | [环境准备](ad26-mcp/docs/setup.md) |
| 阶段输入、放行证据与失败分流 | [Pipeline](ad26-mcp/docs/pipeline.md) |
| 可读取的接口目录 | [命令目录](ad26-mcp/docs/commands.md) |
| 可被程序读取的接口目录 | [commands.json](ad26-mcp/catalog/commands.json) |
| 请求与响应的合成样例 | [examples](ad26-mcp/examples/request.ping.json) |
| 新一轮任务与跨聊接续 | [任务模板](ad26-mcp/templates/task.json) / [接续提示](ad26-mcp/templates/continuation.md) |
| 文档包更新 | [Changelog](ad26-mcp/CHANGELOG.md) |
| 封装、原理图与 PCB 增量流程 | [硬件设计记录](hardware-design/README.md) |
| 本次射频设计变更与新增电容 | [2026-11-25 实施记录](hardware-design/cases/2026-11-25-rf-incremental-update.md) |

<details>
<summary><strong>使用前了解的边界</strong></summary>

- 本仓库提供协议与工作流，没有附带原生脚本、安装器、机器 profile 或真实器件库。
- 入站参数保持 ASCII；出站 Unicode、文档焦点和已加载状态按具体接口核验。
- 探针通过、未保存写入、保存重开、业务设计完成是不同层级的证据。
- 历史验收不是对所有参数、所有工程或永久无人值守的保证。
- 示例全部为合成数据。正式工程与运行凭据应留在使用者自己的受控环境中。

</details>
