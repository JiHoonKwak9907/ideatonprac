from django.shortcuts import redirect, render, get_object_or_404
from .models import Room
from django.utils import timezone
from .forms import RoomForm

def home(request):

  posts = Room.objects.all()
  posts = Room.objects.filter().order_by('time')
  return render(request, 'index.html', {'posts':posts})


def new(request):
  return render(request, 'new.html')

def create(request):
  if request.method == 'POST' or request.method == 'FILES':
    form = RoomForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect('home')
  else:
    form = RoomForm()
  return render(request, 'form_create.html', {'form':form})

def detail(request, room_id):
  room_detail = get_object_or_404(Room, pk=room_id)
  return render(request, 'detail.html', {'room_detail':room_detail})
