from django.shortcuts import render
from django.contrib.auth import login
from django.http import JsonResponse
from models import MyUser


def sign_view(request):
    if request.method == 'POST':
        email = request.body.get('email')
        username = request.body.get('username')
        password1 = request.body.get('password1')
        password2 = request.body.get('password2')

        if password1 != password2 :
            return JsonResponse({
                "message" : "Mot de passe non identique",
                "status" : 400
            }) 
        
        if len(MyUser.objects.filter(email=email)) > 0:    
            return JsonResponse({
                "message" : "Email déjà existant",
                "status" : 400
            })

        if len(MyUser.objects.filter(username=username)) > 0:    
            return JsonResponse({
                "message" : "Username déjà existant",
                "status" : 400
            })

        MyUser.objects.create_user(email=email, username=username)
        return JsonResponse({
                "message" : None,
                "status" : 200
            })