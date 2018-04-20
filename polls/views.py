# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def index(request):

	return render(request, 'index.html')

# Create your views here.

def popNatal(request):

	response = requests.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/2403251')

	if response.status_code in (201, 200):
		parsed = json.loads(response.text)
		logging.info(json.dumps(parsed, indent=4, sort_keys=True))
		return parsed
	else:
		logging.error('PUT ROLE IN USER ### ' + response.text)

	return render(request, 'index.html')