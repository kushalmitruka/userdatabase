from django.shortcuts import render
from django.http import JsonResponse
from models import userInfo
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect

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


@csrf_protect
def createUser (request):
	import pdb;pdb.set_trace()
	if request.method == 'POST':
		a = userInfo()
		a.first_name = request.POST.get('first_name', '')
		a.last_name = request.POST.get('last_name', '')


		a.save()

		return JsonResponse({"status" : "Successful"})
