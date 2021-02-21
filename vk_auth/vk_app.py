from enum import Enum


class VKApp(Enum):
    # subclass describes vk_auth app
    class app:
        cid = ''
        sec = ''

        def __init__(self, cid, sec):
            self.cid = cid
            self.sec = sec

    APPLE_IPHONE = app("7840623", "VeWdmyiDCtnnsfguP1nt")
    WIN = app("3427615", "AlVXZFMUqsfsfgnABp8ncuU")
    ANDROID = app("2654003", "hHbZxrkfggZ6jB1inYsH")

