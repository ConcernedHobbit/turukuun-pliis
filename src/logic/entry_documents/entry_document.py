class EntryDocument:
    def __init__(self,
                 name: str,
                 valid: bool = True,
                 reason_not_valid: str = None):
        self.name = name
        self.valid = valid
        self.reason_not_valid = reason_not_valid
