from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
# Create your views here.

def home(request):
    template = loader.get_template("home/myhome.html")
    return HttpResponse(template.render())
#We are defining another function which will returns some values to template
def send(request):
    template = loader.get_template("home/show.html")
    message = {
        "firstName":"John",
        "lastName" :"Doe",
        "salaryInfo":{
            "basic":12000,
            "HRA":0.02,
            "TDS":0.01,
            "DA"  :0.02
            
        },
        "AccountInfo":{
              "account_no":[44445677888,5567678866],
              "bank_names":['SBI','ICICI'],
              "branches": ['Kolkata','Howrah']
        },
        "contactInfo":{
            "phone":"7003959558",
            "e-mail":"john.doe@gmail.com"
        },
        "address":{
            "state":"WB",
            "city":"Kolkata",
            "pinCode":712235
        }
    }
    DA = message['salaryInfo']['basic'] * message['salaryInfo']['DA']
    message['salaryInfo']['DA']=DA
    #This is where we are binding value and sending through request
    return HttpResponse(template.render(message,request))




