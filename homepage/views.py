from django.views.generic import TemplateView
from django.shortcuts import render
from homepage.forms import HomeForm


class HomeView(TemplateView):
	template_name = 'homepage/home.html'

	def get(self, request):
		form = HomeForm()
		return render(request, self.template_name, {'form': form})