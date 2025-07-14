from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ComplaintForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Complaint

def home(request):
    return redirect('submit_complaint')

def submit_complaint(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save(commit=False)
            # Link complaint to user if they're logged in
            if request.user.is_authenticated:
                complaint.user = request.user
            complaint.save()
            messages.success(request, "Complaint submitted successfully!")
            return redirect('submit_complaint')  # same form page
        else:
            messages.error(request, "There was an error submitting your complaint.")
    else:
        # Pre-fill form with user data if logged in
        initial_data = {}
        if request.user.is_authenticated:
            initial_data = {
                'name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
                'email': request.user.email,
            }
        form = ComplaintForm(initial=initial_data)
    return render(request, 'complaints/submit_complaint.html', {'form': form})

def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful! Welcome to the complaint portal.")
            return redirect('user_dashboard')
        else:
            messages.error(request, "There was an error with your registration.")
    else:
        form = UserRegistrationForm()
    return render(request, 'complaints/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('user_dashboard')
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'complaints/user_login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('user_login')

@login_required
def user_dashboard(request):
    # Show only complaints submitted by the current user
    complaints = Complaint.objects.filter(user=request.user).order_by('-submitted_at')
    total_complaints = complaints.count()
    pending_complaints = complaints.filter(status='Pending').count()
    resolved_complaints = complaints.filter(status='Resolved').count()
    
    context = {
        'complaints': complaints,
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'resolved_complaints': resolved_complaints,
    }
    return render(request, 'complaints/user_dashboard.html', context)

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            messages.success(request, "Admin login successful!")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "Invalid admin credentials.")
    
    return render(request, 'complaints/login.html')

def admin_logout(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('admin_login')

@login_required
def admin_dashboard(request):
    complaints = Complaint.objects.all().order_by('-submitted_at')  # latest first
    total_complaints = complaints.count()
    pending_complaints = complaints.filter(status='Pending').count()
    resolved_complaints = complaints.filter(status='Resolved').count()

    # Analytics data for charts
    # Complaints by status
    from collections import Counter
    status_counts = dict(Counter(complaints.values_list('status', flat=True)))
    # Complaints by priority
    priority_counts = dict(Counter(complaints.values_list('priority', flat=True)))

    context = {
        'complaints': complaints,
        'total_complaints': total_complaints,
        'pending_complaints': pending_complaints,
        'resolved_complaints': resolved_complaints,
        'status_counts': status_counts,
        'priority_counts': priority_counts,
        'status_keys': list(status_counts.keys()),
        'status_values': list(status_counts.values()),
        'priority_keys': list(priority_counts.keys()),
        'priority_values': list(priority_counts.values()),
    }
    return render(request, 'complaints/dashboard.html', context)

@login_required
def resolve_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    complaint.status = 'Resolved'
    complaint.save()
    messages.success(request, f"Complaint #{complaint_id} has been resolved!")
    return redirect('admin_dashboard')

@login_required
def edit_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    
    if request.method == 'POST':
        form = ComplaintForm(request.POST, request.FILES, instance=complaint)
        if form.is_valid():
            form.save()
            messages.success(request, f"Complaint #{complaint_id} has been updated!")
            return redirect('admin_dashboard')
        else:
            messages.error(request, "There was an error updating the complaint.")
    else:
        form = ComplaintForm(instance=complaint)
    
    return render(request, 'complaints/edit_complaint.html', {'form': form, 'complaint': complaint})

@login_required
def delete_complaint(request, complaint_id):
    complaint = get_object_or_404(Complaint, id=complaint_id)
    complaint.delete()
    messages.success(request, f"Complaint #{complaint_id} has been deleted!")
    return redirect('admin_dashboard')
