
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

print(isSugg())
#print("Is adult content: {} with confidence {:.2f}".format(analysis.adult.is_adult_content, analysis.adult.adult_score * 100))
#print("Has racy content: {} with confidence {:.2f}".format(analysis.adult.is_racy_content, analysis.adult.racy_score * 100))

'''
detect_adult_results_remote = computervision_client.analyze_image(image_data, remote_image_features)

# Print results with adult/racy score
print("Analyzing remote image for adult or racy content ... ")
print("Is adult content: {} with confidence {:.2f}".format(detect_adult_results_remote.adult.is_adult_content, detect_adult_results_remote.adult.adult_score * 100))
print("Has racy content: {} with confidence {:.2f}".format(detect_adult_results_remote.adult.is_racy_content, detect_adult_results_remote.adult.racy_score * 100))
'''
