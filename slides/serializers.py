from rest_framework import serializers

from slides.models import Slide, Variant, Attempt


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        #fields = ('order', 'title')


class SlideSerializer(serializers.HyperlinkedModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Slide
        #fields = ('id', 'text', 'variants')


class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ('user', 'points')
