from django  import forms
from .models import reply

class ReplyForm (forms.ModelForm):
    class Meta:
        model  = reply
        fields = ['reply']
