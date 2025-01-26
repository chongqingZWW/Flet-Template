import flet as ft
from app.view.base_view import BaseView
from app.tasks.SchedulerManager import SchedulerManager
from datetime import datetime
import pytz  # 添加时区支持

class TaskView(BaseView):
    """任务管理视图"""

    def __init__(self, page: ft.Page, viewmodel):
        super().__init__(page, viewmodel)
        self.scheduler = SchedulerManager()
        self.scheduler.start()  # 启动调度器
        self.tasks_data = None  # 保存表格引用
        self.view = self._build_view()
        # 初始化后立即加载任务列表
        self.page.on_load = lambda _: self.refresh_tasks()

    def _build_view(self):
        return ft.Container(
            content=ft.Column([
                self._build_header(),
                ft.Divider(),
                ft.Tabs(
                    selected_index=0,
                    animation_duration=300,
                    tabs=[
                        ft.Tab(
                            text="任务列表",
                            content=self._build_task_list()
                        ),
                        ft.Tab(
                            text="添加任务",
                            content=self._build_add_task()
                        ),
                    ],
                )
            ], scroll=ft.ScrollMode.AUTO, expand=True),
            padding=20,
        )

    def _build_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("任务管理", size=30, weight=ft.FontWeight.BOLD),
                ft.Text("管理定时任务和计划任务", size=16, color=ft.colors.GREY_700),
            ]),
            margin=ft.margin.only(bottom=20)
        )

    def show_edit_dialog(self, job):
        """显示编辑对话框"""
        def save_changes(e):
            try:
                if trigger_type.value == "cron":
                    self.scheduler.modify_job(
                        job.id,
                        func=self.scheduler.execute_task,
                        trigger='cron',
                        args=[job.args[0], task_name.value],
                        hour=int(cron_hour.value),
                        minute=int(cron_minute.value)
                    )
                elif trigger_type.value == "interval":
                    self.scheduler.modify_job(
                        job.id,
                        func=self.scheduler.execute_task,
                        trigger='interval',
                        args=[job.args[0], task_name.value],
                        hours=int(interval_hours.value)
                    )
                elif trigger_type.value == "date":
                    self.scheduler.modify_job(
                        job.id,
                        func=self.scheduler.execute_task,
                        trigger='date',
                        args=[job.args[0], task_name.value],
                        run_date=date_time.value
                    )
                
                self.page.dialog.open = False
                self.page.update()
                self.refresh_tasks()
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("任务修改成功！"))
                )
            except Exception as e:
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text(f"修改失败: {str(e)}"))
                )

        def update_form_visibility(e):
            """更新表单可见性"""
            cron_settings.visible = trigger_type.value == "cron"
            interval_settings.visible = trigger_type.value == "interval"
            date_settings.visible = trigger_type.value == "date"
            self.page.update()

        # 创建编辑表单
        task_name = ft.TextField(
            label="任务名称",
            value=job.args[1] if job.args else "",
        )
        
        trigger_type = ft.Dropdown(
            label="触发器类型",
            options=[
                ft.dropdown.Option("cron", "Cron 表达式"),
                ft.dropdown.Option("interval", "时间间隔"),
                ft.dropdown.Option("date", "指定时间"),
            ],
            value="cron",
            on_change=update_form_visibility,
        )

        # Cron 触发器选项
        cron_hour = ft.TextField(label="小时 (0-23)", value="8")
        cron_minute = ft.TextField(label="分钟 (0-59)", value="0")
        cron_settings = ft.Column([
            cron_hour,
            cron_minute,
        ], visible=True)

        # 间隔触发器选项
        interval_hours = ft.TextField(label="间隔小时数", value="1")
        interval_settings = ft.Column([
            interval_hours,
        ], visible=False)

        # 日期触发器选项
        date_time = ft.TextField(
            label="执行时间",
            hint_text="格式: YYYY-MM-DD HH:MM:SS",
        )
        date_settings = ft.Column([
            date_time,
        ], visible=False)

        # 显示对话框
        self.page.dialog = ft.AlertDialog(
            title=ft.Text("修改任务"),
            content=ft.Column([
                task_name,
                trigger_type,
                ft.Divider(),
                ft.Text("触发器设置:", size=16, weight=ft.FontWeight.BOLD),
                cron_settings,
                interval_settings,
                date_settings,
            ], spacing=10),
            actions=[
                ft.TextButton("取消", on_click=lambda e: setattr(self.page.dialog, 'open', False)),
                ft.TextButton("保存", on_click=save_changes),
            ],
        )
        self.page.dialog.open = True
        self.page.update()

    def _build_task_list(self):
        """构建任务列表"""
        # 创建任务列表
        self.tasks_data = ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("任务ID")),
                ft.DataColumn(ft.Text("任务名称")),
                ft.DataColumn(ft.Text("触发器")),
                ft.DataColumn(ft.Text("下次执行时间")),
                ft.DataColumn(ft.Text("状态")),
                ft.DataColumn(ft.Text("操作")),
            ],
            rows=[],
        )

        # 构建布局
        return ft.Column([
            ft.Row([
                ft.ElevatedButton(
                    "刷新",
                    icon=ft.icons.REFRESH,
                    on_click=lambda _: self.refresh_tasks(),
                ),
            ], alignment=ft.MainAxisAlignment.END),
            self.tasks_data,
        ], spacing=20)

    def _build_add_task(self):
        """构建添加任务表单"""
        def add_task(e):
            try:
                if not task_name.value:
                    raise ValueError("任务名称不能为空")

                if trigger_type.value == "cron":
                    self.scheduler.add_cron_job(
                        func=self.scheduler.execute_task,
                        cron_rule=f"{cron_minute.value} {cron_hour.value} * * *",
                        args=[task_name.value, task_name.value],
                        job_id=f"task_{task_name.value}"
                    )
                elif trigger_type.value == "interval":
                    self.scheduler.add_interval_job(
                        func=self.scheduler.execute_task,
                        hours=int(interval_hours.value),
                        args=[task_name.value, task_name.value],
                        job_id=f"task_{task_name.value}"
                    )
                elif trigger_type.value == "date":
                    self.scheduler.add_date_job(
                        func=self.scheduler.execute_task,
                        run_date=date_time.value,
                        args=[task_name.value, task_name.value],
                        job_id=f"task_{task_name.value}"
                    )

                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text("任务添加成功！"))
                )
                
                # 清空输入框
                task_name.value = ""
                if trigger_type.value == "cron":
                    cron_hour.value = "8"
                    cron_minute.value = "0"
                elif trigger_type.value == "interval":
                    interval_hours.value = "1"
                else:
                    date_time.value = ""
                
                self.page.update()
                self.refresh_tasks()  # 使用类方法刷新
                
            except ValueError as e:
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text(str(e)))
                )
            except Exception as e:
                self.page.show_snack_bar(
                    ft.SnackBar(content=ft.Text(f"添加失败: {str(e)}"))
                )

        def update_form_visibility(e):
            """更新表单可见性"""
            cron_settings.visible = trigger_type.value == "cron"
            interval_settings.visible = trigger_type.value == "interval"
            date_settings.visible = trigger_type.value == "date"
            self.page.update()

        task_name = ft.TextField(
            label="任务名称",
            hint_text="请输入任务名称",
            value="",  # 确保初始值为空字符串
            on_change=lambda e: setattr(task_name, 'error_text', None),  # 清除错误提示
        )

        trigger_type = ft.Dropdown(
            label="触发器类型",
            options=[
                ft.dropdown.Option("cron", "Cron 表达式"),
                ft.dropdown.Option("interval", "时间间隔"),
                ft.dropdown.Option("date", "指定时间"),
            ],
            value="cron",
            on_change=update_form_visibility,  # 添加切换事件
        )

        # Cron 触发器选项
        cron_hour = ft.TextField(label="小时 (0-23)", value="8")
        cron_minute = ft.TextField(label="分钟 (0-59)", value="0")
        cron_settings = ft.Column([
            cron_hour,
            cron_minute,
        ], visible=True)  # 默认显示

        # 间隔触发器选项
        interval_hours = ft.TextField(label="间隔小时数", value="1")
        interval_settings = ft.Column([
            interval_hours,
        ], visible=False)

        # 日期触发器选项
        date_time = ft.TextField(
            label="执行时间",
            hint_text="格式: YYYY-MM-DD HH:MM:SS",
        )
        date_settings = ft.Column([
            date_time,
        ], visible=False)

        return ft.Container(
            content=ft.Column([
                task_name,
                trigger_type,
                ft.Divider(),
                ft.Text("触发器设置:", size=16, weight=ft.FontWeight.BOLD),
                cron_settings,
                interval_settings,
                date_settings,
                ft.ElevatedButton(
                    "添加任务",
                    icon=ft.icons.ADD,
                    on_click=add_task,
                ),
            ], spacing=20),
            padding=20,
        )

    def get_task_status(self, job):
        """获取任务状态"""
        if job.next_run_time is None:
            return "已暂停", ft.colors.GREY
        
        # 转换为本地时间进行比较
        local_tz = pytz.timezone('Asia/Shanghai')
        now = datetime.now(local_tz)
        
        if job.next_run_time > now:
            return "运行中", ft.colors.GREEN
        else:
            return "已过期", ft.colors.RED

    def refresh_tasks(self):
        """刷新任务列表"""
        try:
            if not self.tasks_data:
                return
                
            self.tasks_data.rows = []
            jobs = self.scheduler.get_jobs()
            
            if not jobs:
                # 如果没有任务，显示空状态
                self.tasks_data.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text("暂无任务")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                            ft.DataCell(ft.Text("")),
                        ],
                    )
                )
            else:
                for job in jobs:
                    status, color = self.get_task_status(job)
                    self.tasks_data.rows.append(
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text(job.id)),
                                ft.DataCell(ft.Text(job.args[1] if job.args else "未命名")),
                                ft.DataCell(ft.Text(str(job.trigger))),
                                ft.DataCell(ft.Text(
                                    job.next_run_time.astimezone(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S')
                                    if job.next_run_time else "无"
                                )),
                                ft.DataCell(
                                    ft.Container(
                                        content=ft.Text(status, color=ft.colors.WHITE),
                                        bgcolor=color,
                                        padding=5,
                                        border_radius=5,
                                    )
                                ),
                                ft.DataCell(
                                    ft.Row([
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            icon_color=ft.colors.BLUE,
                                            tooltip="编辑",
                                            on_click=lambda _, x=job: self.show_edit_dialog(x),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.PAUSE if status == "运行中" else ft.icons.PLAY_ARROW,
                                            icon_color=ft.colors.BLUE,
                                            tooltip="暂停/恢复",
                                            on_click=lambda _, x=job.id, s=status: self.toggle_job(x, s),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            icon_color=ft.colors.RED,
                                            tooltip="删除",
                                            on_click=lambda _, x=job.id: self.delete_job(x),
                                        ),
                                    ])
                                ),
                            ],
                        )
                    )
            self.page.update()
        except Exception as e:
            import traceback
            print(traceback.format_exc())  # 打印详细错误信息
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"刷新任务列表失败: {str(e)}"))
            )

    def toggle_job(self, job_id, status):
        """切换任务状态"""
        try:
            if status == "运行中":
                self.scheduler.pause_job(job_id)
            else:
                self.scheduler.resume_job(job_id)
            self.refresh_tasks()
        except Exception as e:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"操作失败: {str(e)}"))
            )

    def delete_job(self, job_id):
        """删除任务"""
        try:
            self.scheduler.remove_job(job_id)
            self.refresh_tasks()
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text("任务已删除"))
            )
        except Exception as e:
            self.page.show_snack_bar(
                ft.SnackBar(content=ft.Text(f"删除失败: {str(e)}"))
            ) 