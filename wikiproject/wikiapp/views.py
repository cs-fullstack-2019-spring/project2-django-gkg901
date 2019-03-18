from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import RelatedModel, PostModel
from .forms import postForm, relatedForm, userForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    allposts = PostModel.objects.all()

    return render(request, 'wikiapp/index.html', {'allposts': allposts})


# ADD A WIKI
@login_required
def createwiki(request):
    user = User.objects.get(username=request.user)
    form = postForm(request.POST or None)
    context = {
        "form": form
    }

    if form.is_valid():
        image_info = ''
        if request.FILES:
            image_info = request.FILES['image']

        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        PostModel.objects.create(title=request.POST['title'], text=request.POST['text'], image=image_info,
                                 userTableForeignKey=user)

        return redirect('userEntries')

    return render(request, 'wikiapp/createwiki.html', context)


# READ WIKI
def readwiki(request, ID):
    wiki = get_object_or_404(PostModel, pk=ID)
    item = RelatedModel.objects.filter(post=wiki)

    print(ID, wiki, item)
    context = {
        'wiki': wiki,
        'item': item
    }
    return render(request, 'wikiapp/readwiki.html', context)


# EDIT WIKI
@login_required
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
        return redirect('userEntries')

    return render(request, 'wikiapp/editwiki.html', {'form': form})


# DELETE WIKI
@login_required
def deletewiki(request, ID):
    wiki = get_object_or_404(PostModel, pk=ID)
    form = postForm(request.POST or None, instance=wiki)
    print(ID)
    if form.is_valid():
        wiki.delete()
        return redirect('userEntries')

    return render(request, 'wikiapp/deletewiki.html', {'form': form})


# CREATE RELATED
@login_required
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
        return redirect('userEntries')
    return render(request, 'wikiapp/createrelated.html', context)


# READ RELATED
def readrelated(request, ID):
    item = get_object_or_404(RelatedModel, pk=ID)
    print(item)
    context = {
        'item': item
    }
    return render(request, 'wikiapp/readrelated.html', context)


# EDIT RELATED
@login_required
def editrelated(request, ID):
    item = get_object_or_404(RelatedModel, pk=ID)
    form = relatedForm(request.POST or None, instance=item)

    if form.is_valid():
        item.save()
        return redirect('userEntries')

    return render(request, 'wikiapp/editrelated.html', {'form': form})


def deleterelated(request, ID):
    item = get_object_or_404(RelatedModel, pk=ID)
    form = postForm(request.POST or None, instance=item)
    print(ID)
    if form.is_valid():
        item.delete()
        return redirect('userEntries')

    return render(request, 'wikiapp/deleterelated.html', {'form': form})


def allwiki(request):
    allposts = PostModel.objects.all()
    return render(request, 'wikiapp/allwiki.html', {'allposts': allposts})


# CREATE USER
def newUser(request):
    form = userForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        User.objects.create_user(request.POST['username'], '', request.POST['password'])
        return redirect('index')
    return render(request, 'wikiapp/newUser.html', context)


# USER SPECIFIC ENTRIES
@login_required
def userEntries(request):
    posts = PostModel.objects.filter(userTableForeignKey=request.user)

    return render(request, 'wikiapp/userEntries.html', {'posts': posts})


# search bar
def search(request):
    results = PostModel.objects.filter(Q(title__contains=request.POST['searchBar']) | Q(text__contains=request.POST['searchBar']))
    items = RelatedModel.objects.all()

    context = {
        'allposts': results,
        'items': items
    }
    return render(request, 'wikiapp/search.html', context)
