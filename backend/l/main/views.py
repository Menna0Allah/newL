from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'success':'login successed dude',
                'username': username
            }, status=200)
        else:
            return JsonResponse({'failed':'login failed dude',},status=401)
    else:
        return JsonResponse({'failed request':'only POST requests allowed'},status=405)

@csrf_exempt
def register_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        try:
            user = User.objects.create_user(username=username,password=password)
            login(request, user)
            return JsonResponse({'success':'register successed dude'})
        except:
            return JsonResponse({'failed':'register failed dude'},status=400)
    else:
        return JsonResponse({'failed':'only POST requests allowed'},status=405)
    
@csrf_exempt
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({'success':'logout sccessed dude'},status=200)
    return JsonResponse({'failed':'only POST requests allowed'})






















# json.loads():

# json : trading data betwwen server and browser - loads : to deserialization 

# JSON Object → Python Dictionary
# JSON Array → Python List
# JSON String → Python String
# JSON Number → Python int أو float
# JSON Boolean (true/false) → Python True/False
# JSON null → Python None