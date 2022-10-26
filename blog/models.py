from django.db.models import Model, CharField, TextField

class Post(Model):
    title = CharField(max_length=255)
    blog = TextField()
    creator = CharField(max_length=40)



# Create your models here.
