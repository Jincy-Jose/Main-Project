from msilib.schema import File
from flask import Flask, render_template, request, redirect,send_file,  flash, abort, url_for
from imb import app,db,mail
from imb import app,db,mail
from imb import app
from imb.models import *
# from flask_login import login_user, current_user, logout_user, login_required

from random import randint
import os
from PIL import Image
from flask_mail import Message
from io import BytesIO
import glob
import pandas as pd
import pickle
import tensorflow as tf



import pandas as pd
import numpy as np
import pickle



dir_path = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = "C:/Users/Jincy/Desktop/Main Project/Network Intrusion/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



@app.route('/')
def index1():
    return render_template('index1.html')












@app.route('/det',methods=['GET','POST'])
def det():
    if request.method == "POST":
        csv = request.files['csv']
        filename = "predict.csv"
        csv.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        
        model = pickle.load(open("balanced_random_forest_model_final.pkl", "rb"))
        file = open("enc.obj",'rb')
        enc_loaded = pickle.load(file)
        file.close()
        inputs = pd.read_csv("C:/Users/Jincy/Desktop/Main Project/Network Intrusion/uploads/predict.csv") #provide path of csv file with input values here
        inputs_encoded = enc_loaded.transform(inputs)
        prediction = model.predict(inputs_encoded.iloc[:,:])
        if prediction[0] == 1:


            output = "Attack"
        elif prediction[0] == 0:

            output = "Normal Connection"
        # print(output)
      
        
        return render_template("up_image1.html",output=output)
    filelist = glob.glob("C:/Users/Jincy/Desktop/Main Project/Network Intrusion/uploads/*.*")
    for filePath in filelist:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file")
        
   
  

    
    
    return render_template("up_image1.html")




