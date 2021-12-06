
from array import array
import os
from PIL import Image
import sys
import time
from io import BytesIO
import requests

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials


def isSugg():
    subscription_key = "49476384fc2548968bfc09ab465229ca"
    endpoint = "https://seungjoolee.cognitiveservices.azure.com/"

    computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


    print("===== Detect Adult or Racy Content - remote =====")
    remote_image_features = ["adult"]

    analyze_url = endpoint + "vision/v3.1/analyze"
    image_data = open("C:/gjjj.jpg", "rb").read()
    headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
    params = {'visualFeatures': 'adult'}
    response = requests.post(
        analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    analysis = response.json()
    isAdult = analysis['adult']['isAdultContent']
    isRacy = analysis['adult']['isRacyContent']
    print("isAdult: " + str(isAdult))
    print("isRacy: " + str(isRacy))
    return isAdult, isRacy