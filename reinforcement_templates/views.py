from django.http import HttpResponse
from django.shortcuts import render

def new_profile(request):
    context = {'email': User.objects.email, 'username': User.objects.username, 'pin': User.objects.pin, 'website': User.objects.website, 'address': User.objects.address, 'alias': User.objects.alias}
    return HttpResponse(render(request, 'profiles/new.html', context))