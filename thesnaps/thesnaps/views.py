from django.shortcuts import redirect, render
from app.models import Category, Image

# HOME PAGE RENDER
def show_index_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()

    data = {'images': images , 'cats':cats}
    return render(request,"index.html" , data)

# SHOW CATEGORY
def show_category(request , cid):
    print(cid)
    cats = Category.objects.all()

    category = Category.objects.get(pk=cid)
    print(category)

    images = Image.objects.filter(cat=category)
    #! filter by date
    """ filter_date = Image.objects.all().order_by('-added_date')
    print("filter_date",filter_date) """

    data = {'images': images , 'cats':cats }

    return render(request,"index.html" , data)

# SEARCH BY TITLE
def search_by_title(request):
    if request.method == 'POST':
        title = request.POST["title"]
        filter_title = Image.objects.filter(title__icontains = title)
        print("filter_title",len(filter_title))
        print(filter_title.count())

        if title != '' and title is not None and filter_title.count() != 0:
            print("filter", filter_title)
            data = {'images_filter': filter_title ,"title":title , "count":filter_title.count()}
            return render(request, "search.html" , data)
        else:
            ERROR = "Oops, can't find this Snap! "
            return render(request, "search.html" ,  {"ERROR": ERROR})
    else:
        print("NO")
        return render(request, "search.html" ,)

#  REDIRECT TO HOME PAGE
def home(request):
    return redirect("/home")
