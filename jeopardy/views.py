from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from .models import Clue, Category


def index(request, round_name):
    round_dict={'jeopardy':0,'doublejeopardy':1,'finaljeopardy':2}
    category_list = Category.objects.filter(game=3, round=round_dict[round_name])
    clue_list = Clue.objects.filter(game=3)
    round_name = ' J'.join(round_name.split("j")) + ' Round'
    round_name = round_name.title()
    context = {'clue_list': clue_list, 'category_list': category_list, 'round_name': round_name}
    return render(request, 'jeopardy/index.html', context)

def detail(request, clue_id):
    clue = get_object_or_404(Clue, pk=clue_id)
    return render(request, 'jeopardy/detail.html', {'clue': clue})

def result(request, clue_id):
    return HttpResponse(response % question_id)

def answer(request, clue_id):
    return HttpResponse("You're trying to answer clue %s." % clue_id)
