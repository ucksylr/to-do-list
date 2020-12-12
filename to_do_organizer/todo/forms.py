from django import  forms

class TodoForm(forms.Form):
    name = forms.CharField(max_length=64)
    description = forms.CharField(max_length=256)
    deadline = forms.DateTimeField()
    status = forms.BooleanField()