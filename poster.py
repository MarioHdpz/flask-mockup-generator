import textwrap
from PIL import ImageFont, ImageDraw, Image

POSTER_ROUTE = 'assets/poster.jpg'
FONT = 'assets/Market_Deco.ttf'
SIZE = (512, 512)

class MoviePoster:
    def __init__(self):
        self.x_text = 400
        self.y_text = 150
        self.image = self.open_image()
        self.draw = ImageDraw.Draw(self.image)

    @staticmethod
    def open_image():
        image = Image.open(POSTER_ROUTE)
        image.thumbnail(SIZE, Image.ANTIALIAS)
        return image

    def draw_text(self, text, font_size=30, spacing=30):
        font = ImageFont.truetype(FONT, font_size)
        max_width = round(300 / font_size)
        lines = textwrap.wrap(text, width=max_width)
        for line in lines:
            width, height = font.getsize(line) 
            x = (self.x_text - width) / 2
            self.draw.text(( x, self.y_text), line, font=font, fill=(0,0,0,0))
            self.y_text += height
        
        self.y_text += spacing

    def make_poster(self, title='', premiere_date='', cast=''):
        self.draw_text(title, 30, 50)

        self.draw_text('Premiere:', 12, 0)
        self.draw_text(premiere_date, 12)

        for actor in cast:
            self.draw_text(actor, 20, 0)
        
        return self.image

if __name__ == "__main__":
    poster = MoviePoster()
    poster.make_poster('EL CLUB DE LA PELEA', '01/01/2019', ['Brad Pitt', 'Edward Norton'])
    poster.image.show()
