import openai
import requests

API_KEY = ""
openai.api_key = API_KEY

def transcribe_audio(url):
    filename = "0.mp4"
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)


    model_id = 'whisper-1'
    media_file = open(filename, 'rb')

    response = openai.Audio.transcribe(
        # api_key=API_KEY,
        model=model_id,
        file=media_file
    )
    return response['text']