from django.shortcuts import render
from .models import Text
import django.contrib.auth
from django.http import JsonResponse
from django.http import HttpResponse
from .encryption import create_password_key

# Create your views here.


def textview(request, slug):
    obj, created = Text.objects.get_or_create(
        slug=slug, defaults={"text": "", "password": create_password_key(123)}
    )
    return render(request, "text/textpage.html", {"obj": obj, "created": created})


def home(request):
    return render(request, "text/index.html", {})


def update(request):
    if request.POST.get("action") == "post":
        slug = request.POST.get("slug")
        text = request.POST.get("newText")
        obj = Text.objects.get(slug=slug)
        obj.text = text
        obj.save()
        response = JsonResponse({"status": "OK", "text": text})
        return response


def delete(request):
    if request.POST.get("action") == "post":
        slug = request.POST.get("slug")
        obj = Text.objects.get(slug=slug)
        obj.delete()
        response = JsonResponse({"status": "OK"})
        return response


def download(request):
    if request.POST.get("action") == "post":
        slug = request.POST.get("slug")
        obj = Text.objects.get(slug=slug)
        text = obj.text
        response = JsonResponse({"text": text, "filename": slug})
        return response


def reset_pass(request):
    if request.POST.get("action") == "post":
        slug = request.POST.get("slug")
        password = request.POST.get("newPass")
        obj = Text.objects.get(slug=slug)
        password_key = create_password_key(password)
        obj.password = password_key
        obj.save()
        response = JsonResponse({"status": "OK", "password_local": password})
        return response


def grant_access(request):
    if request.POST.get("action") == "post":
        slug = request.POST.get("slug")
        password = request.POST.get("pass")
        obj = Text.objects.get(slug=slug)
        pass_key = create_password_key(password)
        if obj.password == pass_key:
            response = JsonResponse(
                {
                    "status": "OK",
                    "text": obj.text,
                    "safety": False,
                    "password_local": password,
                }
            )
            return response
        else:
            response = JsonResponse(
                {
                    "status": "NOTOK",
                    "text": "incorrect password, try again",
                    "safety": False,
                }
            )
            return response


def handle_404_view(request, exception=None):
    return render(request, "text/404.html", status=404)
