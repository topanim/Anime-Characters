from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from PIL import Image

from characters.utils.responses import Status


@deconstructible
class ImageSizeValidator(object):
    message = _("Изображение слишком большое.")
    code = Status.INVALID

    def __init__(self, max_width=500, max_height=700):
        self.max_width = max_width
        self.max_height = max_height

    def __call__(self, value):
        image = Image.open(value)
        width, height = image.size
        if width > self.max_width or height > self.max_height:
            raise ValidationError(self.message, code=self.code)
