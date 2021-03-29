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
        phone = forms.IntegerField(min_value=9, max_value=10)  #help_text="Введите 9 цифр номера телефона в формате 29ххххххх, 33ххххххх, 25ххххххх, 44ххххххх"
        fields = ['name', 'phone', 'days', 'textMessage']


        def clean_phone(self):
            new_phone = self.phone

            if not new_phone.isdigit():
                return 'Введите только цифры'
                #raise ValidationError(_('Введите только цифры'))

            elif new_phone != r'\d{9}':
                return 'Номер должен состоять из 9 цифр.'
                #raise ValidationError(_('Номер должен состоять из 9 цифр.'))

            else:
                return 'OK'


        #day = forms.RadioSelect(choices=((1, "пн-пт утро"), (2, "пн-пт вечер"), (3, "сб-вс утро"), (4, "сб-вс день")))
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


#class ChangeLesson(forms.ModelForm):
#    class Meta:
#        model = Lessons
#        fields = ('name', 'phone', 'days', 'textMessage', 'note')

#        widgets = {
#            "textMessage": Textarea(attrs={
#               'rows': '1',
#                'required': False
#            })
#        }