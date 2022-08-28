import calendar
import importlib.resources as pkg_resources
from datetime import datetime
from typing import Optional
from functools import lru_cache

from PIL import Image, ImageDraw, ImageFont

from . import resources


@lru_cache()
def talk_captain(msg: str) -> Image.Image:
    img = Image.open(pkg_resources.open_binary(resources, "base_captain.jpg"))

    x, y = coords_text = (195, 126)
    W, H = rect_size = (135, 30)

    jon = Image.new("RGB", rect_size, "white")
    img.paste(jon, coords_text)

    font = ImageFont.truetype(
        pkg_resources.open_binary(resources, "LiberationSans-Regular.ttf"), 25
    )
    draw = ImageDraw.Draw(img)  # Image
    draw.text(
        (x + W / 2, y + H / 2),
        msg,
        "black",
        align="center",
        spacing=rect_size[0],
        font=font,
        anchor="mm",
    )
    return img


def whataweek(date: Optional[datetime] = None) -> Image.Image:
    if date is None:
        date = datetime.today()
    weekday = date.weekday()
    return talk_captain(calendar.day_name[weekday])
