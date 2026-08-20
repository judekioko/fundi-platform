from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from core.models import Job

from .forms import ProviderRegistrationForm
from .models import Provider


def register(request):
    if request.method == "POST":
        form = ProviderRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(
                request,
                "You're registered. Your profile is pending approval — "
                "we'll let you know once you're live and can start claiming jobs.",
            )
            return redirect("providers:dashboard")
    else:
        form = ProviderRegistrationForm()

    return render(request, "providers/register.html", {"form": form})


@login_required
def dashboard(request):
    provider = get_object_or_404(Provider, user=request.user)

    open_jobs = []
    if provider.is_approved:
        open_jobs = Job.objects.filter(
            category=provider.category,
            matched_provider__isnull=True,
        )

    claimed_jobs = provider.claimed_jobs.all()

    return render(request, "providers/dashboard.html", {
        "provider": provider,
        "open_jobs": open_jobs,
        "claimed_jobs": claimed_jobs,
    })


@login_required
def claim_job(request, job_id):
    provider = get_object_or_404(Provider, user=request.user)
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST" and provider.is_approved and not job.is_claimed:
        job.matched_provider = provider
        job.matched_at = timezone.now()
        job.save(update_fields=["matched_provider", "matched_at"])
        messages.success(request, f"You've claimed the {job.category} job in {job.location}.")

    return redirect("providers:dashboard")
