from django.shortcuts import render, redirect
from .models import Session
from .forms import SessionForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import views as auth_views

def session_list(request):
    sessions = Session.objects.all()
    return render(request, 'session_list.html', {'sessions': sessions})

# View for creating a new session
def session_create(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            return redirect('main:session-list')
    else:
        form = SessionForm()
    return render(request, 'session_form.html', {'form': form})

def session_delete(requests, pk):
    session = Session.objects.get(pk=pk)
    session.delete()
    return redirect('main:session-list')

def session_details(request, pk):
    session = Session.objects.get(pk=pk)
    return render(request, 'session_details.html', {'session': session})


class CustomPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('session-list')

    def form_valid(self, form):
        messages.success(self.request, 'Your password was successfully updated.')
        return super().form_valid(form)