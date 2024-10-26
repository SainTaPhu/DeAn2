# Cap2App/forms.py

from django import forms


class CSVUploadForm(forms.Form):
    file = forms.FileField(label='Chọn tệp CSV')
