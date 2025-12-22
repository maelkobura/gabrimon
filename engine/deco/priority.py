def priority(order):
    def decorator(cls):
        cls.priority = order
        return cls
    return decorator
