from ast import Num
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.

challenges = {"january": "january", "february": "february", "march": None}

def index(request):
  list_items = ""
  months = list(challenges.keys())

  return render(request, "challenges/index.html", {
    "months": months
  })
  for month in months:
    month_path = reverse("month-challenge", args=[month])
    list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
  response_data = f"<ul>{list_items}</ul>"
  # return HttpResponse(list_items)
  return HttpResponse(response_data)


def monthly_challenge_by_number(request, month:int):
  try: 
    month_str = list(challenges.keys())[month-1]
    # Django knows how to construct a full path to the view with name "month-challenge (see urls.py in ../challenges"
    redirect_path = reverse("month-challenge", args=[month_str]) # /challenge/january
    return HttpResponseRedirect(redirect_path)
  except IndexError:
    return HttpResponseNotFound("Response not found")


def monthly_challenge(request, month:str):
  # try:
    challenge_text = challenges[month]
    return render(request, "challenges/challenge.html", {
      "text": challenge_text,
      "month": month,
    })
    # response_data = render_to_string("challenges/challenge.html")
    return HttpResponse(response_data)
  # except:
    # return HttpResponseNotFound("Response not found")
