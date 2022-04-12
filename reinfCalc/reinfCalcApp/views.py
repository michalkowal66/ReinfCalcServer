from django.views.generic import TemplateView, ListView
from django.middleware.csrf import get_token
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts import models
import json


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileInfoView(LoginRequiredMixin, TemplateView):
    context_object_name = 'user'
    template_name = 'reinfCalcApp/user_profile.html'


class ResultsView(LoginRequiredMixin, ListView):
    model = models.Task
    template_name = 'reinfCalcApp/results.html'

    def get_queryset(self):
        tasks = self.model.objects.filter(owner=self.request.user)
        task_list = []
        if tasks:
            for task in tasks:
                task_dict = json.loads(task.save_file)
                task_list.append(task_dict)

        return task_list


def auth_app_user(request):
    user_agent = request.headers['User-Agent']
    if user_agent.startswith('python-requests'):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return HttpResponse('authenticated')
            else:
                return HttpResponseForbidden('wrong username or password')

        response = HttpResponse(get_token(request))
        return response

    raise Http404


@login_required
def upload_file(request):
    user_agent = request.headers['User-Agent']
    if user_agent.startswith('python-requests'):
        if request.method == 'POST':
            data = request.POST.get('data')
            print(data)
            current_user = models.User.objects.get(pk=request.user.id)
            task = models.Task(owner=current_user, save_file=data)
            task.save()

        response = HttpResponse(get_token(request))
        return response

    raise Http404
