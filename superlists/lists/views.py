from django.shortcuts import render
from django.http import HttpResponse

def home_page(request):
    content = b'<html><head><title>To-Do lists</title></head><body></body></html>'
    response = HttpResponse(content)
    return response
