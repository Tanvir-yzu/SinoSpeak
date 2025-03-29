from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/home.html'  # Replace with your actual template name
class TestView(LoginRequiredMixin, TemplateView):
    template_name = 'core/test.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add any test-related context data here
        context['test_types'] = [
            {'id': 1, 'name': 'Vocabulary Test'},
            {'id': 2, 'name': 'Grammar Test'},
            {'id': 3, 'name': 'Listening Test'},
            {'id': 4, 'name': 'Reading Test'},
        ]
        return context
    
class TextbookView(LoginRequiredMixin, TemplateView):
    template_name = 'core/textbook.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['textbook_sections'] = [
            {
                'level': 'HSK1',
                'chapters': [
                    {'number': 1, 'title': 'Basic Greetings'},
                    {'number': 2, 'title': 'Numbers and Counting'},
                    {'number': 3, 'title': 'Family Members'},
                ]
            },
            {
                'level': 'HSK2',
                'chapters': [
                    {'number': 1, 'title': 'Daily Activities'},
                    {'number': 2, 'title': 'Shopping'},
                    {'number': 3, 'title': 'Transportation'},
                ]
            }
        ]
        return context
    

class MePageView(LoginRequiredMixin, TemplateView):
    template_name = 'core/me.html'  # Replace with your actual template name