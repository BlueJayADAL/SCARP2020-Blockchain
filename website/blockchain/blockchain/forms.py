from django import forms
from .models import Display_File

#DataFlair #File_Upload


class Display_Form(forms.ModelForm):
    class Meta:
        model = Display_File
        fields = [
            'file_name',
            'email',
            'display_file'
        ]