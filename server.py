from flask import Flask
from flask import render_template
from flask import request

from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect_emotion():

    text_to_analyze = request.args.get(
        "textToAnalyze"
    )

    response = emotion_detector(
        text_to_analyze
    )

    return str(response)

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
