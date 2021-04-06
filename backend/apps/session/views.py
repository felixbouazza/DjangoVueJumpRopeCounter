from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets

from .serializers import SessionSerializer
from .models import Session

import base64
from PIL import Image
import io
import numpy as np
import skimage

from .detection import pose_estimation
import matplotlib.pyplot as plt
import cv2 as cv

from csv import writer
from .utils.counting import counting_jump_on_last_second


class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    queryset = Session.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)


@api_view(['POST'])
def load_frame(request):

    frame = request.data['frame']
    jumpCounter = request.data['jumpCounter']
    lastSecondData = request.data['lastSecondData']

    # Decode base 64 string
    frame = decode(frame)

    neckPoint = pose_estimation(frame)

    if neckPoint == 0:
        pass
    else:
        lastSecondData, jumpCounter = [counting_jump_on_last_second(
            neckPoint, lastSecondData, jumpCounter)[k] for k in ('lastSecondData', 'jumpCounter')]

    return Response({
        "jumpCounter": jumpCounter,
        "lastSecondData": lastSecondData
    })


def encode(image):
    with io.BytesIO() as output_bytes:
        PIL_image = Image.fromarray(skimage.img_as_ubyte(image))
        # Note JPG is not a vaild type here
        PIL_image.save(output_bytes, 'JPEG')
        bytes_data = output_bytes.getvalue()

    # encode bytes to base64 string
    base64_str = str(base64.b64encode(bytes_data), 'utf-8')
    return "data:image/png;base64," + base64_str


def decode(image64):
    encoded_image = image64.split(",")[1]
    decoded_image = base64.b64decode(encoded_image)
    img = Image.open(io.BytesIO(decoded_image))
    pixels = np.asarray(img, dtype='uint8')
    return pixels[:, :, :3]
