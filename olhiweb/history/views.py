from django.shortcuts import render
from history.models import *
from django.core.paginator import Paginator
# Create your views here.

def testdb(request):
    push_history = ShowPushMessage.objects.all()[0:5]
    for l in push_history:
        print (l.sent_message,l.sent_url)

def history(request):
    page = int(request.GET.get('page',1))
    pe = 4
    pf = 5
    pview = pe+pf+1
    prepage = page-1
    nextpage = page+1
    historylist = ShowPushMessage.objects.all()
    p = Paginator(historylist,10)
    if page < 0:
        page = 1
    if page > p.num_pages:
        page = p.num_pages
    pagelist = p.page(page).object_list
    if page > pf:
        page_range=p.page_range[page-pf-1:page+pe]
    else:
        page_range=p.page_range[0:pview]
    return render(request,"history/historylist.html",locals())

