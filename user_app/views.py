from django.shortcuts import render
from django.http import JsonResponse
from models import userInfo
from django.template import RequestContext

def userData (request):
	information = userInfo.objects.all()
	result = {}
	for info in information:
		result[info.pk] = {
			'first_name': info.first_name,
			'last_name': info.last_name,
			'age': info.age,
			'address': info.address,
			'birth_date': info.birth_date,
		}


	response = JsonResponse(result)
	return response



def createUser (request):
	if request.method == 'POST':
		a = userInfo()
		a.first_name = request.POST.get('first_name', '')
		a.last_name = request.POST.get('last_name', '')

		a.save()
		return JsonResponse('Added successfully')
