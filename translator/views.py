from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def index(request):
    translated_text = None
    if request.method == 'POST':
        text = request.POST['text']
        source_lang = request.POST['source_lang']
        target_lang = request.POST['target_lang']

        # استدعاء Google Translation API
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={source_lang}&tl={target_lang}&dt=t&q={text}"
        response = requests.get(url)
        if response.status_code == 200:
            result = response.json()
            translated_text = ''.join([item[0] for item in result[0]])
    
    return render(request, 'translator/index.html', {'translated_text': translated_text})
