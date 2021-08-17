from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserForm


def log_out(req):
    logout(req)
    return redirect("listings:index")


def register(req):
    if req.method != "POST":
        form = UserForm()
    else:
        form = UserForm(data=req.POST)
        if form.is_valid():
            form.save()
            return redirect("users:login")

    context = {"form": form}
    return render(req, "registration/register.html", context)
