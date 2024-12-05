from django.forms import Form, CharField, Textarea, DateField, DateInput


class CreatePost(Form):
    title = CharField(max_length=100)
    content = CharField(widget=Textarea())

class EditPost(Form):
    title = CharField(max_length=100)
    content = CharField(widget=Textarea())

class AddComment(Form):
    author = CharField(max_length=50)
    text = CharField(widget=Textarea())

class EditComment(Form):
    author = CharField(max_length=50)
    text = CharField(widget=Textarea())
