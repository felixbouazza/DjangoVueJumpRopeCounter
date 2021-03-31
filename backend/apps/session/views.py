import re
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .serializers import SessionSerializer
from .models import Session

import base64
import cv2
import pickle
import codecs
from PIL import Image
import io
import numpy as np
import re

import skimage


class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)


@api_view(['POST'])
def load_frame(request):
    image64 = request.data['image']
    pixels = decode(image64)

    output = encode(pixels)
    return Response({
        "image": "data:image/png;base64," + output
    })


def encode(image):
    with io.BytesIO() as output_bytes:
        PIL_image = Image.fromarray(skimage.img_as_ubyte(image))
        # Note JPG is not a vaild type here
        PIL_image.save(output_bytes, 'JPEG')
        bytes_data = output_bytes.getvalue()

    # encode bytes to base64 string
    base64_str = str(base64.b64encode(bytes_data), 'utf-8')
    return base64_str


def decode(image64):
    encoded_image = image64.split(",")[1]
    decoded_image = base64.b64decode(encoded_image)
    img = Image.open(io.BytesIO(decoded_image))
    pixels = np.asarray(img, dtype='uint8')
    return pixels[:, :, :3]
