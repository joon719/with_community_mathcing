from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def getRoute(request):
    routes = [
        {
            'Endpoint' : '/withapp/' ,
            'method' : 'GET' ,
            'body' : None ,
            'description' : 'Returns an array of notes'
        },
        {
            'Endpoint' : '/withapp/id' ,
            'method' : 'GET' ,
            'body' : None ,
            'description' : 'Returns a single note object'
        },
        {
            'Endpoint' : '/withapp/create/' ,
            'method' : 'POST' ,
            'body' : {'body' : ""} ,
            'description' : 'Creates new note with data sent in post req'
        },
        {
            'Endpoint' : '/withapp/id/update/' ,
            'method' : 'PUT' ,
            'body' : {'body' : ""} ,
            'description' : 'Create an existing note with data sent'
        },
        {
            'Endpoint' : '/withapp/id/delete/' ,
            'method' : 'DELETE' ,
            'body' : None ,
            'description' : 'Deletes and exiting note'
        },
    ]
    return Response(routes)