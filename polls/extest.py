#coding:utf-8
'''
Created on 2015年12月22日

@author: zengchunyun
'''
import datetime
from django.utils import timezone
from polls.models import Question
import django
django.setup()


future_question = Question(pub_date=timezone.now()+datetime.timedelta(days=30))
print future_question
print future_question.was_published_recently()


from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client =Client()
response = client.get('/')

response.status_code
