from django.contrib.auth.models import Group

def user_tools(request):
    type_user = None
    if request.user.is_authenticated:
        if(request.user.groups.filter(name='TeamLead').exists()):
            type_user = 'TeamLead'
        elif(request.user.groups.filter(name='Player').exists()):
            type_user = 'Player'


    return {'type_user': type_user}