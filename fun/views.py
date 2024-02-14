from django.shortcuts import render
from django.core.exceptions import PermissionDenied
# Create your views here
                        
def one(request):
        raise PermissionDenied                            