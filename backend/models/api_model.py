class ApiHostModel:
    def __init__(self, host: str):
        self.__HOST: str = host

    def __str__(self):
        return self.__HOST

    def __join__(self, item: str):
        path = "/".join([self.__HOST, item])
        return ApiHostModel(path)

    def __truediv__(self, other):
        return self.__join__(other)

    def __add__(self, other):
        return ApiHostModel(host=self.__HOST + other)
