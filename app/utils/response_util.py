# 状态码常量
class ResponseCode:
    """
    统一定义 API 状态码
    """
    SUCCESS = 0  # 请求成功
    BAD_REQUEST = 400  # 客户端参数错误
    UNAUTHORIZED = 401  # 未认证
    FORBIDDEN = 403  # 权限不足
    NOT_FOUND = 404  # 资源不存在
    INTERNAL_SERVER_ERROR = 500  # 服务器内部错误


# 统一的响应方法
def api_response(code=ResponseCode.SUCCESS, message="success", data=None):
    """
    统一返回结构
    :param code: 状态码
    :param message: 返回消息
    :param data: 返回数据
    :return: dict
    """
    return {
        "code": code,  # 状态码
        "message": message,  # 消息
        "data": data  # 数据
    }
