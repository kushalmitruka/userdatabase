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



def createUser (request):
	obj = request.data
	a = userInfo()
	a.first_name = obj.first_name
	a.last_name = obj.last_name
	a.age = obj.age
	a.address = obj.address
	a.birth_date = obj.birth_date

	a.save()
	return JsonResponse('Added successfully')

