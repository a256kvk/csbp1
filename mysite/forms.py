from django import forms

from .models import PostsModel, PrivateNotesModel

class CreateForm(forms.Form):
    content = forms.CharField(label="contents", max_length=100)
    def save(self,user):
        PostsModel.objects.create(account=user,content=self.cleaned_data["content"])

class CreatePrivateNoteForm(forms.Form):
    content = forms.CharField(label="contents", max_length=100)
    def save(self,user):
        PostsModel.objects.create(account=user,content=self.cleaned_data["content"])
