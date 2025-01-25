from app.repository.example_repository import ExampleRepository

class ExampleViewModel:
    """
    示例视图模型
    演示基本的业务逻辑封装
    """
    def __init__(self, repository: ExampleRepository):
        self.repository = repository
        self.items = []  # 缓存数据
        self.selected_item = None  # 当前选中项

        # 观察者列表
        self.observers = {
            "item_selected": [],  # 选中项改变
            "items_changed": []   # 列表数据改变
        }

    def load_items(self):
        """加载所有数据"""
        self.items = self.repository.get_all()
        self._notify("items_changed", self.items)
        return self.items

    def select_item(self, item_id: int):
        """选择指定项"""
        self.selected_item = self.repository.get_by_id(item_id)
        self._notify("item_selected", self.selected_item)
        return self.selected_item

    # === 观察者模式实现 ===
    def subscribe(self, event_name: str, callback):
        """订阅事件"""
        if event_name in self.observers:
            self.observers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback):
        """取消订阅"""
        if event_name in self.observers:
            self.observers[event_name].remove(callback)

    def _notify(self, event_name: str, data):
        """通知观察者"""
        if event_name in self.observers:
            for callback in self.observers[event_name]:
                callback(data) 