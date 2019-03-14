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
        PostModel.objects.create(title=request.POST['title'], text=request.POST['text'], image=request.FILES['image'])

        return redirect('allwiki')

    return render(request, 'wikiapp/createwiki.html', context)


def readwiki(request, ID):
    wiki = get_object_or_404(PostModel, pk=ID)
    print(ID)
    context = {
        'wiki': wiki
    }
    return render(request, 'wikiapp/readwiki.html', context)


def editwiki(request, ID):
    wiki = get_object_or_404(PostModel, pk=ID)
    print(wiki)
    print(wiki.text)
    form = postForm(instance=wiki)
    print(form)
    print(ID)
    if request.POST == "POST" and form.is_valid():
        form.save()


    return render(request, 'wikiapp/editwiki.html', {'form': form})


def deletewiki(request, ID):
    wiki = get_object_or_404(PostModel, pk=ID)
    form = postForm(instance=wiki)
    print(ID)
    if request.POST == "POST" and form.is_valid():
        form.delete()
        return redirect('allwiki')

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
