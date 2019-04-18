import json
import fileinput
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

def main():
    visual_recognition = VisualRecognitionV3('2018-03-19',iam_apikey='0jaBn4dvOecmCRTGQe4e6uoXDHGow7_mFvqOr4N')
    with open('images/classifyme3.zip', 'rb') as images_zip:
        response = visual_recognition.classify(
            images_zip, threshold=0.0,
            classifier_ids='fire_types_1841952908').get_result()
        print(json.dumps(response, indent=2))


main()



#-------------------Graveyard of code rip-----------------------------

#visual_recognition = VisualRecognitionV3(
     #   '2018-03-19',
      #  iam_apikey='09tx6UjaBn4dvOecmCRTGQe4e6uoXDHGow7_mFvqOr4N')
       # url = 'https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/640px-IBM_VGA_90X8941_on_PS55.jpg'

    #classes_result = visual_recognition.classify(url=url).get_result()
    #print(json.dumps(classes_result, indent=2))
#classA_positive_examples = open(r"C:\\Users\\drags\\Documents\\classA.zip")
#classB_positive_examples = open(r'C:\\Users\\drags\\Documents\\classB.zip')
#classC_positive_examples = open(r'C:\\Users\\drags\\Documents\\classC.zip')
#classD_positive_examples = open(r'C:\\Users\\drags\\Documents\\classD.zip')
#classK_positive_examples = open(r'C:\\Users\\drags\\Documents\\classK.zip')


#headers = {'apikey:09tx6UjaBn4dvOecmCRTGQe4e6uoXDHGow7_mFvqOr4N'}
# payload = {'form':"classA_positive_examples=@classA.zip",
# 'form':"classB_positive_examples=@classB.zip",
# 'form':"classC_positive_examples=@classC.zip",
# 'form':"classD_positive_examples=@classD.zip",
# 'form':"classK_positive_examples=@classK.zip",
# 'form':"negative_examples=@negative.zip",
# 'form':"name=fires"}

# r = requests.post("https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers?version=2018-03-19",
# data=payload, headers=headers)
#conn = http.client.HTTPConnection("https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers?version=2018-03-19")
#conn.request("POST", "", payload, headers)
#response = conn.getresponse()

# print(r)
