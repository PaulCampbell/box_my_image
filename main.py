from PIL import Image, ImageDraw, ImageFont
import requests
import urllib.parse
from flask import send_file
import io

def box_my_image(req):
    image_url = req.args['image_url']
    print(urllib.parse.unquote(image_url))
    tag_name = req.args['name']
    top = int(req.args['top'])
    left = int(req.args['left'])
    right = int(req.args['right'])
    bottom = int(req.args['bottom'])
    image_response = requests.get(urllib.parse.unquote(image_url))
    img = Image.open(io.BytesIO(image_response.content))
    print('got image')
    draw = ImageDraw.Draw(img)
    draw.rectangle((left, top, right, bottom), fill=None, outline=(240, 52, 52, 1))
    draw.rectangle((left, top -15, right, top), fill=(240, 52, 52, 1))
    draw.text((left + 2, top -13),tag_name,(255,255,255))

    del draw

    return serve_pil_image(img)


def serve_pil_image(pil_img):
    img_io = io.BytesIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')
