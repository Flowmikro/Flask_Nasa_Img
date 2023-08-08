from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


@app.route('/')
def mars_photos():
    nasa_api = requests.get(
        'https://api.nasa.gov/mars-photos/api/v1/rovers/Perseverance/latest_photos?api_key=DEMO_KEY')
    jasondata = json.loads(nasa_api.text)
    phohtos = jasondata['latest_photos']
    return render_template('mars_photos.html', photos=phohtos)


if __name__ == '__main__':
    app.run(debug=True)
