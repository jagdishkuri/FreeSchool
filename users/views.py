from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegisterForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get("username")
            messages.success(
                request, "Your account has been created. You can now login"
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    return render(request, "users/profile.html")

# def search_view(request):
#     query = request.GET.get('q')
#     if query:
#         # Perform search operation on your Post model
#         search_results = Post.objects.filter(title__icontains=query)
#     else:
#         search_results = None
#     return render(request, 'blog/search_results.html', {'search_results': search_results})
