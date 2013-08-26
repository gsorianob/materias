# encoding: utf-8
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response


# @login_required
def setup(request):
    return render_to_response('setup.html')


# @login_required
def create(request):
    return render_to_response('create.html')
