import flet as ft


class BaseView:
    """基础视图类，封装通用功能"""

    def __init__(self, page: ft.Page, viewmodel):
        self.page = page
        self.viewmodel = viewmodel
