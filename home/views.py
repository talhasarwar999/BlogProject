from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
from django.contrib import auth
from django.utils import timezone
now = timezone.now()
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def home(request):
    return render(request, "home/home.html")

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allPosts = Post.objects.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        # email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        username = request.POST['username']
        if User.objects.filter(username=username).exists():
            messages.warning(request,'This email is already taken: Try another Email')
            return redirect('home')
        if len(fname) < 3:
            messages.error(request, "Your First name must be under 3 charcter")
            return redirect('home')
        if len(lname) < 3:
            messages.error(request, "Your Last name must be under 3 charcter")
            return redirect('home')
        if not fname.isalpha():
            messages.error(request, " Your First name should be only in alphabet letters")
            return redirect('home')
        if not lname.isalpha():
            messages.error(request, " Your Last name should be only in alphabet letters")
            return redirect('home')
        if len(pass1)<6:
            messages.error(request, "Your password must be under 6 charcter")
            return redirect('home')
        if not pass1.isalnum():
            messages.error(request, " Your password cannot contain special characters")
            return redirect('index')
        if (pass1 != pass2):
            messages.error(request, " Passwords do not match")
            return redirect('home')

        # Create the user
        else:
            myuser = User.objects.create_user(username,fname, pass1)
            myuser.save()
            messages.success(request, " Your iCoder has been successfully created")
            return redirect('home')
    else:
        return HttpResponse("404 - Not found")


def handelLogin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = auth.authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            auth.login(request,user)
            messages.success(request, "Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("home")
    return HttpResponse("404- Not found")
def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')


def about(request):
    return render(request, "home/about.html")
