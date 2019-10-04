import time


class Redis(object):
    def __init__(self):
        """使用字典存储数据"""
        self.cache = dict()

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value


class Image(object):
    """图片对象, 存储在七牛中, 只保存一个地址"""
    def __init__(self, name):
        self.name = name

    @property
    def url(self):
        time.sleep(2)
        return "http://www.baidu.com/"


class Page(object):
    """用于显示图片"""
    def __init__(self, image):
        self.image = image

    def render(self):
        """显示图片"""
        return print(self.image.url)


redis = Redis()


class ImageProxy(object):
    """图片代理模式启动, 首次会从真正图片中获取, 以后就会从缓存中获取"""
    def __init__(self, image):
        self.image = image

    @property
    def url(self):
        addr = redis.get(self.image.name)
        if not addr:
            addr = self.image.url
            print("Set url in redis cache!")
            redis.set(self.image.name, addr)
        else:
            print("Get url from redis cache!")
        return addr


if __name__ == '__main__':
    img = Image(name="logo")
    proxy = ImageProxy(img)
    page = Page(proxy)
    # 首次访问
    page.render()
    # 第二次访问
    page.render()
