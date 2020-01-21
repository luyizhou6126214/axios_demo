from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.views.generic import View
import json

# Create your views here.

class LoginView(View):

    def get(self,request):

        return render(request,'login.html')

    def post(self,request):
        pass

class ReceiveView(View):

    def get(self,request):
        data = request.GET
        username = data.get('username')
        password = data.get('password')
        return JsonResponse({'data':{'username':username}})

    def post(self,request):

        data = json.loads(request.body.decode())
        username = data.get('username')
        password = data.get('password')
        return JsonResponse({'data':{'username':username}})
