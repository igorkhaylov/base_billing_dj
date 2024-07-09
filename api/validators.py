import re
from django.utils.translation import gettext
from rest_framework import serializers


def phone_validator(value):
    if re.match("^\\+?[1-9][0-9]{7,14}$", value):
        return value
    raise serializers.ValidationError(gettext("Введите верный номер телефона"))