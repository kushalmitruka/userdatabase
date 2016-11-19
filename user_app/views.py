from django.shortcuts import render
from django.http import JsonResponse
from models import userInfo

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
