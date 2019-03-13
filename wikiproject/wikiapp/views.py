from django.shortcuts import render
from .models import relatedModel, postModel
from .forms import postForm, relatedForm
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request, 'wikiapp/index.html')

# ADD A WIKI
def createwiki(request):
    form = postForm(request.POST or None)
    context = {
        "form": form
    }

    if request.method == "POST" and form.is_valid():
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        postModel.objects.create(request.POST['title'], request.POST['text'], request.POST['image'],
                                 request.POST['created'], request.POST['updated'])
        return render(request, 'wikiapp/createwiki.html')

    return render(request, 'wikiapp/createwiki.html', context)


def readwiki(request, ID):
    return render(request, 'wikiapp/readwiki.html')


def editwiki(request, ID):
    return render(request, 'wikiapp/editwiki.html')


def deletewiki(request, ID):
    return render(request, 'wikiapp/deletewiki.html')


def createrelated(request, postID):
    return render(request, 'wikiapp/createrelated.html')


def readrelated(request, ID):
    return render(request, 'wikiapp/readrelated.html')


def editrelated(request, ID):
    return render(request, 'wikiapp/editrelated.html')


def deleterelated(request, ID):
    return render(request, 'wikiapp/deleterelated.html')


def allwiki(request):
    return render(request, 'wikiapp/allwiki.html')


def newUser(request):
    return render(request, 'wikiapp/newUser.html')


def userEntries(request):
    return render(request, 'wikiapp/userEntries.html')
