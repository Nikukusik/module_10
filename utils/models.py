from mongoengine import *


class Author1(Document):
    _id = ObjectIdField()
    fullname = StringField(max_length=100)
    born_date = StringField(max_length=100)
    born_location = StringField(max_length=100)
    description = StringField(max_length=10000)
class Quote1(Document):
    tags = ListField()
    author = ReferenceField(Author)
    quote = StringField(max_length=10000)