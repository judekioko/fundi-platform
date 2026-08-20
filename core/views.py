from urllib.parse import quote

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from .choices import CATEGORY_CHOICES
from .forms import JobForm
from .models import Job


def landing(request):
    if request.method == "POST":
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save()
            return redirect("core:job_thanks", job_id=job.id)
    else:
        form = JobForm()

    return render(request, "core/landing.html", {
        "form": form,
        "categories": CATEGORY_CHOICES,
    })


def job_thanks(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    message = "\n".join([
        "New Fundi request:",
        f"Category: {job.category}",
        f"Problem: {job.description}",
        f"Location: {job.location}",
        f"Urgency: {job.urgency}",
        f"Name: {job.name}",
        f"Phone: {job.phone}",
    ])
    whatsapp_url = f"https://wa.me/{settings.WHATSAPP_NUMBER}?text={quote(message)}"

    return render(request, "core/job_thanks.html", {
        "job": job,
        "whatsapp_url": whatsapp_url,
    })
