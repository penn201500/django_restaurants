# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from restaurants.models import Restaurant, Food
from django.shortcuts import render_to_response

# Create your views here.
def  menu ( request ): 
    restaurants = Restaurant.objects.all()
    return  render_to_response ( 'menu.html' , locals ())
