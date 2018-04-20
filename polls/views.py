# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import logging

def index(request):

	return render(request, 'index.html')

# Create your views here.

def popNatal(request):

	response = requests.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/2403251')


	if response.status_code in (201, 200):

		parsed = json.loads(response.text)
		data = str(parsed['projecao']['populacao'])
		print(data)
		arq = open('polls/static/data-files/dataNatal.json', 'w')	
		arq.close()
		return HttpResponse('População de Natal: '+data+' habitantes')

	else:

		logging.error('ERROR EM POPULACAO NATAL ### ' + response.text)

def popMossoro(request):

	response = requests.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/2404408')


	if response.status_code in (201, 200):

		parsed = json.loads(response.text)
		data = str(parsed['projecao']['populacao'])
		arq = open('polls/static/data-files/dataMossoro.json', 'w')
		arq.write(data) 	
		arq.close()
		return HttpResponse('População de Mossoro: '+data+' habitantes')

	else:

		logging.error('ERROR EM POPULACAO NATAL ### ' + response.text)

def popNatalMossoro(request):

	responseN = requests.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/2403251')
	responseM = requests.get('https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/2404408')


	if response.status_code in (201, 200):

		parsedN = json.loads(responseN.text)
		parsedM = json.loads(responseM.text)
		dataN = parsedN['projecao']['populacao']
		dataM = parsedM['projecao']['populacao']
		totalS = dataM + dataN
		total = str(totalS)
		arq = open('polls/static/data-files/dataMossoroNatal.json', 'w')
		arq.write(data) 	
		arq.close()
		return HttpResponse('População de Natal e Mossoro: '+total+' habitantes')

	else:

		logging.error('ERROR EM POPULACAO NATAL ### ' + response.text)

