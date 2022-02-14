from rest_framework import serializers
from .models import BookModel


class BookSerializer(serializers.ModelSerializer):
    TITLE_VALIDATION_ERROR_MESSAGE = 'Title must start with capital letter'

    # custom validator
    def validate(self, data):
        """
        checks if title starts with a capital letter --> throws error if not
        """
        title = data['title']
        if title:
            start_letter = title[0]
            if start_letter.islower():
                raise serializers.ValidationError(BookSerializer.TITLE_VALIDATION_ERROR_MESSAGE)
        return data

    class Meta:
        model = BookModel
        fields = '__all__'
