# 运行环境准备与发布边界

本发布包不含Altium安装、原生pas/PrjScr、DFM、机器profile或可部署Python适配器；先取得受认可的运行实现，再按以下步骤接入。这里没有自动安装命令。

1. 明确Altium版本、代码来源与许可、唯一脚本集和宿主入口；旧实验工程列deprecated，恢复钩子不作日常入口。
2. 使用自己机器的显式profile、脚本目录和ASCII IPC目录；随机生成候选身份。响应与server编译身份必须匹配，不能照抄本仓库的合成ID。
3. 记录脚本集11文件的字节与SHA，另行登记宿主工具；保持client允许集/profile/release一致，重算profile文件哈希。机器绑定入口的适配须单独验收。
4. 准备明确授权的TEMP测试工程/库，记录源与副本前后SHA；不得默认复制真实库、保存真实工程或改工程搜索路径。
5. Win32进程与可见窗口交叉选择已有宿主。没有宿主时不擅自新开；瞬态转发器与第二个持久AD宿主区别记录。
6. 先确认目标文档聚焦并已加载。未加载时能否打开由任务许可决定，不能为了跑通擅自补操作。
7. 定时器/脚本服务启动后等待新session_start与first_tick，再独立ping/version。只看到进程或旧日志不算成功。
8. 从只读命令开始，通过[任务模板](../templates/task.json)逐项跑[Pipeline](pipeline.md)。写操作、保存重开和生产交付是不同授权门禁。

## 维护和宿主守护

运行中的MCP与独立RunScript共用脚本引擎，不能并发。先暂停守护或确认守护未运行，再正常停MCP并证实session_end；探针后恢复受认可服务，保留所有未保存文档。

已验证的守护约定：默认5s、连续2次失败、最大3次重启；每失败序列至多一次，恢复后清零。--once是纯探测且永不重启；pause时退出0且只记录paused。预算用尽记录budget_exhausted并立即退出。事件为probe_ok/probe_fail/paused/restart_begin/restart_result/budget_exhausted。

停机验收中用exchange ping检查超时；handshake可能拉起服务，不能用于该负向测试。自动恢复耗时按首次probe_fail至首次probe_ok计算，原始日志和时区必须留存。

AD内调度器异常走fail-closed。外部守护能恢复脚本服务停止，不代表能从AD进程退出、断点、模态框、native崩溃或系统重启中恢复。未知写结果不自动重放；恢复后先核数据。守护退出、日志轮转、OS启动和任务调度是独立部署责任，本包不配置它们。
