import random

from django.core.mail import send_mail
from django.template.loader import render_to_string

from Userauth.models import Users


def generate_otp(length):
    return int(''.join([str(random.randint(0, 9)) for i in range(length)]))


def send_otp_mail(User):
    user = Users.objects.get(id=User.id)
    subject = 'OTP for your account'
    msg_html = render_to_string('Email_templates/otpemail.html', {'OTP': user.otp})
    msg_plain = render_to_string('Email_templates/otpemail.html', {'OTP': user.otp})
    from_email = 'agharameez1990@gmail.com'
    to_list = [user.email]
    sent_email = send_mail(subject, msg_plain, from_email, to_list,html_message=msg_html, auth_password=None)
    if sent_email == 1:
        return True
    else:
        return False