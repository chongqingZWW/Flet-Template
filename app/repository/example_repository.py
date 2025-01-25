from sqlalchemy.orm import Session
from app.db.models import ExampleModel

class ExampleRepository:
    """
    示例仓储类
    演示基本的数据库操作封装
    """
    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        """获取所有记录"""
        try:
            items = self.session.query(ExampleModel).all()
            return [self._to_dict(item) for item in items]
        except Exception as e:
            print(f"查询失败: {e}")
            return []

    def get_by_id(self, id: int):
        """根据ID获取记录"""
        try:
            item = self.session.query(ExampleModel).filter_by(id=id).first()
            return self._to_dict(item) if item else None
        except Exception as e:
            print(f"查询失败: {e}")
            return None

    def _to_dict(self, model: ExampleModel):
        """模型转字典"""
        return {
            "id": model.id,
            "name": model.name,
            "description": model.description,
            "settings": model.settings,
            "created_at": model.created_at,
            "updated_at": model.updated_at
        } 