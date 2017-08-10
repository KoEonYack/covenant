from django import forms
from .models import SellPost
from django_summernote import fields as summer_fields
from django_summernote.widgets import SummernoteWidget

class PostForm(forms.ModelForm):

    class Meta:
        model = SellPost
        fields = ['title', 'content']

        widgets = {
            'content': SummernoteWidget(),
        }

