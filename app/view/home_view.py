import flet as ft
from app.view.base_view import BaseView
import platform
import psutil
from datetime import datetime


class HomeView(BaseView):
    """首页视图"""

    def __init__(self, page: ft.Page, viewmodel):
        super().__init__(page, viewmodel)
        # 初始化性能监控文本控件
        self.performance_text = ft.Text("获取中...", size=14)
        self.network_text = ft.Text("获取中...", size=14)
        self.battery_text = ft.Text("获取中...", size=14)
        self.boot_text = ft.Text("获取中...", size=14)
        
        self.view = self._build_view()
        # 添加定时更新
        self.page.on_interval = self._update_system_info
        self.page.update_interval = 2000  # 2秒更新一次

    def _build_view(self):
        return ft.Container(
            content=ft.Column([
                # 顶部标题
                ft.Container(
                    content=ft.Row([
                        ft.Text("系统监控", size=30, weight=ft.FontWeight.BOLD),
                        ft.IconButton(
                            icon=ft.icons.REFRESH,
                            tooltip="刷新",
                            on_click=lambda _: self._update_system_info(),
                        ),
                    ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    margin=ft.margin.only(bottom=20)
                ),
                
                # 系统状态卡片
                ft.Row([
                    self._build_stat_card("CPU使用率", "0%", ft.icons.MEMORY, ft.colors.BLUE),
                    self._build_stat_card("内存使用率", "0%", ft.icons.STORAGE, ft.colors.GREEN),
                    self._build_stat_card("磁盘使用率", "0%", ft.icons.DISC_FULL, ft.colors.ORANGE),
                    self._build_stat_card("进程数", "0", ft.icons.APPS, ft.colors.PURPLE),
                ], spacing=20),

                # 系统信息和性能监控
                ft.Row([
                    # 系统信息
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text("系统信息", size=20, weight=ft.FontWeight.BOLD),
                                ft.Divider(),
                                ft.Text(f"操作系统: {platform.platform()}", size=14),
                                ft.Text(f"处理器: {platform.processor()}", size=14),
                                ft.Text(f"Python版本: {platform.python_version()}", size=14),
                                ft.Text(f"机器架构: {platform.machine()}", size=14),
                            ], spacing=10),
                            padding=20,
                            width=400,
                        ),
                    ),
                    # 性能监控
                    ft.Card(
                        content=ft.Container(
                            content=ft.Column([
                                ft.Text("性能监控", size=20, weight=ft.FontWeight.BOLD),
                                ft.Divider(),
                                self.performance_text,
                                self.network_text,
                                self.battery_text,
                                self.boot_text,
                            ], spacing=10),
                            padding=20,
                            width=400,
                        ),
                    ),
                ], spacing=20, alignment=ft.MainAxisAlignment.CENTER),

                # 最近活动列表
                ft.Container(
                    content=ft.Column([
                        ft.Text("系统日志", size=20, weight=ft.FontWeight.BOLD),
                        ft.ListView(
                            controls=[
                                self._build_activity_item(
                                    "系统启动",
                                    f"系统于 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 启动",
                                    "刚刚"
                                ),
                                self._build_activity_item(
                                    "监控启动",
                                    "系统监控服务已启动",
                                    "刚刚"
                                ),
                            ],
                            spacing=10,
                            height=200,
                        )
                    ]),
                    margin=ft.margin.only(top=20)
                ),
            ]),
            padding=20
        )

    def _build_stat_card(self, title: str, value: str, icon: str, color: str):
        """构建统计卡片"""
        return ft.Card(
            content=ft.Container(
                content=ft.Column([
                    ft.Icon(icon, size=30, color=color),
                    ft.Text(value, size=24, weight=ft.FontWeight.BOLD, color=color),
                    ft.Text(title, size=14, color=ft.colors.GREY),
                ], spacing=10, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                width=180,
                padding=15,
            )
        )

    def _build_activity_item(self, title: str, desc: str, time: str):
        """构建活动列表项"""
        return ft.ListTile(
            leading=ft.CircleAvatar(
                content=ft.Icon(ft.icons.ACCESS_TIME),
                bgcolor=ft.colors.BLUE_100,
            ),
            title=ft.Text(title),
            subtitle=ft.Text(desc),
            trailing=ft.Text(time, size=12, color=ft.colors.GREY),
        )

    def _update_system_info(self):
        """更新系统信息"""
        try:
            # 更新卡片数据
            cards = self.view.content.controls[1].controls
            
            # CPU使用率
            cpu_percent = psutil.cpu_percent()
            cards[0].content.content.controls[1].value = f"{cpu_percent}%"
            
            # 内存使用率
            memory = psutil.virtual_memory()
            cards[1].content.content.controls[1].value = f"{memory.percent}%"
            
            # 磁盘使用率
            disk = psutil.disk_usage('/')
            cards[2].content.content.controls[1].value = f"{disk.percent}%"
            
            # 进程数
            process_count = len(psutil.pids())
            cards[3].content.content.controls[1].value = str(process_count)

            # 更新性能监控
            performance_info = []
            
            # CPU详细信息
            cpu_freq = psutil.cpu_freq()
            if cpu_freq:
                performance_info.append(
                    f"CPU频率: {cpu_freq.current:.1f}MHz"
                )
            
            # 内存详细信息
            memory_info = psutil.virtual_memory()
            performance_info.append(
                f"内存使用: {memory_info.used/1024/1024/1024:.1f}GB/"
                f"{memory_info.total/1024/1024/1024:.1f}GB"
            )
            
            self.performance_text.value = "\n".join(performance_info)

            # 网络信息
            net_io = psutil.net_io_counters()
            self.network_text.value = (
                f"网络流量: ↑{net_io.bytes_sent/1024/1024:.1f}MB "
                f"↓{net_io.bytes_recv/1024/1024:.1f}MB"
            )

            # 电池信息
            if hasattr(psutil, "sensors_battery"):
                battery = psutil.sensors_battery()
                if battery:
                    self.battery_text.value = (
                        f"电池: {battery.percent}% "
                        f"({'充电中' if battery.power_plugged else '使用电池'})"
                    )

            # 启动时间
            boot_time = datetime.fromtimestamp(psutil.boot_time())
            self.boot_text.value = f"启动时间: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}"

            self.page.update()
        except Exception as e:
            print(f"更新系统信息失败: {e}") 