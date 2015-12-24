#/usr/bin/env python
#encoding:utf-8
from django.shortcuts import render
from .models import Article
def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year) 
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)



# Create your views here.
# from news.models import Reporter,Article
# from datetime import date
# import django
# django.setup()
# print Reporter.objects.all()
# 
# r = Reporter(full_name='John Smith')
# r.save()   
# print r.id
# print Reporter.objects.all()
# 
# print r.full_name
# 
# # print Reporter.objects.get(id=1)
# print Reporter.objects.get(full_name__startswith='zcy')  #只取一条匹配字段内容
# print Reporter.objects.get(full_name__contains='zcy')  #get只匹配一条数据，如果多余一条，则会报错
# 
# print Reporter.objects.get(id=1)

# r = Reporter(full_name='John Smith')
# a = Article(pub_date=date.today(), headline='Django is cool',content='Yeah.', reporter=r)
# a.save()
# print Article.objects.all()
# r = a.reporter
# print r
# print r.full_name

# print r.article_set.all()
# print Article.objects.filter(reporter__full_name__startswith='John')
# r.full_name = 'Bill Goat'
# r.save()
# r.delete()