from django import forms
from .models import Updates as UpdateModel

class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = [
            'user',
            "content",
        ]
    def clean(self,*args,**kwargs):
        data  =self.cleaned_data
        content = data.get('content',None)
        if content == "":
            content = None

        if content is None :
            raise forms.ValidationError('content is required')
        return super().clean(*args,**kwargs)
    