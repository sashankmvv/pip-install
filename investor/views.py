from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from investor.models import Investor

# Create your views here.


class HoldingView(DetailView):
    model = Investor
    template_name = 'registration/view_profile.html'

    def get_object(self):
        return get_object_or_404(self.model, investor__username=self.kwargs['username'])
