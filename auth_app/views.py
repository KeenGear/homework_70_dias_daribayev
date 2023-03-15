from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        context = {}
        return render(request, self.template_name, context=context)

    def post(self, request):
        context = {}
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task_list')
        else:
            context['has_error'] = True
        return render(request, self.template_name, context=context)


def logout_view(request):
    logout(request)
    return redirect('task_list')
