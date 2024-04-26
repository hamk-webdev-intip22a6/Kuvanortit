from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


# class LogInView(generic.CreateView):
#     def login_view(request):
#         if request.method == 'POST':
#             form = UserCreationForm(request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data['username']
#                 password = form.cleaned_data['password']
#                 user = authenticate(request, username=username, password=password)
#                 if user is not None:
#                     login(request, user)
#                     # Redirect to a success page.
#                     return redirect('gallerino/')
#                 else:
#                     # Redirect to a failure page (e.g., login page with error message).
#                     return redirect('')
#         else:
#             form = UserCreationForm()
#         return render(request, 'login.html', {'form': form})



