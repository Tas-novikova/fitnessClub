from django import forms

from django.core.exceptions import ValidationError
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from .models import Lessons
from django.forms import ModelForm, TextInput, Textarea, Select, RadioSelect
import re


class LessonsForm(ModelForm):
    class Meta:
        model = Lessons
        phone = forms.IntegerField(min_value=9, max_value=10)
        fields = ['name', 'phone', 'days', 'textMessage']


        # def clean_phone(self):
        #     new_phone = self.phone
        #
        #     if not new_phone.isdigit():
        #         return 'Введите только цифры'
        #         #raise ValidationError(_('Введите только цифры'))
        #
        #     elif new_phone != r'\d{9}':
        #         return 'Номер должен состоять из 9 цифр.'
        #         #raise ValidationError(_('Номер должен состоять из 9 цифр.'))
        #
        #     else:
        #         return 'OK'


        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш телефон (29xxxxxxx)'
            }),
            "days": Select(attrs={
                'class': 'form-control'
            }),
            "textMessage": Textarea(attrs={
                'class': 'form-control',
                'rows': '3',
                'placeholder': 'Текст сообщения',
                'required': False
            }),
        }


