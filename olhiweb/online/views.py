from django.shortcuts import render
from django.core.paginator import Paginator
from online.models import ShowEndAlive

# Create your views here.
def online(request):
    page = int(request.GET.get('page',1))
    pe = 4
    pf = 5
    pview = pe+pf+1
    onlinelist = ShowEndAlive.objects.all()
    try:
        p = Paginator(onlinelist,10)
        if page <= 0:
            page = 1
        if page > p.num_pages:
            page = p.num_pages
        pagelist=[]
        pagelist = p.page(page).object_list
    except:
        print("p",p)
        print("pagelist",pagelist)
    if page > pf:
        page_range=p.page_range[page-pf-1:page+pe]
    else:
        page_range=p.page_range[0:pview]
    print('page_range',page_range)
    print('numberpages',p.num_pages)
    return render(request,"online/onlinelist.html",locals())