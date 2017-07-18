# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from stream.models import RandomNumber


@csrf_exempt
def stream(request):
    if request.is_ajax():
        print request
        number = RandomNumber.objects.get(pk=1)
        number.update_number()
        number.save()
        print "number Updated from ajax request"
        return HttpResponse('success')
    if request.method == 'GET':
        RandomNumber.objects.get_or_create(pk=1)
        return render(request, 'stream/stream.html')