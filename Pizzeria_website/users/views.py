from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from .forms import RegisterForm, LoginForm


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            instance = form.save()
            instance.profile.phone_number = form.cleaned_data["phone_number"]
            instance.profile.country = form.cleaned_data["country"]
            instance.profile.save()
            return redirect("main_page")
    return render(request, "user/registration.html",
                  {"form": form})


def login_user(request):
    form = LoginForm()
    next_url = request.GET.get("next")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = get_object_or_404(User, username=form.cleaned_data["username"])
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect("main_page")
    return render(request, "user/login.html", {"form": form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("main_page")


class ProfileListView(ListView):
    queryset = User.objects.filter(is_superuser=False)
    template_name = "user/user_list.html"
    paginate_by = 4


class ProfileView(DetailView):
    template_name = "user/profile.html"
    model = User
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Profile"
        return context


class UpdateProfileView(UpdateView):
    model = User
    template_name = "user/profile_update.html"
    fields = ("first_name", "last_name", "email", "username")
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return reverse_lazy("users:profile", args=(self.object.pk,))


class DeleteUserView(DeleteView):
    model = User
    template_name = "user/delete_account.html"
    pk_url_kwarg = 'id'

    def post(self, request, *args, **kwargs):
        fname = request.POST.get('fname')
        if fname == request.user.username:
            return super().post(request, *args, **kwargs)
        else:
            messages.warning(self.request, "Your Account has NOT been deleted. Enter your username!")
            return HttpResponseRedirect(request.path_info)

    def get_success_url(self):
        messages.info(self.request, "Your account has been successfully deleted.")
        return reverse_lazy("main_page")
