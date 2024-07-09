from rest_framework import serializers
from django.conf import settings
from django.utils import translation
from django.db.models.fields import files


langs = settings.LANGUAGES


class NameISOSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        def file_serialize(field):
            serializers.FileField.context = self.context
            return serializers.FileField().to_representation(field)

        i18n_fields = getattr(self.Meta, 'i18n_fields', dict())
        representation = super().to_representation(instance)
        for field in i18n_fields.get("exact", list()):
            representation[f'{field}'] = getattr(instance, f"{field}_{translation.get_language()}", None)
            if isinstance(representation[f'{field}'], files.FieldFile):
                representation[f'{field}'] = file_serialize(representation[f'{field}'])
        for field in i18n_fields.get("catch", list()):
            representation[f'{field}'] = getattr(instance, f"{field}_{translation.get_language()}", None)
            if isinstance(representation[f'{field}'], files.FieldFile):
                representation[f'{field}'] = file_serialize(representation[f'{field}'])
            if not representation[f"{field}"]:
                for iso, lang in langs:
                    if getattr(instance, f'{field}_{iso}', None):
                        representation[f'{field}'] = getattr(instance, f"{field}_{iso}", None)
                        if isinstance(representation[f'{field}'], files.FieldFile):
                            representation[f'{field}'] = file_serialize(representation[f'{field}'])
                        break
        return representation

    class Meta:
        model = None
        i18n_fields: dict = {
            "catch": list(),
            "exact": list(),
        }
        fields = list()
