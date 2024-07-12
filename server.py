"""
Flask Application for Emotion Detection
"""

from flask import Flask, request, jsonify, render_template

from EmotionDetection import emotion_detector  # Import your emotion detection function

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index.html template.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET', 'POST'])
def detect_emotion():
    """
    Handle GET and POST requests for emotion detection.

    Returns:
        JSON: Emotion scores and dominant emotion.
    """
    if request.method == 'GET':
        text_to_analyze = request.args.get('textToAnalyze', '')
    elif request.method == 'POST':
        text_to_analyze = request.form['textToAnalyze']
    else:
        return jsonify({'error': 'Method not allowed'}), 405  # Handle other methods gracefully

    result = emotion_detector(text_to_analyze)  # Call your emotion detection function

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    formatted_result = {
        "anger": result['anger'],
        "disgust": result['disgust'],
        "fear": result['fear'],
        "joy": result['joy'],
        "sadness": result['sadness'],
        "dominant_emotion": result['dominant_emotion']
    }

    return jsonify(formatted_result)

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
