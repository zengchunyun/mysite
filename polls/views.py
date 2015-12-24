#!/usr/bin/env python
#coding:utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext,loader
from .models import Question,Choice
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
# from django.http import Http404

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
                pub_date__lte=timezone.now()
                ).order_by('-pub_date')[:5]
#         return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self): 
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
    
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/result.html'
        

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] 
#     context = {'latest_question_list':latest_question_list}
#     return render(request, 'polls/index.html', context,)
#     output = ', '.join([p.question_text for p in latest_question_list]) 
#     template = loader.get_template('polls/index.html',)
#     context = RequestContext(request,{
#             'latest_question_list':latest_question_list,
#             })
#     return HttpResponse(template.render(context))
#     return HttpResponse(output)
#     return HttpResponse("Hello,world.You're at the polls index.")

# def detail(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/detail.html', {'question':question},)
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question':question},)
#     return HttpResponse("You're looking at question %s."%question_id)

# def results(request,question_id):
#     question = get_object_or_404(Question,pk=question_id)
#     return render(request, 'polls/result.html',{'question':question})
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response %question_id)

def vote(request,question_id):
    p = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
        print selected_choice
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {'question':p,'error_message':"You didn't select a choice."})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results',args=(p.id,)))
#     return HttpResponse("You're voting on question %s."%question_id)






# import django
# django.setup()
# 
# # Create your views here.
# from polls.models import Question,Choice
# 
# print Question.objects.all()
# print Question.objects.filter(id=1)
# print Question.objects.filter(question_text__startswith='What')
# from django.utils import timezone
# current_year = timezone.now().year
# print Question.objects.get(pub_date__year=current_year)
# print Question.objects.get(pk=1)
# q = Question.objects.get(pk=1)
# print q.was_published_recently()
# q = Question.objects.get(pk=1)
# print q.choice_set.all()
# print q.choice_set.create(choice_text='Not much', votes=0)
# print q.choice_set.create(choice_text='The sky', votes=0)
# c = q.choice_set.create(choice_text='Just hacking again', votes=0)
# print c.question
# print q.choice_set.all()
# print q.choice_set.count()
# Choice.objects.filter(question__pub_date__year=current_year)
# c = q.choice_set.filter(choice_text__startswith='Just hacking')
# c.delete()