import json
from django.http import HttpResponse

def route(request):

    data = {"message" : "Hello World!"}
    Json_Data = json.dumps(data)
    
    return HttpResponse(Json_Data, content_type='application/json')
# Create your views here.
