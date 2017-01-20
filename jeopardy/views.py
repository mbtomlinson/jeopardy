from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Clue, Category


def index(request):
    category_list = Category.objects.filter(game=3, round=1)
    clue_list = Clue.objects.filter(game=3)
    context = {'clue_list': clue_list, 'category_list': category_list}
    return render(request, 'jeopardy/index.html', context)

def detail(request, clue_id):
    clue = get_object_or_404(Clue, pk=clue_id)
    return render(request, 'jeopardy/detail.html', {'clue': clue})

def result(request, clue_id):
    return HttpResponse(response % question_id)

def answer(request, clue_id):
    return HttpResponse("You're trying to answer clue %s." % clue_id)
