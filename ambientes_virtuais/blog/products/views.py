from django.http import HttpResponse

def index(resquest):
	return HttpResponse("Hello world!")