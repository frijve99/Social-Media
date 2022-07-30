from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required #
from django.contrib.auth import authenticate, login,logout 
from django.contrib import messages
from django.http import HttpResponse
import uuid
from .models import Profile
from .helpers import verify_account_sendmail,forget_pass_sendmail

# Create your views here.

#Signin
def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid User')
            return redirect('signin')
    else:
        return render(request, 'signin.html')
    

#For Verifying Email
def verify_email(request,token):

    if Profile.objects.filter(auth_token = token).exists():                     #checking if the token exists

      profile_obj = Profile.objects.filter(auth_token = token).first()   #getting the profile object via token
      user_obj = User.objects.get(username=profile_obj.username)
      user_obj.is_active=True                                              #Put the user in active mode

      profile_obj.is_verified = True                                    #Put the user in active mode 
      user_obj.save()
      profile_obj.save()
      
      #auto login and direct to welcome Setting Page
      username = user_obj.username
      password = user_obj.password
      print(password)
    #   user = us

    #   if user is not None:
    #         auth.login(request,user)
    #         return redirect('home')
    #   else:
    #         messages.info(request, 'Invalid User')
    #         return redirect('signin')
      user_log = user_obj
      auth.login(request,user_log)
      
    #   messages.info(request, 'Account Has Been Verified.')
    #   return redirect(f'/verify_email/{token}/')
      return redirect('welcomeSettings')                                        
    else:       
      return render(request,'verify_email.html')


#Create a new account
def signup(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username,password=password, email=email)
                user.is_active=False
                user.save()
                verify_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(user = user , username=username,auth_token = verify_token,id_user = user.id)
                profile_obj.save()
                verify_account_sendmail(user.email,verify_token)
                messages.info(request,'An email has been sent')               
                return redirect('signup')
        else:
            messages.info(request, 'Password dont match')
            return redirect('signup')
    else:
        return render(request,'signup.html')


#logout from site
@login_required(login_url='signin')
def logout_view(request):
    logout(request)
    return redirect('signin')
   

@login_required(login_url='signin')
def welcomeSettings(request):
    profile_obj = Profile.objects.get(user = request.user)
    context = {
        'user_profile' : profile_obj,    
    }

    if request.method=='POST':
        if request.FILES.get('image') == None:
            image = profile_obj.profileimg
        else:
            image = request.FILES.get('image')
            
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']        
        bio = request.POST['bio']
        country = request.POST['country']
        gender = request.POST['gender']
        dob = request.POST['dateofbirth']


        #saving the Profile
        profile_obj.gender = gender
        profile_obj.profileimg = image
        profile_obj.bio = bio
        profile_obj.gender
        profile_obj.country = country
        profile_obj.dob = dob
        profile_obj.firstname = firstname
        profile_obj.lastname = lastname

        
        #changing the auth token also generating forgot pass token
        auth_token = str(uuid.uuid4())
        forget_pass_token = str(uuid.uuid4())
        profile_obj.auth_token = auth_token
        profile_obj.forget_pass_token = forget_pass_token

        profile_obj.save()
        return redirect('profile')
    else:  
        return render(request,'welcomeSettings.html',context)


@login_required(login_url='signin')
def accountSettings(request):
    profile_obj = Profile.objects.get(user = request.user)
    context = {
        'user_profile' : profile_obj,    
    }

    if request.method=='POST':
        if request.FILES.get('image') == None:
            image = profile_obj.profileimg
        else:
            image = request.FILES.get('image')
            
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']        
        bio = request.POST['bio']
        country = request.POST['country']
        gender = request.POST['gender']
        dob = request.POST['dateofbirth']


        #saving the Profile
        profile_obj.gender = gender
        profile_obj.profileimg = image
        profile_obj.bio = bio
        profile_obj.gender
        profile_obj.country = country
        profile_obj.dob = dob
        profile_obj.firstname = firstname
        profile_obj.lastname = lastname

        
        #changing the auth token also generating forgot pass token

        profile_obj.save()
        return redirect('accountSettings')
    else:  
        return render(request,'accountSettings.html',context)

#User Profile page
@login_required(login_url='signin')
def profile(request):
    profile_obj= Profile.objects.get(user = request.user)
    context = {
        'user_profile' : profile_obj,    
    }
    return render(request,'profile.html',context)

@login_required(login_url='signin')
def about(request):
    profile_obj= Profile.objects.get(user = request.user)
    context = {
        'user_profile' : profile_obj,    
    }
    return render(request,'about.html',context)



#Default Home Page
@login_required(login_url='signin')
def home(request):
    profile_obj = Profile.objects.get(user = request.user)
    context = {
        'user_profile' : profile_obj,    
    }

    return render(request,'index.html',context)  

#If Password is forgotten
def forgetPassword(request):
    if request.method=='POST':
        username = request.POST['username'] 

        if User.objects.filter(username=username).exists():
            user_obj = User.objects.get(username=username) #create a object of the user
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user = user_obj)
            forget_pass_sendmail(user_obj.email ,token)
            profile_obj.forget_pass_token = token
            profile_obj.save()
            messages.info(request,'An email has been sent')
            return redirect('forgetPassword')

        else:
            messages.info(request, 'No User Found.')
            return redirect('forgetPassword')
    else:
        return render(request,'forgetPassword.html')

#reset the password --->> forgetpassword
def resetPassword(request,token):
        
        # context = {'user_id' : profile_obj.user.id}
        
    if request.method == 'POST':
            profile_obj = Profile.objects.filter(forget_pass_token = token).first()
            new_password = request.POST.get('password')
            confirm_password = request.POST.get('password2')

            #checking if the password match      
            if  new_password != confirm_password:
                messages.info(request, 'Password do not match!!')
                return redirect(f'/resetPassword/{token}/')
            

            username = profile_obj.username        
            # user_id = profile_obj.user.name
            user_obj = User.objects.get(username=username)
            user_obj.set_password(new_password)

            user_obj.save()

            #changing the token again
            token = str(uuid.uuid4())
            profile_obj.forget_pass_token = token
            profile_obj.save()
            return redirect('signin')
    else:
        return render(request,'resetPassword.html')

@login_required(login_url='signin')
def changePassword(request):
    user_obj = request.user
    username = user_obj.username
    # messages.info(request, user_obj.username)
    if request.method == 'POST':
        password = request.POST.get('password')
        new_password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
        if  new_password != confirm_password:
            messages.info(request, 'Password do not match!!')
            return redirect('changePassword')
        else:
            user = auth.authenticate(username=username,password=password)
            if user is not None:
               user_obj.set_password(new_password)
               user_obj.save()
               return redirect('signin')
            else:
               messages.info(request, 'Incorrect Password')
               return redirect('changePassword')

    else:
        return render(request,'changePassword.html')