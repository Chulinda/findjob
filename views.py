from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .work import get_data, get_data_from_work




def jobs(requests):





    if requests.method == 'POST':
        job = requests.POST['title']
        location = requests.POST['location']


        # url = 'https://www.work.ua/ru/jobs-'+location+'-'+job+'/'


        x,y,z,a = get_data_from_work(location,job)
        data = zip(x,y,z,a)
        
        context = {'data':data}
        return render(requests, 'index.html', context)

    return render(requests, 'index.html')