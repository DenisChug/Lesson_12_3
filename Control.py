def control_of_execution(method):
    """Декоратор для выполнения или пропуска теста"""

    def wrapper(self, *args, **kwargs):
        if not self.is_frozen:
            return method(self, *args, **kwargs)
        else:
            self.skipTest("Тесты в этом кейсе заморожены")

    return wrapper