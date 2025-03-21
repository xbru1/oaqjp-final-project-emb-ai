"""Server for Emotion Detector application"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """Render the main page"""
    return render_template('index.html')

@app.route("/emotionDetector")
def sent_detector():
    """Get user input and return a response"""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] == 'none':
        return "Invalid Text! Please Try Again"

    to_return = f'''
    For the given statement, the system response is
    \n'anger': {response['anger']}
    \n'disgust': {response['disgust']}
    \n'fear': {response['fear']}
    \n'joy': {response['joy']}
    \n'sadness': {response['sadness']}
    \nThe dominant emotion is {response['dominant_emotion']}
    '''

    return to_return

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
