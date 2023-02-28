from captcha.fields import CaptchaField
from django import forms
from .models import Comments

class UserCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ('is_active',)
        widgets = {'game' : forms.HiddenInput}

class GuestCommentForm(forms.ModelForm):
    captcha = CaptchaField(label = 'Введите текст с картинки',
                            error_messages = {'invalid': 'Неправильный текст'},)
    
    class Meta:
        model = Comments
        exclude = ('is_active',)
        widgets = {'game' : forms.HiddenInput}