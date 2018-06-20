from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from models import Question
from forms import AskForm, AnswerForm, RegisterForm


@require_http_methods(['GET', 'POST'])
# @login_required(login_url='/login')
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            q = form.save()
            return HttpResponseRedirect('/question/%d' % q.id)

    else:
        form = AskForm()

    return render(request, 'qa/ask.html', {'form': form})


@require_POST
# @login_required(login_url='/login')
def answer(request):
    form = AnswerForm(request.POST)
    form._user = request.user
    if form.is_valid():
        q_id = form.cleaned_data['question']
        form.save()
        return HttpResponseRedirect('/question/%d' % q_id)


@require_GET
def home(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.all(), limit)
    questions = paginator.page(page)
    context = {'questions': questions}
    return render(request, 'qa/index.html', context)


@require_GET
def popular(request):
    try:
        limit = int(request.GET.get('limit', 10))
    except:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    paginator = Paginator(Question.objects.order_by('-rating'), limit)
    questions = paginator.page(page)
    context = {'questions': questions}
    return render(request, 'qa/popular.html', context)


def q_id(request, q_id):
    question = get_object_or_404(Question, id=q_id)
    form = AnswerForm(initial={'question': q_id})
    context = {'question': question,
               'form': form}
    return render(request, 'qa/q_detail.html', context)


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return HttpResponseRedirect('/')

    else:
        form = RegisterForm()

    return render(request, 'qa/signup.html', {'form': form})
