import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response['emotionPredictions']
    emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    dominant_emotion = 'anger'
    output=[]
    for prediction in emotion_predictions:
        for i in range(5):
            output.append({emotions[i]: prediction['emotion'][emotions[i]]})
            if prediction['emotion'][emotions[i]]>prediction['emotion'][dominant_emotion]:
                dominant_emotion = emotions[i]
    output.append({'dominant emotion': dominant_emotion})
    return output


