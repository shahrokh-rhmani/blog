from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from .models import User
from .forms import FormProfile
from django.urls import reverse_lazy


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.save()

            context = {
                'new_user': new_user
            }
            return render(request, 'account/register_done.html', context)
    else:
        user_form = UserRegistrationForm()
    context = {
        'user_form': user_form
    }
    return render(request, 'account/register.html', context)


class Profile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "registration/profile.html"
    form_class = FormProfile
    success_url = reverse_lazy('account:profile')

    def get_object(self, queryset=None):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs
