from django.shortcuts import render
from django.core.paginator import Paginator
from qa.models import Question, Answer

from django.http import HttpResponse 
def test(request, *args, **kwargs):
    return HttpResponse('OK')
  
  # Create your views here.

def index(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    questions = Question.objects.all().order_by('new')
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'index.html',
                   {'title': 'Latest',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,})


def popular(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    questions = Question.objects.all().order_by('popular')
    paginator = Paginator(questions, limit)
    page = paginator.page(page)
    return render(request, 'popular.html',
                  {'title': 'Popular',
                   'paginator': paginator,
                   'questions': page.object_list,
                   'page': page,})
                
def question(request, num,):
    try:
        q = Question.objects.get(id=num)
    except Question.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            _ = form.save()
            url = q.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': q.id})
    return render(request, 'qa/'question.html', context)

  
  
