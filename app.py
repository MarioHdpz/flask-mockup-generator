""" Movie poster creator """
from flask import Flask, send_file, request
from io import BytesIO
from modules.poster import MoviePoster

app = Flask(__name__)

def convert_image(image):
    io_object = BytesIO()
    image.save(io_object, 'JPEG', quality=70)
    io_object.seek(0)
    return send_file(io_object, mimetype='image/jpeg')


@app.route('/', methods=['POST'])
def create_movie():
    poster_creator = MoviePoster()
    poster = poster_creator.make_poster(
        **request.json
    )
    return convert_image(poster)


    