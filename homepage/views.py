from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from homepage.forms import HomeForm


class HomeView(TemplateView):
	template_name = 'homepage/home.html'

	def get(self, request):
		form = HomeForm()
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = HomeForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			text = form.cleaned_data['post']
			form = HomeForm()
			return redirect('/home/')
			
		args = {'form': form, 'text': text}	
		return render(request, self.template_name, args)