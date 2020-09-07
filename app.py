from flask import Flask
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/search/<string:keywords>')
def search(keywords):
    response = requests.get(f"https://api.adjaranet.com/api/v1/search?[type]=movie&keywords={keywords}")
    return response.json()

@app.route('/get-data/<string:movie_id>')
def get_data(movie_id):
    response = requests.get(f"https://api.adjaranet.com/api/v1/movies/{movie_id}?filters[with_directors]=3&source=adjaranet")
    return response.json()

@app.route('/get-files/<string:movie_id>/<string:season_index>')
def get_movie_files(movie_id, season_index):
    response = requests.get(f"https://api.adjaranet.com/api/v1/movies/{movie_id}/season-files/{season_index}?source=adjaranet")
    return response.json()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
