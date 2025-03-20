import requests
import json

def emotion_detector(text_to_analyse):
	url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
	header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
	obj = { "raw_document": { "text": text_to_analyse } }
	response = requests.post(url, json = obj, headers=header)
	formatted = json.loads(response.text)
	emotions = formatted['emotionPredictions'][0]['emotion']

	# Loop through the emotions and get the one with the highest value, then reassign it to the object
	highest = 0
	dominant = 'Unknown'
	for emotion, value in emotions.items():
		if value > highest:
			highest = value
			dominant = emotion
	emotions['dominant_emotion'] = dominant

	# print(formatted)
	# print(max([emotions['anger'], emotions['disgust'], emotions['fear'], emotions['joy'], emotions['sadness'], emotions['sadness']]))
	return emotions
