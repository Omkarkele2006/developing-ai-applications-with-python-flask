"""Flask server for the emotion detection application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the submitted text and return the detected emotions."""
    text_to_analyse = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyse)

    if response["dominant_emotion"] is None:
        return "Invalid input! Try again."

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    result = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)