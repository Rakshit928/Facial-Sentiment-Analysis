from django.http import JsonResponse
from django.shortcuts import render
from .utils import load_model, preprocess_image
from django.template.context_processors import csrf
import base64
from PIL import Image
import numpy as np
import io

def capture(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'capture.html', c)

def predict_emotion(request):
    if request.method == 'POST':
        img_data = request.POST.get('image_data')
        if not img_data:
            return JsonResponse({'error': 'No image data provided.'})

        img_str = img_data.split(',')[1]
        img_bytes = base64.b64decode(img_str)
        img = Image.open(io.BytesIO(img_bytes))
        img_processed = preprocess_image(img)

        model = load_model()
        prediction = model.predict(img_processed)
        emotion_index = np.argmax(prediction)
        emotion_labels = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
        emotion = emotion_labels[emotion_index]

        return JsonResponse({'emotion': emotion})
    else:
        return JsonResponse({'error': 'Invalid request method.'})