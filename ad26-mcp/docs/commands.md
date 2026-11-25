# 原生命令与MCP工具目录

本目录仅列登记命令，不臆造全部参数或完整元素Schema。具体参数与写副作用需核受认可实现；无标准工具映射时须通过受控exchange调用，不能直接tools/call命令名。

| 原生命令 | 对外标准工具 | 风险分类 |
|---|---|---|
| `application.ping` | `ad26_health` | read_or_observe |
| `application.get_version` | `ad26_health` | read_or_observe |
| `application.stop_server` | `ad26_stop` | stateful_review_command_contract |
| `application.get_open_documents` | 无独立映射 | read_or_observe |
| `application.get_active_document` | 无独立映射 | read_or_observe |
| `application.set_active_document` | 无独立映射 | stateful_review_command_contract |
| `application.run_process` | 无独立映射 | stateful_review_command_contract |
| `pcb.component_silk_frame` | `ad26_component_silk_frame` | stateful_review_command_contract |
| `lo.snapshot` | `ad26_lo_snapshot` | stateful_review_command_contract |
| `lo.sync` | `ad26_lo_sync` | stateful_review_command_contract |
| `lo.test_document` | 无独立映射 | stateful_review_command_contract |
| `lo.delete` | 无独立映射 | stateful_review_command_contract |
| `project.get_focused` | 无独立映射 | read_or_observe |
| `project.get_open_projects` | 无独立映射 | read_or_observe |
| `project.get_project_path` | 无独立映射 | read_or_observe |
| `project.get_documents` | 无独立映射 | read_or_observe |
| `project.compile` | 无独立映射 | stateful_review_command_contract |
| `project.open` | 无独立映射 | stateful_review_command_contract |
| `project.close` | 无独立映射 | stateful_review_command_contract |
| `project.get_messages` | 无独立映射 | read_or_observe |
| `project.get_compile_freshness` | 无独立映射 | read_or_observe |
| `project.get_design_stats` | 无独立映射 | read_or_observe |
| `project.get_nets` | 无独立映射 | read_or_observe |
| `project.find_component` | 无独立映射 | read_or_observe |
| `project.get_bom` | 无独立映射 | read_or_observe |
| `generic.query_objects` | 无独立映射 | read_or_observe |
| `generic.modify_objects` | 无独立映射 | stateful_review_command_contract |
| `generic.delete_objects` | 无独立映射 | stateful_review_command_contract |
| `generic.batch_modify` | 无独立映射 | stateful_review_command_contract |
| `generic.place_wire` | 无独立映射 | stateful_review_command_contract |
| `generic.place_net_label` | 无独立映射 | stateful_review_command_contract |
| `generic.place_port` | 无独立映射 | stateful_review_command_contract |
| `generic.place_sch_component_from_library` | 无独立映射 | stateful_review_command_contract |
| `generic.set_sch_components_parameters` | 无独立映射 | stateful_review_command_contract |
| `library.get_component_details` | 无独立映射 | read_or_observe |
| `library.set_current_component` | 无独立映射 | stateful_review_command_contract |
| `library.get_components` | 无独立映射 | read_or_observe |
| `library.uninstall_library` | 无独立映射 | persistent_library_registry_change_confirm_required |
| `library.set_model_source` | 无独立映射 | stateful_review_command_contract |
| `library.get_footprints` | 无独立映射 | read_or_observe |
| `library.get_footprint_pads` | 无独立映射 | read_or_observe |
| `pcb.get_board_statistics` | 无独立映射 | read_or_observe |
| `pcb.get_components` | 无独立映射 | read_or_observe |
| `pcb.get_layer_stackup` | 无独立映射 | read_or_observe |
| `pcb.get_mech_layer_names` | 无独立映射 | read_or_observe |
| `pcb.set_layer_visibility` | 无独立映射 | stateful_review_command_contract |
| `generic.get_sch_geometry` | 无独立映射 | read_or_observe |

47条为历史基线快照，不代表当前机器自动具备。创建封装探针不在清单内；真实卸载、真库放件及所有参数组合未全验。

回到[协议](protocol.md)或查看[机器清单](../catalog/commands.json)。
