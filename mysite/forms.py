from django import forms

from .models import PostsModel, PrivateNotesModel

class CreateForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(), label="contents", max_length=1000)
    def save(self,user):
        PostsModel.objects.create(account=user,content=self.cleaned_data["content"])
