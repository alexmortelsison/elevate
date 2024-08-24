from django.shortcuts import render

from django.http import HttpResponse

def homepage(request):

    clientList = [

        {
            'id': '1',
            'name': 'John Doe',
            'occupation': 'Electrical Engineer'
        },

        {
            'id': '2',
            'name': 'Kate Smith',
            'occupation': 'Lawyer'
        }
    ]

    context = {'mainClientList': clientList}


    return render(request, 'crm/index.html', context)





def register(request):
    return render(request, 'crm/register.html')

