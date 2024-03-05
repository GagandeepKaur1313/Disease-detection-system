from django.shortcuts import render, redirect
from diseaseapp.models import blogs
from diseaseapp.models import doctors
from diseaseapp.models import review
from diseaseapp.models import contactus
from diseaseapp.models import userregister
from diseaseapp.models import helpus
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def login(request):
	if request.method=="POST":
		e=request.POST.get('em')
		p=request.POST.get('pw')
		user=userregister.objects.filter(email=e,password=p)
		if len(user) >0:
			request.session['email'] = e
			return render(request,'myprofile.html')
		else:
			return render(request,'login.html',{'msg':"Invalid Candidate"})
	else:
		return render(request,'login.html')
	

def register(request):
	if request.method=="POST":
		n=request.POST.get('fnm')
		ln=request.POST.get('lnm')
		e=request.POST.get('em')
		p=request.POST.get('pw')
		c=request.POST.get('cpw')
		if userregister.objects.filter(email=e,password=p).exists():
			msg="Email Id already registered"
			return render(request,'register.html',{'msg':msg})
		else:
			if p == c:
				x=userregister()
				x.firstname=n
				x.lastname=ln
				x.email=e
				x.password=p
				x.save()
				msg="User Successfully registered"
				return render(request,'register.html',{'msg':msg})
			else:
				msg="Password and Confirm Password doesn't match"
				return render(request,'register.html',{'msg':msg})
	else:
		return render(request,'register.html')

def contact(request):
	if request.method == "POST":
		x=contactus()
		x.firstname=request.POST.get('fn')
		x.lastname=request.POST.get('ln')
		x.email=request.POST.get('em')
		x.phone=request.POST.get('ph')
		x.message=request.POST.get('tt')
		x.save()
		return render(request,'contact.html',{'msg':1})
	else:
		return render(request,'contact.html')
	

def footer(request):
	return render(request,'footer.html')

def base(request):
	return render(request,'base.html')

def allblogs(request):
	res=blogs.objects.all()
	return render(request,'allblogs.html',{'data':res})

def alldoctors(request):
	res=doctors.objects.all()
	return render(request,'alldoctors.html',{'data':res})

def detailblog(request,id):
	res=blogs.objects.get(id=id)
	return render(request,'detailblog.html',{'data':res})

def myreview(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	if request.method == "POST":
		x=review()
		x.title=request.POST.get('ti')
		x.message=request.POST.get('msg')
		x.save()
		return render(request,'review.html',{'msg':1})
	else:
		return render(request,'review.html')

def sidebar(request):
	return render(request,'sidebar.html')

def help(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	if request.method == "POST":
		x=helpus()
		x.title=request.POST.get('tt')
		x.content=request.POST.get('ct')
		x.save()
		return render(request,'help.html',{'msg':1})
	else:
		return render(request,'help.html')
	

def changepassword(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	if request.method=="POST":
		o=request.POST.get('op')
		n=request.POST.get('np')
		c=request.POST.get('cp')
		if n==c:
			user=userregister.objects.get(email=request.session['email'])
			p=user.password
			if p==o:
				user.password=n
				user.save()
				msg="Password Changed Successfully"
				return render(request,'changepassword.html',{'msg':msg})
			else:
				msg="Old password doesn't match"
				return render(request,'changepassword.html',{'msg':msg})
		else:
			msg="Password and Confirm password do not match"
			return render(request,'changepassword.html',{'msg':msg})
	else:
		return render(request,'changepassword.html')

def editprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	detail=userregister.objects.get(email=request.session['email'])
	if request.method=="POST":
		detail.firstname=request.POST.get('fn')
		detail.lastname=request.POST.get('ln')
		detail.bio=request.POST.get('bi')
		detail.age=request.POST.get('ag')
		detail.pincode=request.POST.get('pi')
		detail.contact=request.POST.get('co')
		detail.date=request.POST.get('dob')
		detail.address=request.POST.get('add')
		detail.save()
		print("Successfully Edited")
		return redirect('/myprofile/')
	else:	
		return render(request,'editprofile.html',{'i':detail})

def myprofile(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	user=userregister.objects.get(email=request.session['email'])
	if request.method=="POST":
		print("yes")
		user.image=request.FILES['file1']
		user.save()
		return render(request,'myprofile.html',{'user':user,'msg':'success'})
	else:
		return render(request,'myprofile.html',{'user':user})

def logout(request):
	if not request.session.has_key('email'):
		return redirect('/login/')
	del request.session['email']
	return redirect('/login/')

def forget(request):
	if(request.method=='POST'):
		em=request.POST.get('em')
		user=userregister.objects.filter(email=em)
		if(len(user)>0):
			password=user[0].password
			subject="Password"
			message="Welcome! Your password is"+password
			email_from=settings.EMAIL_HOST_USER
			receipent_list=[em]
			send_mail(subject,message,email_from,receipent_list)
			res="Your password sent to your respective email account"
			return render(request,'forget.html',{'res':res})
		else:
			res='This Email Id is not registered'
			return render(request,'forget.html',{'res':res})
	else:
		return render(request,'forget.html')


