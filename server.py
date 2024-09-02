from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emote_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger_score = str(response[0]['anger'])
    disgust_score = str(response[1]['disgust'])
    fear_score = str(response[2]['fear'])
    joy_score = str(response[3]['joy'])
    sadness_score = str(response[4]['sadness'])
    dominant_emote = response[5]['dominant emotion']

    ret_string = ("For the given statement, the system response is 'anger' : " + anger_score
    + ", 'disgust' : " + disgust_score + ", 'fear' : " + fear_score + ", 'joy' : " + joy_score
    + ", 'sadness' : " + sadness_score + ". The dominant emotion is : " + dominant_emote + ".")

    return ret_string

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

