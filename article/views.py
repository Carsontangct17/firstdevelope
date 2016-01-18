#-*-coding:utf-8-*-

# 导入APP所需要的模块
from django.shortcuts import render_to_response,HttpResponse,HttpResponseRedirect
from models import fz_Article,fz_classic,fz_comment,Contacts
from django.core.context_processors import csrf
from django.contrib import auth
from django.template import loader,Context,RequestContext
# from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

#想要读取文章，需要用户先登入
@login_required(login_url='/loginpage/')
def readarticle(request):
    title = fz_Article.objects.get(id=2).title
    publish_date = fz_Article.objects.get(id=2).publish_date
    content = fz_Article.objects.get(id=2).content
    return render_to_response('article.html',{'title':title,'publish_date':publish_date,'content':content})
# page使用方法
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def listing(request):
    contact_list = fz_Article.objects.all()
    paginator = Paginator(contact_list, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page).object_list
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'list.html', {'contacts': contacts})


# @csrf_protect
def loginpage(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # c = {}
        # c.update(csrf(request))
        # Redirect to a success page.
        # return HttpResponseRedirect("/loginpage/")
        t = loader.get_template('loginpage.html')
        c = Context({'username':username})
        return HttpResponse( t.render(c) )
        # return render_to_response("loginpage.html",{'username':username},context_instance=RequestContext(request))
        # return render_to_response("loginpage.html",c)
    else:
        # Show an error page
        return HttpResponseRedirect('/registration/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")
def registration(request):
    return render_to_response("registration.html")
def signup(request):
    from django.contrib.auth.models import User
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    useremail = request.POST.get('useremail','')
    user = User.objects.create_user(username=username,email=useremail,password=password)
    user.is_staff = True
    user.save()
    return HttpResponseRedirect('/')
def index(request):
    title = fz_Article.objects.get(id=2).title
    content = fz_Article.objects.get(id=2).content
    return render_to_response('index.html',{'title1':title,'title2':title,'title3':title,'mypragraph1':content,'mypragraph2':content,'mypragraph3':content})


