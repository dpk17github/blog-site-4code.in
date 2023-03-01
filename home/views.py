from email import message
import http
from django.shortcuts import render,HttpResponse,redirect
from home.models import Contactus,profile
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.

# home
def home(request):
    popularpost = Post.objects.all()
    list = []
    for i in popularpost:
        list.append(i.views)
    w = sorted(list)
    x = w[:-6:-1]
    p =[]
    d ={}
    for h in x:
        for j in popularpost:
            if j.views == h: 
                p.append(j)
                if j.views in d.keys():
                    d[j.views + 1] = j
                else:
                    d[j.views] = j
    z =sorted(d.keys())[::-1]
    f = []
    for o in z:
        f.append(d[o])
    context = {'popularpost':f}
    return render(request,'home/home.html',context)

# about
def about(request):
    return render(request,'home/about.html')

# contactus-->
def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['help']
        if len(name)<3:
            messages.error(request,'faild! name is too short...')
        elif len(email)<8:
            messages.error(request,'faild! please give a valid email...')
        elif len(phone)<10:
            messages.error(request,'faild! please give a valid phone no.')
        elif len(content)<5:
            messages.error(request,'faild! content is too short...')
        else:
            contact = Contactus(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"We got your message successfully.. we'll reply soon")
    return render(request,'home/contactus.html')

# handle signup--->
def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username)<3:
            messages.error(request,'Signup faild! username is too short...')
        elif len(fname)<3:
            messages.error(request,'Signup faild! firstname is too short...')
        elif len(lname)<3:
            messages.error(request,'Signup faild! lastname is too short...')
        elif len(email)<8:
            messages.error(request,'Signup faild! please give valied email address.')
        elif len(pass1)<8:
            messages.error(request,'Signup faild! password shoud be more than 8 characters..')
        elif pass1 != pass2:
            messages.error(request,'Signup faild! password not same..')
        else:
            myuser = User.objects.create_user(username=username,email=email,password=pass2)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.save()
            messages.success(request,'Your 4code account has been created successfully')    
        return redirect('home')

    return HttpResponse('404 page not fond')

# handle login
def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['loginusername']        
        password = request.POST['loginpass']

        user = authenticate(username=username, password=password) 
        if user is not None:
            login(request,user)
            messages.success(request,f'Hey {user.first_name.upper()} {user.last_name.upper()} welcome to 4code')
            return redirect('home')
        else:
            messages.error(request,f'login failed!! invalid user {username.upper()} please try again..')
            return redirect('home')
    return HttpResponse('error 404 page not found')

# handle logout
def handlelogout(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request,'successfully logout')
        return redirect('home')
    return HttpResponse('error 404 page not found')
# handle search-->
def search(request):
    query = request.GET['query']
    if len(query)>50:
        allpost = Post.objects.none()
    else:
        title = Post.objects.filter(title__icontains = query)
        text = Post.objects.filter(text__icontains = query)
        allpost = title.union(text)
    if allpost.count() == 0:
        messages.warning(request,'No results found! try again')
    context = {'allpost': allpost, 'query': query}
    return render(request,'home/search.html',context)


def myprofile(request):
    pro = profile.objects.filter(Username=request.user)
    context = {'profile': pro}
    return render(request,'home/myprofile.html',context)