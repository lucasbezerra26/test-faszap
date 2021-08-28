from django.shortcuts import render

def index(request):
    return render(request, 'website/chat.html')

def roomClient(request, attendance):
    return render(request, 'website/room.html', {
        'attendance': attendance
    })

def roomAtendace(request, attendance):
    return render(request, 'website/roomAtendente.html', {
        'attendance': attendance
    })