from django.shortcuts import render
import google.generativeai as genai

from Googleai.models import Prompts
from djangoProject15 import settings

# Create your views here.
api_key = settings.GEMINI_API_KEY
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
def home(request):
    second = model.generate_content('Tell me about googles gemini model')
    result = second.text
    return render(request,'home.html',{"Data":result})
def send_prompt(request):
    prompt_value = request.GET.get('genprompt')
    prompt = model.generate_content(prompt_value)
    results = prompt.text
    Prompts.objects.create(text=prompt_value,response=results)
    return render(request,'home.html',{'Data':results})