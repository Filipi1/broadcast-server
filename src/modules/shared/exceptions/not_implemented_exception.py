class NotImplementedException(NotImplementedError):
    def __init__(self, func_name: str):
        super().__init__(f"Function '{func_name}' is not implemented.")