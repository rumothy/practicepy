def greet():
    return "hello"


class ClassInModule:
    property1 = 1
    
    def __init__(self, prop1):
        self.property1 = prop1

    @classmethod
    def StaticFunc(self):
        return "StaticFunc"

