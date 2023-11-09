from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
import smtplib
import os
from email.mime.text import MIMEText

def send_email(message):
    sender = 'prosto.isovkusom29@yandex.ru'
    password = 'Jrs777666'
    server = smtplib.SMTP("smtp.yandex.ru", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = sender
        msg['To'] = sender
        msg['Subject'] = "Обращение"

        server.sendmail(sender, sender, msg.as_string())
    except Exception as _ex:
        return f"{_ex}\nCheck ur login or pass"
    
def send_email_confirm(subject, message, email):
    sender = 'prosto.isovkusom29@yandex.ru'
    password = 'Jrs777666'
    server = smtplib.SMTP("smtp.yandex.ru", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = sender
        msg['To'] = email
        msg['Subject'] = subject

        server.sendmail(sender, email, msg.as_string())
    except Exception as _ex:
        return f"{_ex}\nCheck ur login or pass"
    

def site(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']

        print(email)
        message = f"Имя: {name}\nТелефон: {phone}\nПочта: {email}"
        send_email(message) 

        confirmation_subject = "Обращение в Простор"
        confirmation_message = "Ваше обращение зарегистрировано, ожидайте обратного звонка"
        send_email_confirm(confirmation_subject, confirmation_message, email)

        return HttpResponseRedirect('/') 
    return render(request, 'index.html')





    
