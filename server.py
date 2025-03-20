from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():

    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    toReturn = f'''
    For the given statement, the system response is
    \n'anger': {response['anger']}
    \n'disgust': {response['disgust']}
    \n'fear': {response['fear']}
    \n'joy': {response['joy']}
    \n'sadness': {response['sadness']}
    \nThe dominant emotion is {response['dominant_emotion']}
    '''

    return toReturn

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)