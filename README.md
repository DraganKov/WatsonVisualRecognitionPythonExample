# WatsonVisualRecognitionPythonExample
How to create and use custom classifiers through IBM Watson Visual Recognition Service https://imgur.com/a/m3VQNXx

Getting Starting with IBM’s Visual Recognition Service:
Pre-requisites: 
•	An IBM Watson account
•	Python 3.7 with PIP
•	Visual Studio Code
Install the Watson developer tools by entering this command into your VS code terminal:
pip install watson-developer-cloud
Then just create a new Python file and you’re set. 


Step 1: Creating the Visual Recognition Service
Login to your Watson Developer Account and Navigate to the Watson Services Page or Click this URL: https://cloud.ibm.com/developer/watson/services And create a Visual Recognition instance. Be sure to Save your API key because you’ll need it later. 


Step 2: Trying out the Built-in models
In your desired application, you may have a data model that already exists in one of the many thousands available in the general model, so to get started, save your image as a JPEG or PNG then zip it into a folder. 


import json

import fileinput

from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

visual_recognition = VisualRecognitionV3('2018-03-19', iam_apikey='yourAPIkeyHere')
with open('images/classifyme3.zip', 'rb') as images_zip:
    response = visual_recognition.classify(images_zip,classifier_ids="text").get_result()

print(json.dumps(response, indent=2))


Be sure to enter your API key that you saved before, and run it. If it all went as planned, you should see this JSON in your terminal: 
 
 https://imgur.com/hRbAEGH

As you can see by the results of my image, by giving it the label of a fire extinguisher it failed to return any useful form of data for our use case, therefore, we’ll need a custom classifier to give us our desired result.  But if your Image returned exactly what you expected, you can find a tutorial on what to do next. 


Step 3: Creating a Custom Classifier
Now begins the part, start by defining the various classes that your are looking to sort, for myself, that was the 5 different classes of fire that are most common in our everyday environments. 
 
 https://imgur.com/FDzGf9U
 
Each of these Zip folders contain yet another folder that has at least 10 images of the various angles and labels that each class pertains to. The Negative folder should contain 10+ images of things that look very similar, or could be mistaken for your classification scheme, and should not be confused by it. Upon creating this directory, be sure to save it in a location close to your python file, that way you have to do less file I/O. 


import json

import fileinput

from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

visual_recognition = VisualRecognitionV3('2018-03-19', iam_apikey=’yourAPIkeyHere’)
with open('classA.zip', 'rb') as classA, open('classB.zip', 'rb') as classB, open('./classC.zip', 'rb') as classC, open('./negative.zip', 'rb') as negative:
    model = visual_recognition.create_classifier('firetypes',
    classA_positive_examples=classA,
    classB_positive_examples=classB,
    classC_positive_examples=classC,
    negative_examples=negative).get_result()
            
print(json.dumps(model, indent=2))

Upon successful training, we get this JSON returned to us:  

https://imgur.com/Kycwxao

Step 4: Using the Classifier
Now comes the scary part, seeing if it works after all this effort. Using the same image that I initally gave to classify, I’m passing it in but calling my custom classifier instead:

import json

import fileinput

from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

visual_recognition = VisualRecognitionV3('2018-03-19', iam_apikey='yourAPIkeyHere')
with open('images/classifyme3.zip', 'rb') as images_zip:
response = visual_recognition.classify(
      images_zip, threshold=0.0,
      classifier_ids='fire_types_1841952908').get_result()
print(json.dumps(response, indent=2))

https://imgur.com/vGJqMVc

As we can see, passing in the Class B fire extinguisher returned a confidence score of a very respectable 0.877, which is 87.7%. 
