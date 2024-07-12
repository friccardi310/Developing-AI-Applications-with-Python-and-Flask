import requests

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  # Check if text_to_analyze is blank or only whitespace
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    if response.status_code == 200:
        response_data = response.json()
        
        # Extracting emotions and their scores
        emotions = response_data.get('emotionPredictions')[0]['emotion']
        required_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']
        emotion_scores = {emotion: emotions.get(emotion, 0) for emotion in required_emotions}
        
        # Finding the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)
        emotion_scores['dominant_emotion'] = dominant_emotion
        
        return emotion_scores
    else:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
