from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    movie_data = {
        'movies': [
        {
        'title':'Godfather',
        'year': 1990,
        'summary': 'story of an underworld king',
        'success': True
    },
    {
        'title':'Lelam',
        'year': 1997,
        'summary': 'Rivalry between two liquor business groups',
        'success': True
    },
    {
        'title':'Thudarum',
        'year': 2025,
        'summary':'a fathers delemma',
        'success':False 
    },
    {
        'title':'Classmates',
        'year': 2006 ,
        'summary': 'A college reunion reopens old wounds and secrets among friends',
        'success': True
    },
    {
        'title':'Chotta Mumbai',
        'year': 2007,
        'summary': 'An orphaned boy in Mumbai is adopted by a local gangster.',
        'success': True
    },
    {
        'title':'Diamond Necklace',
        'year': 2012,
        'summary': 'A man juggles three wives for financial gain.',
        'success': False
    }
    ]}
    return render(request,'index.html',movie_data)