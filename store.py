def init_store():  # 初始化
    global _global_dict
    _global_dict = {}


def set_store(key, value):
    """ 定义一个全局变量 """
    _global_dict[key] = value


def get_store(key, default=None):
    """
    获得全局变量,不存在则返回默认值
    """
    try:
        return _global_dict.get(key, default)
    except:
        init_store()
