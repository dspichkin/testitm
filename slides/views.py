from rest_framework import viewsets

from slides.serializers import SlideSerializer, AttemptSerializer
from slides.models import Slide, Variant, Attempt


class SlideViewSet(viewsets.ModelViewSet):
    queryset = Slide.objects.all()
    serializer_class = SlideSerializer


class AttemptViewSet(viewsets.ModelViewSet):
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer