from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from .models import PostModel

@login_required(login_url='/login/')
def post_model_list_view(request):
    qs = PostModel.objects.all()
    print(qs)
    # return HttpResponse('Some Data')
    template_path = 'blog/list-view.html'
    context_dict = {
        'object_list': qs,
    }
    # Using request.user.is_authenticated() --> we can check if user is authenticated
    # and make changes as we deem fit
    # for example, load different templates for authenticated & un-authenticated users
    return render(request=request, template_name=template_path, context=context_dict)