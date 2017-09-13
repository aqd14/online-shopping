from django.shortcuts  import render_to_response

from users.models import RegistrationForm


# Create your views here.
def register(request):
    if (request.method == 'Post'):
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            print('')
    else:
        register_form = RegistrationForm()
        
    return render_to_response('registration.html', {'form' : register_form})