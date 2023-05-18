from django.shortcuts import render, HttpResponse

from src.settings import BASE_DIR
from .models import Category, News, Contact, Comments, View
import requests as re

# Create your views here.
from .services import get_all_ctg, search_new


def valyuta():
    url = 'https://cbu.uz/oz/arkhiv-kursov-valyut/json/'

    data = {

    }

    headers = {

    }
    response = re.get(url, headers=headers, data=data)
    return response.json()


def ctgs():
    return get_all_ctg()


def index(requests, pk=None):
    news = News.objects.all().order_by('-date')

    dtrlash_ctg = Category.objects.get(name="Dasturlash")
    dtl_news = News.objects.filter(ctg=dtrlash_ctg)

    # mahall_ctg = Category.get
    # mahal_news = News.filter(mahl=mahall_ctg)

    actnews = News.objects.all().order_by('-view')

    ctx = {
        "ctgs": ctgs(),
        'big': news[0],
        "actnews": actnews[0:3],
        'pop_news': news[4:8],
        'dasturlash': dtrlash_ctg,
        'news': news,
        'das_news': dtl_news,
        'val': valyuta()
    }
    return render(requests, 'index.html', ctx)


def ctg(requests, _id):
    try:
        ctg = Category.objects.get(id=_id)
    except:
        ctx = {
            'val': valyuta(),
            "error": True,
            "ctgs": ctgs()
        }
        return render(requests, 'category.html', ctx)

    ctg_news = News.objects.filter(ctg=ctg).order_by('-id')

    ctx = {
        'val': valyuta(),
        "ctgs": ctgs(),
        'ctg': ctg,
        "ctg_news": ctg_news[1:],
    }
    if len(ctg_news) > 0:
        ctx['big'] = ctg_news[0]

    return render(requests, 'category.html', ctx)


def cnt(requests):
    ctx = {"ctgs": ctgs(),
           'val': valyuta()}
    if requests.POST:
        ism, sms, tel = requests.POST.get('ism'), requests.POST.get('sms'), requests.POST.get('tel')
        contact = Contact.objects.create(ism=ism, phone=tel, message=sms)
        ctx['contact'] = contact

    return render(requests, 'contact.html', ctx)


def srch(requests):
    savol = requests.GET.get('s', None)
    news = search_new(savol)

    ctx = {
        "news": news,
        "len": len(news),
        "savol": savol,
        'val': valyuta(),
        "ctgs": ctgs()
    }
    return render(requests, 'search.html', ctx)


def view(requests, pk):
    new = News.objects.filter(id=pk).first()

    if not requests.user.is_anonymous:
        View.objects.get_or_create(user=requests.user, new=new)

    if not new:
        return render(requests, 'view.html', {
            "ctgs": ctgs(),
            "error": True,
            'val': valyuta()
        })
    new.view = new.view + 1
    new.save()

    if requests.POST:
        user = requests.user
        izoh = requests.POST.get('comment')

        # cmt = Comments()
        # cmt.user = user
        # cmt.comment = izoh
        # cmt.new = new
        # cmt.save()

        cmt = Comments.objects.create(user=user, comment=izoh, new=new)

    comments = Comments.objects.filter(new=new, trash=False).order_by('-pk')

    ctx = {
        "ctgs": ctgs(),
        "new": new,
        'val': valyuta(),
        "comments": comments[:25],
        "len_comment": len(comments)
    }
    return render(requests, 'view.html', ctx)

# def alljson(requests):
#     file = open('./all.json', 'rb')
#     js = file.read()
#     file.close()
#
#     return HttpResponse(js)
