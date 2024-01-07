
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Leave



def home(request):
    if request.method == 'POST':
        # Handle form submission logic here
        # Extract data from the request.POST dictionary

        # Example: Retrieve values
        employee_name = request.POST.get('employee_name')
        leave_type = request.POST.get('leave_type')
        leave_description = request.POST.get('leave_description')
        leave_from = request.POST.get('leave_from')
        leave_to = request.POST.get('leave_to')
        proof_attachment = request.FILES.get('proof_attachment')  # For file upload
        application_date = request.POST.get('application_date')
        # Create and save a Leave instance
        leave = Leave(
            employee_name=employee_name,
            leave_type=leave_type,
            leave_description=leave_description,
            leave_from=leave_from,
            leave_to=leave_to,
            proof_attachment=proof_attachment,
            application_date=application_date
        )
        leave.save()

        return HttpResponse("Leave form submitted successfully")  # Modify the response as needed

    return render(request, 'abc.html')

   