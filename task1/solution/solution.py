from functools import wraps


def strict(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Получаем аннотации типов аргументов функции
        annotations = func.__annotations__

        # Проверяем позиционные аргументы
        for i, arg in enumerate(args):
            param_name = list(annotations.keys())[i]
            expected_type = annotations[param_name]
            if not isinstance(arg, expected_type):
                raise TypeError(f"Argument '{param_name}' must be of type {expected_type}, but got {type(arg)}")

        # Проверяем именованные аргументы
        for param_name, arg in kwargs.items():
            expected_type = annotations.get(param_name)
            if expected_type and not isinstance(arg, expected_type):
                raise TypeError(f"Argument '{param_name}' must be of type {expected_type}, but got {type(arg)}")

        return func(*args, **kwargs)

    return wrapper
