from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _
from PIL import Image

from characters.dataclasses.responses import Status


@deconstructible
class FileExtensionValidator(object):
    message = _("Файлы данного типа не поддерживаются.")
    code = Status.INVALID

    def __init__(self, allowed_extensions):
        self.allowed_extensions = allowed_extensions

    def __call__(self, value):
        extension = value.name.split('.')[-1].lower()
        if extension not in self.allowed_extensions:
            raise ValidationError(self.message, code=self.code)
