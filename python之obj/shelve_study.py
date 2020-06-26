import shelve
from contextlib import closing
import datetime


# with closing(shelve.open('./data/blog')) as shelf:
#     shelf['wocao'] = 'hahaha'


class Blog:
    def __init__(self, title, *posts):
        self.title = title

    def as_dict(self):
        return dict(
            title=self.title,
            underline="=" * len(self.title)
        )



class Post:
    def __init__(self, date, title, rst_txt, tags):
        self.date = date
        self.title = title
        self.rst_txt = rst_txt
        self.tags = tags

    def as_dict(self):
        return dict(
            date=str(self.date),
            title=self.title,
            rst_txt=self.rst_txt,
            tag_text=" ".join(self.tags)
        )


# b1 = Blog(title='Travel Blog')
# shelf = shelve.open('./data/blog')
# b1._id = 'Blog:1'
# shelf[b1._id] = b1


p2 = Post(date=datetime.datetime(2013, 11, 14, 17, 25),
          title="Hard Aground",
          rst_txt="""Some embarrassing revelation....""",
          tags=("#RedRanger", "#Whitby42", "#ICW")
          )

p3 = Post(date=datetime.datetime(2013, 11, 18, 17, 25),
          title="Anchor Follies",
          rst_txt="""Some witty revelation....""",
          tags=("#RedRanger", "#Whitby42", "#Mistakes")
          )


b1 = Blog(title='Travel Blog')
shelf = shelve.open('./data/blog')
owner = shelf['Blog:1']
p2._parent = owner._id
p2._id = p2._parent + ":Post:2"
shelf[p2._id] = p2

p3._parent = owner._id
p3._id = p3._parent + ":Post:3"
shelf[p3._id] = p3

print(list(shelf.keys()))



class BlogFactory:
    @staticmethod
    def version(self, version):
        self.version = version

    @staticmethod
    def blog(self, *args, **kw):
        if self.version == 1:
            return Blog(*args, **kw)


blog = BlogFactory.version(2).blog(title='this', other_attribute='that')
