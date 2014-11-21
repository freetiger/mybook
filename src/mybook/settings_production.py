# -*- coding: utf-8 -*-

from settings import *

print "helllllllllllllllllllll"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []

#第二，确保你的服务器配置为发送电子邮件。 设置好postfix,sendmail或其他本书范围之外但是与Django设置相关的邮件服务器,
#你需要将将 EMAIL_HOST设置为你的邮件服务器的正确的主机名.
#Django在你的代码引发未处理的异常时，将会发送一封Email至开发者团队。
ADMINS = (
    ('John Lennon', 'jlennon@example.com'),
    ('Paul McCartney', 'pmacca@example.com'),
)

