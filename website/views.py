from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from website.templates import *
from website.models import Enquiry
from website.forms import EnquiryForms
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login
from django.contrib import messages

# '''''''''''''''''''''''
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Enquiry
from .serializer import Enquiryserializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status



# Create your views here.

def head(request):
    customer_details = Enquiry()
    
    if request.method == "POST":

        if request.POST.get('customer_name') or request.POST.get("customer_mob") or request.POST.get('customer_time') or request.POST.get("customer_country"):
            customer_details = Enquiry()
            customer_details.customer_name =  request.POST.get("customer_name")
            customer_details.customer_mob =   request.POST.get("customer_mob")
            customer_details.customer_time =  request.POST.get("customer_time")
            customer_details.customer_country =  request.POST.get("customer_country")
            customer_details.id =  request.POST.get("id")


            customer_details.save()
            print(customer_details.id,"id prints here")
            
            return render(request,"show.html",{"form":[customer_details]})
            # return redirect(f'/show/{customer_details.id}')
        else:
            return request (render,'form.html')

    else:
        # form = Enquiry()
        return render(request,'form.html')
    return render(request,'form.html')

def show(request,user_id= None):


    obj = Enquiry.objects.all()
    return render(request,'show.html',{'form':obj})
def edit(request,id = None):
    action = Enquiry.objects.get(id = id)

    return render(request, 'edit.html',{'form':action})
def update(request,id = None):
    action = Enquiry.objects.filter(id = id)
    action.update(customer_name=request.POST.get('customer_name'))
    return redirect('/show')
    
    # return render(request, 'edit.html',{'form':action})
def delete(request,id = None):
    action = Enquiry.objects.get(id = id)
    action.delete()
    return redirect('/edit')
    
    # return render(request,'show.html',{'form':action})

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 ==password2:
            if User.objects.filter(username=username).exists():
                messages.info("username exist")
            elif User.objects.filter(email=email).exists():
                messages.INFO("userneame exist")
            else:

        
                user = User.objects.create_user(username=username,password=password1,email=email,first_name= first_name,last_name=last_name)
                user.save();
                print("created")
                return redirect("/head")
        else:
            messages.info("passsword not matching")

        # user = authenticate(request, username= customer_name,password = customer_mob)

    
        # if user:
        #     login(request, user)


        #     return HttpResponse("u r logged in ")
        # else:
        #     messages.info(request,"credential not found")

    
    else:
        print("last else block")
        return render(request,'signin.html')
def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username= username,password= password)
        if user is not None:
            auth.login(request,user)
            print("priniting")
            return redirect("/head")
        else:
            messages.info(request,'invalid credentials')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def signout(request):
    auth.logout(request)
    return render(request,"login.html")




"""Creating API for returning JSON """
"""wokirng with classe based rest api view using APIView class in restframework"""
class customer_data(APIView):
    def get(self,request):
        customer = Enquiry.objects.all()
        serializer = Enquiryserializer(customer, many= True)
        return Response (serializer.data)
    def post(self,request):
        serializer = Enquiryserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors)

class customer_detail_data(APIView):
    def get_object(self,pk):
        try:
            customer = Enquiry.objects.get(pk = pk)
            print(customer,"customer")
            return customer
        except Exception as e:
            return None
    def get(self,request,pk,*args, **kwargs):
        customer = self.get_object(pk)
        serializer = Enquiryserializer(customer)
        if customer:
            return Response(serializer.data)
        else:
            return Response({"msg: request not available"})
    # def post(self,request,pk):
    #     customer = self.get_object(pk)
    #     serializer = Enquiryserializer(customer,data= request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
        # return Response({'msg':"invalid"})
    def put(self,request,pk,*args, **kwargs):
        customer = self.get_object(pk)
        serializer = Enquiryserializer(customer,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({"msg: request not available"})
    def delete(self,request,pk,*args, **kwargs):
        customer = self.get_object(pk)
        if customer:
            customer.delete()
            return Response({'msg:msg is deleted'})
        else:
            return Response({"msg":"not found"})
        
"""Start wokirng with classe based rest api view using Genericview and mixins restframework classes"""

