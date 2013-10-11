from django.shortcuts import render_to_response,redirect
from django.contrib.auth import *
from django.template import RequestContext
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from teemo.auth.forms import *

def auth(request):
	if request.user.is_authenticated():
		return redirect('/')
	else:
		c = {}
		c.update(csrf(request))
		c['form'] = SimpleUserCreation()
		# c['authform'] = SimpleAuthForm()
		return render_to_response('auth.html',c,context_instance=RequestContext(request))

def register(request):
	return HTTPResponse('hi')

