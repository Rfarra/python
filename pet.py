class Pet:
    def __init__(self, kind, breed, name):
        self.__kind = kind
        self.__breed = breed
        self.__name = name

    def get_kind(self):
        return self.__kind

    def set_kind(self, kind):
        self.__kind = kind

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        self.__breed = breed

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

   



