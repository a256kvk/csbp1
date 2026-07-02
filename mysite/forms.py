from django import forms

from .models import PostModel

class CreateForm(forms.Form):
    content = forms.CharField(label="contents", max_length=100)
    def save(self,user):
        PostModel.objects.create(account=user,content=self.cleaned_data["content"])
