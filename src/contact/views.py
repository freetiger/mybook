# -*- coding: utf-8 -*-
'''
Created on 2014年11月10日

@author: heyuxing
'''

from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from contact.forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact_form.html', {'form': form})


from django.views.generic.edit import FormView
class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # 当有效的数据被 POST 进来以后，本方法就会被调用
        # 本方法应当返回一个 HttpResponse.
        form.send_email()
        return super(ContactView, self).form_valid(form)
