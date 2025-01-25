import flet as ft


class ThemeManager:
    """管理应用主题的类"""

    # 全局颜色变量
    WECHAT_GREEN = "#1AAD19"        # 微信绿色
    DARK_GREEN = "#0D9F13"          # 深绿色
    BLUE_PRIMARY = "#1976D2"        # 蓝色
    GREEN_PRIMARY = "#388E3C"       # 绿色
    LIGHT_BACKGROUND = "#F2F2F2"    # 浅背景
    DARK_BACKGROUND = "#1A1A1A"     # 深背景
    WHITE = "#FFFFFF"               # 白色
    BLACK = "#000000"               # 黑色
    GRAY_TEXT = "#999999"           # 浅灰文字
    DARK_GRAY_TEXT = "#333333"      # 深灰文字
    ICON_GRAY = "#B0B0B0"           # 图标灰色


    def __init__(self):
        """初始化主题管理器"""
        self.themes = {
            "light": ft.Theme(
                color_scheme=ft.ColorScheme(
                    primary=self.WECHAT_GREEN,
                    background=self.LIGHT_BACKGROUND,
                    surface=self.WHITE,
                    on_primary=self.WHITE,
                    on_background=self.DARK_GRAY_TEXT,
                    on_surface=self.BLACK,
                )
            ),
            "dark": ft.Theme(
                color_scheme=ft.ColorScheme(
                    primary=self.DARK_GREEN,
                    background=self.DARK_BACKGROUND,
                    surface="#262626",  # 深灰表面
                    on_primary=self.WHITE,
                    on_background=self.WHITE,
                    on_surface=self.GRAY_TEXT,
                )
            ),
            "blue": ft.Theme(
                color_scheme=ft.ColorScheme(
                    primary=self.BLUE_PRIMARY,
                    background="#E3F2FD",  # 浅蓝背景
                    surface=self.WHITE,
                    on_primary=self.WHITE,
                    on_background="#0D47A1",  # 深蓝文字
                    on_surface="#0D47A1",
                )
            ),
            "green": ft.Theme(
                color_scheme=ft.ColorScheme(
                    primary=self.GREEN_PRIMARY,
                    background="#E8F5E9",  # 浅绿色背景
                    surface=self.WHITE,
                    on_primary=self.WHITE,
                    on_background="#1B5E20",  # 深绿色文字
                    on_surface="#1B5E20",
                )
            ),
        }

    def get_theme(self, theme_name: str) -> ft.Theme:
        """根据主题名称获取主题"""
        return self.themes.get(theme_name, self.themes["light"])

    def apply_theme(self, page: ft.Page, theme_name: str):
        """将主题应用到页面"""
        theme = self.get_theme(theme_name)
        page.theme = theme
        page.theme_mode = (
            ft.ThemeMode.DARK if theme_name == "dark" else ft.ThemeMode.LIGHT
        )
        print(f"Applied theme: {theme_name}")
