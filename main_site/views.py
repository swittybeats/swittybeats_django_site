#from django.shortcuts import render

from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'templates/main_site/index.html'

    def get_context_data(self, *args, **kwargs):
        # context = super(HomeView, self).get_context_data(*args, **kwargs)
        context = {
            'navbar_home_active': 'active',
            'navbar_contact_active': '',
        }
        return context


class ContactView(TemplateView):
    template_name = 'templates/main_site/contact.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'navbar_home_active': '',
            'navbar_contact_active': 'active',
        }
        return context
