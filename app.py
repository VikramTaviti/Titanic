from flask import Flask,render_template,request
import pickle

loaded_model=pickle.load(open('dtc_model2.pkl','rb'))

app=Flask(__name__)

@app.route('/',methods=['GET','POST']) #To render homepage
def home_page():
    return render_template('index.html')

def predictor(feat):
   return loaded_model.predict([feat])

@app.route('/results',methods=['POST']) #This will be called from UI
def result():
    if request.method=='POST':
        to_predict_list = request.form.to_dict()
        print(to_predict_list,'  conntctn8ox  \n') #------DEBUG
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        print(to_predict_list) #----DEBUG
        print('result is::',predictor(to_predict_list))
        result=predictor(to_predict_list)
        if int(result) == 0:
            prediction = "You will survive"
        else:
            prediction = "You will not survive"
        return render_template('results.html', prediction=prediction)
if __name__=='__main__':
    app.run(debug=True)