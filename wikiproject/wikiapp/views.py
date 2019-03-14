from django.shortcuts import render, get_object_or_404, redirect
from .models import RelatedModel, PostModel
from .forms import postForm, relatedForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'wikiapp/index.html')


# ADD A WIKI
def createwiki(request):
    form = postForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        image_info = ''
        if request.FILES:
            image_info = request.FILES['image']

        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        PostModel.objects.create(title=request.POST['title'], text=request.POST['text'], image=image_info)

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
    # print(wiki)
    # print(wiki.text)
    form = postForm(request.POST or None, instance=wiki)
    # print(form)
    # print(ID)
    if form.is_valid():
        print(wiki)
        wiki.save()
        return redirect('allwiki')

    return render(request, 'wikiapp/editwiki.html', {'form': form})


def deletewiki(request, ID):
    wiki = get_object_or_404(PostModel, pk=ID)
    form = postForm(request.POST or None, instance=wiki)
    print(ID)
    if form.is_valid():
        wiki.delete()
        return redirect('allwiki')

    return render(request, 'wikiapp/deletewiki.html')


def createrelated(request, postID):
    wiki = get_object_or_404(PostModel, pk=postID)
    form = relatedForm(request.POST or None)
    context = {
        'form': form,
        'wiki': wiki
    }

    if form.is_valid():
        image_info = ''
        if request.FILES:
            image_info = request.FILES['image']

        RelatedModel.objects.create(title=request.POST['title'], text=request.POST['text'],
                                    image=image_info, post=wiki)
        return redirect('allwiki')
    return render(request, 'wikiapp/createrelated.html', context)


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
    user = User.objects.create_user(username = request.)
    return render(request, 'wikiapp/newUser.html')


@login_required
def userEntries(request):
    posts = PostModel.Objects.filter(usertableforeignkey=request.user)

    return render(request, 'wikiapp/userEntries.html', {'posts': posts})
