from flask import Flask,request,render_template
from tensorflow.keras.models import load_model
import numpy as np


app=Flask(__name__)
model=load_model('mod1.h5')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        kms=float(request.form['kms'])
        year=int(request.form['year'])
        price=float(request.form['price'])
        year=2020-int(year)
        fuel=request.form['FUEL']
        if fuel=='CNG':
            cng=1
            pet=0
            die=0
        elif fuel=='Petrol':
            cng=0
            pet=1
            die=0
        else:
            cng=0
            pet=0
            die=0
        tr=request.form['Transmission']
        if tr=='Automatic':
            aut=1
            man=0
        else:
            aut=0
            man=1
        lis=[price,kms,year,cng,pet,die,aut,man]
        a=np.array(lis)
        a = np.expand_dims(a, axis=0)
        pred=model.predict(a)
        return render_template('index.html',pred=pred)

    return render_template('index.html')

if __name__=='__main__':
    print("starting server")
    app.run(debug=True)