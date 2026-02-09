# 
from django.shortcuts import render, redirect
from .models import contact

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")   # ← space काढला
        message = request.POST.get("message")

        contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )

        return redirect("contact")

    return render(request, "TEJAL2005app/contact.html")
