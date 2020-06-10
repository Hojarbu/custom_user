from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response

# Create your views here.
from django.views.generic import UpdateView

from account.forms import CreateCustomUserForm
from django.contrib import messages
from django.views import generic

from account.models import CustomUser


class CreateCustomUserView(generic.FormView):
    template_name = 'create.html'
    form_class = CreateCustomUserForm

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.create(username=email, password=password)
        form.save()
        user.save()
        messages.add_message(self.request, messages.SUCCESS, "User successfully")
        return super(CreateCustomUserView, self).form_valid(form)


class UpdateCustomUserView(UpdateView):
    template_name = 'update.html'
    form_class = CreateCustomUserForm
    model = CustomUser

    def form_valid(self, form):
        self.object = form.save(commit=False)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = User.objects.update(username=email, password=password)
        user.save()
        self.object.save()

        return render_to_response(self.template_name, self.get_context_data())

