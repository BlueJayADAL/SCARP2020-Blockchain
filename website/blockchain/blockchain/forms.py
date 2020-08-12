from django import forms
from .models import Display_File, Request_File


class Display_Form(forms.ModelForm):
    class Meta:
        model = Display_File
        fields = [
            'file_name',
            'email',
            'display_file'
        ]


class Request_Form(forms.ModelForm):
    class Meta:
        model = Request_File
        fields = [
            'file_name',
            'email',
            'status',
        ]