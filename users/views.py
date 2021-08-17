from django.shortcuts import render, redirect
from django.contrib.auth import logout


def log_out(req):
    logout(req)
    return redirect("listings:index")
