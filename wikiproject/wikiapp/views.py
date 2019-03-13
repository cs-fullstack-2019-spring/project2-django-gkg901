from django.shortcuts import render, get_object_or_404, redirect
from .models import RelatedModel, PostModel
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
        PostModel.objects.create(request.POST['title'], request.POST['text'], request.FILES['image'])

        return redirect('allwiki')

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
    allposts = PostModel.objects.all()
    return render(request, 'wikiapp/allwiki.html', {'allposts': allposts})


def newUser(request):
    return render(request, 'wikiapp/newUser.html')


def userEntries(request):
    return render(request, 'wikiapp/userEntries.html')
