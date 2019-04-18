import json
import fileinput
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

visual_recognition = VisualRecognitionV3('2018-03-19',iam_apikey='0jaBn4dvOecmCRTGQe4e6uoXDHGow7_mFvqOr4N')
response = visual_recognition.get_classifier('fire_types_1841952908').get_result()
print(response)
