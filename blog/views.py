from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash
from blog.forms import SignUpForm,EditProfileForm,PostForm,AddComment,PostFormOrignal,EditProfileImage
from django.contrib.auth.models import User
from .models import Post
import datetime
from django.core.mail import EmailMultiAlternatives

def index(request):

    comment = AddComment
    if request.user not in request.user.profile.following.all():
        request.user.profile.following.add(request.user)
        
    following_list = request.user.profile.following.all()
    if request.method=="POST":
        form = PostForm(request.POST)
        form2 = PostFormOrignal()
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            title=form.cleaned_data['title']
            description=form.cleaned_data['description']
            post2=form2.save(commit=False)
            post2.user=post.user
            post2.title=title
            post2.description=description
            post2.save()
            form = PostForm()
            mailto=[]
            for ab in request.user.profile.following.exclude(id=request.user.id):
                    if ab.email:
                        mailto.append(ab.email)
            mail = EmailMultiAlternatives(
                subject="New Post has been Posted",
                body="'"+request.user.username+"' has posted a new post titled '"+post.title+"'",
                from_email="Punit Lohia <lohiapunit97@gmail.com>",
                to=mailto,
            )
            mail.send()
    else:
        form = PostForm()
    posts = Post.objects.filter(user__in=following_list).order_by('-createddatetime')
    return render(request,'blog/index.html',{'form':form,'posts':posts,'comment':comment},)

def initialpage(request):
    return render(request,'initialpage/initialpage.html')

def profile(request):
    data = request.user
    comment = AddComment
    followers_list = data.profile.followers.all()
    following_list = data.profile.following.exclude(id=request.user.id)
    posts = Post.objects.filter(user=request.user).order_by('-createddatetime')
    return render(request,'blog/profile.html',{"followers_list":followers_list,"following_list":following_list,"posts":posts,'comment':comment})

def allusers(request):
    data = User.objects.exclude(id=request.user.id)
    return render(request,'registration/allusers.html',{"data":data})

def user_profile(request,id):
    data = User.objects.get(pk=id)
    comment = AddComment
    followers_list = data.profile.followers.all()
    following_list = data.profile.following.exclude(id=id)
    posts = Post.objects.filter(user=data).order_by('-createddatetime')
    return render(request,'registration/user_profile.html',{"data":data,"posts":posts,'comment':comment,"followers_list":followers_list,"following_list":following_list})

def register(request):
    if request.method=="POST":
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.image = form.cleaned_data.get('image')
            user.profile.following.add(user)
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('index')
    else:
        form = SignUpForm()
    context = {'form':form}
    return render(request,'registration/register.html',context)

def EditProfile(request):
    if request.method=="POST":
        form = EditProfileForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            user = form.save()
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.profile.image = form.cleaned_data.get('image')
            user.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    context = {'form':form}
    return render(request,'registration/editprofile.html',context)

def ChangePassword(request):
    if request.method=="POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,form.user)
            return redirect('profile')

    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form':form}
    return render(request,'registration/editpassword.html',context)

def edit_post(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        form2 = PostFormOrignal()
        if form.is_valid():
            post = form.save()
            post.user=request.user
            post.save()
            post2=form2.save(commit=False)
            post2.user=post.user
            post2.title=post.title
            post2.description=post.description
            post2.save()
            return redirect('index')

    else:
        form=PostForm(instance=post)
    return render(request,'registration/edit_post.html',{"form":form})

def edit_post_profile(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save()
            post.user=request.user
            post.save()
            return redirect('profile')
    else:
        form=PostForm(instance=post)
    return render(request,'registration/edit_post.html',{"form":form})

def delete_post(request,id):
    Post.objects.get(id=id).delete()
    PostOrignal.objects.get(id=id).deleteddatetime=datetime.datetime.now()
    return redirect('index')

def delete_post_profile(request,id):
    Post.objects.get(id=id).delete()
    return redirect('profile')

def add_comment(request, id):
    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = Post.objects.get(pk=id)
            comment.save()

    return redirect('index')

def add_comment_profile(request, id):
    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = Post.objects.get(pk=id)
            comment.save()

    return redirect('profile')

def add_comment_userprofile(request, id,id2):
    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = Post.objects.get(pk=id2)
            comment.save()

    return redirect('user_profile',id)

def changeimage(request):
    if request.method == "POST":
        form = EditProfileImage(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            profileimage = form.save(commit=False)
            request.user.profile.image=form.cleaned_data.get('image')
            request.user.save()
            print("Hello")
            return redirect('profile')

    else:
        print("Hello")
        form=EditProfileImage(request.POST,request.FILES,instance=request.user)

    return render(request,'registration/changeimage.html',{"form":form})

def follow_user(request,id):
    temp = User.objects.get(pk=id)
    request.user.profile.following.add(temp)
    temp.profile.followers.add(request.user)
    return redirect('user_profile',id)

def unfollow_user(request,id):
    temp = User.objects.get(pk=id)
    request.user.profile.following.remove(temp)
    temp.profile.followers.remove(request.user)
    return redirect('user_profile',id)

def LogoutProfile(request):
    return render(request,'registration/logoutprofile.html')
