# -*- coding: utf-8 -*-
'''
Created on 2014年11月10日

@author: heyuxing
'''
from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False, label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)

    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
    
    def send_email(self):
        # 使用 self.cleaned_data 字典来发送一封邮件
        pass
    
