from django.forms import ModelForm
from .models import Files


class UploadFileForm(ModelForm):
    class Meta:
        model = Files
        fields = ['title', 'uploadfile']
