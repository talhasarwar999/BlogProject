from django import forms
from requests import post

from blog.models import BlogComment
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment']
class EmployeeForm1(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comment']