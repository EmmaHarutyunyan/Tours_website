from django.shortcuts import render, redirect, get_object_or_404
from .models import Tour, Gallery, Review, Contact, Booking, SlideshowImage, Video, AboutUs
from .forms import BookingForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import json
from datetime import date

def search(request):
    query = request.GET.get('query', '')
    if query:
        tours = Tour.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        contacts = Contact.objects.filter(Q(name__icontains=query) | Q(message__icontains=query))
        bookings = Booking.objects.filter(Q(customer_name__icontains=query) | Q(customer_email__icontains=query))
    else:
        tours = Tour.objects.none()
        contacts = Contact.objects.none()
        bookings = Booking.objects.none()

    return render(request, 'main/search_results.html', {
        'query': query,
        'tours': tours,
        'contacts': contacts,
        'bookings': bookings,
    })

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('index') 
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

def index(request):
    tours = Tour.objects.all()
    hero_tours = tours
    videos = Video.objects.all()
    featured_video = videos.first() if videos.exists() else None
    other_videos = videos.exclude(id=featured_video.id) if featured_video else videos

    today = date.today()
    booked_dates = Booking.objects.filter(end_date__gte=today).values_list('start_date', 'end_date')
    booked_dates = [
        (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
        for start_date, end_date in booked_dates
    ]

    slideshow_images = SlideshowImage.objects.all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.start_date = request.POST.get('start_date')
            booking.end_date = request.POST.get('end_date')
            booking.save()
            return redirect('index')
    else:
        form = BookingForm()

    return render(request, 'main/index.html', {
        'tours': tours,
        'hero_tours': hero_tours,
        'form': form,
        'booked_dates': json.dumps(booked_dates),
        'today': today.strftime('%Y-%m-%d'),
        'slideshow_images': slideshow_images,
        'featured_video': featured_video,
        'other_videos': other_videos,
    })

def tour_detail(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    gallery = tour.gallery.all()
    reviews = tour.reviews.all()
    return render(request, 'main/tour_detail.html', {'tour': tour, 'gallery': gallery, 'reviews': reviews})

def gallery(request, tour_id):
    tour = get_object_or_404(Tour, id=tour_id)
    all_galleries = Gallery.objects.filter(tour=tour)
    return render(request, 'main/gallery.html', {
        'galleries': all_galleries,
        'tour': tour
    })

def all_galleries(request):
    galleries = Gallery.objects.select_related('tour').all()
    tours_dict = {}
    for gallery in galleries:
        if gallery.tour not in tours_dict:
            tours_dict[gallery.tour] = []
        tours_dict[gallery.tour].append(gallery.image)

    return render(request, 'main/all_galleries.html', {'tours_dict': tours_dict})

def testimonials(request):
    reviews = Review.objects.all()
    return render(request, 'main/testimonials.html', {'reviews': reviews})

def tours_list(request):
    tours = Tour.objects.all()
    return render(request, 'main/tours.html', {'tours': tours})

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Contact.objects.create(name=name, email=email, message=message)
        return redirect('contact') 
    return render(request, 'main/contact.html')

def about(request):
    about_us_content = AboutUs.objects.first() 
    return render(request, 'main/about.html', {'about_us': about_us_content})
