#coding: utf-8
import datetime
import os

from django.core.management.base import BaseCommand
from django.core import serializers
from django.utils import simplejson as json
from django.core import serializers

from slides.models import Slide, Variant


class Command(BaseCommand):

    def handle(self, *args, **options):
        slide_index = 0
        variant_index = 0
        for filename in args:
            if not os.path.exists(filename):
                print u"Incorrect file name {0} or file doesn't exists!".format(filename)
            else:
                json_data = open(filename)
                data = json.load(json_data)

                for item in data.get('slides', {}):
                    # Перезатерем старые записи
                    obj = Slide.objects.filter(id=item.get('id'))[:1]
                    if obj:
                        obj.get().delete()
                    slide = Slide.objects.create(
                        id=item.get('id'),
                        text=item.get('text')
                    )
                    slide_index += 1
                    for variant in item.get('variants', []):
                        # Перезатерем старые записи
                        obj = Variant.objects.filter(slide=slide, variantId=variant.get('variantId'))[:1]
                        if obj:
                            obj.get().delete()

                        Variant.objects.create(
                            slide=slide,
                            variantId=variant.get('variantId'),
                            points=variant.get('points'),
                            text=variant.get('text'),
                            nextId=variant.get('nextId'),
                            comment=variant.get('comment')
                        )
                        variant_index += 1

            print u"Добавлено слайдов: {0}".format(slide_index)
            print u"Добавлено вариантов: {0}".format(variant_index)
