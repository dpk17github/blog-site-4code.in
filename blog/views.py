from sqlite3 import Timestamp
from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post,blogComment
from home.models import profile
from django.contrib import messages
from blog.templatetags import extras
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your views here.


def bloghome(request):
    allpost = Post.objects.all()
    context ={'allpost':allpost}
    return render(request,'blog/bloghome.html',context)

def blogpost(request, slug):
    allpost = Post.objects.filter(slug=slug).first()
    allpost.views = allpost.views + 1
    allpost.save()
    comments = blogComment.objects.filter(post=allpost, parent=None)
    replies = blogComment.objects.filter(post=allpost).exclude(parent=None)
    replydict = {}
    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno] = [reply]
        else:
            replydict[reply.parent.sno].append(reply)
    tc =comments.count()
    context ={'allpost':allpost, 'comments':comments, 'tc':tc, 'replydict':replydict}
    return render(request,'blog/blogpost.html',context)

def postComment(request):
    if request.method == 'POST':
        comment = request.POST['comment']
        postsno = request.POST['postsno']
        user = request.user
        post = Post.objects.get(sno=postsno)
        parentsno = request.POST['parentsno']
        if parentsno == '':
            comment = blogComment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,'your comment has been posted successfully')
        else:
            parent = blogComment.objects.get(sno=parentsno)
            comment = blogComment(comment=comment,user=user,post=post,parent=parent)
            comment.save()
            messages.success(request,'your reply has been posted successfully')

            
        
    return redirect(f"/blog/{post.slug}")

def createblog(request):
    user = User.objects.filter(username=request.user)
    context = {'user':user}
    if request.method == 'POST':
        title = request.POST['title']
        authorname = request.POST['authorname']
        blogtext = request.POST['blogtext']
        if blogtext == '':
            messages.error(request,'Upload faiiled! blog is emply.. please write someting')
            return redirect('/blog/createblog')
        
        addblog = Post(title=title,author=authorname,slug=title,text=blogtext)
        addblog.save()
        messages.success(request,'done hogya')
        return redirect('/blog/createblog')
    return render(request,'blog/createblog.html',context)