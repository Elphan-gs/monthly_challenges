from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

from django.template.loader import render_to_string

month_dictionary = {
    'january': "Focus on being productive instead of busy.",
    'february': "Do the hard jobs first. The easy jobs will take care of themselves.",
    'march': "Productivity is being able to do things that you were never able to do before.",
    'april': "It's not always that we need to do more but rather that we need to focus on less.",
    'may': "My goal is no longer to get more done, but rather to have less to do.",
    'june': "You can fool everyone else, but you can't fool your own mind.",
    'july': "You miss 100% of the shots you don't take.",
    'august': "Simplicity boils down to two steps: Identify the essential. Eliminate the rest.",
    'september': "Strive not to be success, but rather to be of value.",
    'october': "Sometimes, things may not go to your way, but the effort should be there every single night.",
    'november': "The way to get started is to quit talking and begin doing.",
    'december': None
    # 'december': "If you spend to much time thinking about a thing, you'll never get it done."
}


# Create your views here.
def index(request):
    months = list(month_dictionary.keys())

    return render(request, 'challenges/index.html', {
        'head_title': "All Challenges",
        'months': months
    })


def monthly_challenges(request, month):
    try:
        month_quote = month_dictionary[month]
        response_data = f"<h1>{month_quote}</h1>"
    except:
        print("Invalid Month")
    else:
        return render(request, 'challenges/challenge.html', {
            'head_title': "Monthly Challenges",
            'month': month,
            'quote': month_quote
        })


def monthly_challenges_number(request, month):
    if month >= 1 and month <= 12:
        month = (list(month_dictionary.keys()))[month - 1]
        return HttpResponseRedirect(reverse("challenges:monthly_challenges", args=[month]))
    else:
        return render(request, '404.html', {
            'head_nav': "There something went wrong",
            'message': "Page not Found",
            'description': "Sorry, we could not process your request. It looks like you have entered an invalid month."
        })
