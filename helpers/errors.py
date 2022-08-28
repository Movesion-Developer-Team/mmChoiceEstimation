class TextLengthExceededError(Exception):
    def __init__(self, length, message = f"Text size is exceeded available limit of 500 characters."):
        self.length = length
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f"{self.message} Actual size is {self.length}"