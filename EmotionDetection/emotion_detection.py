import requests
import json

def emotion_detector(text_to_analyse):
	url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
	header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
	obj = { "raw_document": { "text": text_to_analyse } }
	response = requests.post(url, json = obj, headers=header)
	formatted = json.loads(response.text)
	print(response.status_code)

    # Instructions say to check only for code 400, but instead we check for any code that isn't 200 to ensure that it can handle other error types
	if (response.status_code != 200):
        # For some reason I have put his into a value before returning it
		toReturn = {'anger': 'none', 'disgust': 'none', 'fear': 'none', 'joy': 'none', 'sadness': 'none', 'dominant_emotion': 'none'}
		return toReturn
	
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
