from django.shortcuts import render,redirect
from django.http import HttpResponse
import random
from estateapp.models import Registration
from datetime import datetime
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Property 

def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request,'index.html')
def properties(request):
    # Get the sorting option from the GET request
    sort_option = request.GET.get('sort', 'default')

    # Determine the sorting order based on the selected option
    if sort_option == 'name':
        properties = Property.objects.all().order_by('title')  # Sort by name
    elif sort_option == 'price':
        properties = Property.objects.all().order_by('price')  # Sort by price
    elif sort_option == 'date':
        properties = Property.objects.all().order_by('-created_at')  # Sort by date (newest first)
    else:
        properties = Property.objects.all()  # Default order (no specific sorting)

    return render(request, 'properties.html', {'properties': properties})
def prediction_view(request):
    return render(request, 'prediction.html')
def chat(request):
    return render(request,'chat.html')
def review(request):
    return render(request,'review.html')
def dashboard(request):
    return render(request,'dashboard.html')
def addproperty(request):
    if request.method == "POST":
        title = request.POST.get('title')
        location = request.POST.get('location')
        price = request.POST.get('price')
        description = request.POST.get('description')
        main_image = request.FILES.get('main_image')
        sliding_images = request.FILES.getlist('sliding_images')  # Handling multiple images

        # Save the property
        property_obj = Property.objects.create(
            title=title,
            location=location,
            price=price,
            description=description,
            main_image=main_image
        )

        # Save multiple sliding images (optional if your model supports it)
        for image in sliding_images:
            property_obj.sliding_images = image
            property_obj.save()

        return redirect('dashboard')  # Redirect after saving

    return render(request, 'addproperty.html')
def message(request):
    # Load initial messages if needed
    # This can be replaced with actual logic to fetch messages from the database or API
    initial_messages = []  # Placeholder for initial messages
    return render(request, 'message.html', {'initial_messages': initial_messages})
def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=Registration.objects.get(
            email=email,
            password=password
        )
        if not user:
            JsonResponse("Login Sucess")
        else:    
            return JsonResponse({"success": True, "redirect_url": "/index"})
    return render(request,'signin.html')
def propertydetail(request):
    return render(request,'properties-detail.html')
def send_otp_email(request):
    if request.method == "POST":
        email = request.POST.get("email")
        
        if not email:
            return JsonResponse({"error": "Email is required"}, status=400)

        otp = str(random.randint(100000, 999999))  # Generate 6-digit OTP

        subject = "Your OTP Code"
        message = f"Hello,\n\nYour OTP code is: {otp}\n\nUse this code to complete your registration."
        sender_email = "padmaraj7654@gmail.com"  # Must match `EMAIL_HOST_USER` in settings.py

        try:
            send_mail(subject, message, sender_email, [email])
            request.session["otp"] = otp  # Store OTP in session
            return JsonResponse({"success": "OTP sent successfully!"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        stored_otp = request.session.get("otp")

        if entered_otp == stored_otp:
            request.session["otp_verified"] = True  # Mark OTP as verified in session
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "error": "Invalid OTP"})
def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dob_str = request.POST.get('dob')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate all fields
        if not (name and phone and email and dob_str and password and confirm_password):
            return JsonResponse({"success": False, "error": "All fields are required."})

        # Validate password match
        if password != confirm_password:
            return JsonResponse({"success": False, "error": "Passwords do not match."})
        
        if not request.session.get("otp_verified"):
            return JsonResponse({"success": False, "error": "OTP verification is required."})

        # Validate unique email
        if Registration.objects.filter(email=email).exists():
            return JsonResponse({"success": False, "error": "An account with this email already exists."})

        # Convert Date of Birth
        try:
            dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
        except ValueError:
            return JsonResponse({"success": False, "error": "Invalid date format."})

        # Create user
        user = Registration(
            first_name=name,
            email=email,
            phone=phone,
            dob=dob,
            password=password
        )
    
        user.save()

        return JsonResponse({"success": True, "redirect_url": "/signin"})  # Redirect to login page

    return render(request, 'register.html')
from django.shortcuts import render

def chat(request):
    # You can pass a default room or allow user-defined chat rooms
    return render(request, 'chat.html', {
        'room_name': 'myroom'  # This can alternatively be dynamic
    })
