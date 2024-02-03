from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Contact
# Create your views here.


def cantact_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('.')
    ctx = {
        "form": form
    }
    return render(request, 'main/contact.html', ctx)




