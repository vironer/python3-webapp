from orm import Model, StringField, IntegerField

class user(Model):
    __table__ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()

# 定义Model