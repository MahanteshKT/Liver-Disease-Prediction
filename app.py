import numpy as np
import pandas as pd

# import pymysql
# pymysql.install_as_MySQLdb
# import MySQLdb
from liver_disease_pre import build_model

from flask import Flask,render_template,redirect,url_for,request,flash
import joblib
buildmsg=''
app=Flask(__name__)
app.secret_key='liver'
model=joblib.load('final_pickle_model.pk1')
@app.route("/register")
def register():
    context={
        'title':'Register',
    }
    return render_template("register.html",context=context)

@app.route("/login")
def login():
    context={
        'title':'Login',
    }
    return render_template("login.html",context=context)

@app.route('/build_model')
def build_modell():
    
    total=build_model()
    buildmsg=total

    flash(f"build successfull with {total}",'success')
    return redirect(url_for("home"))
    # return render_template("home.html",context=context)

    

@app.route("/",methods=['POST','GET'])
def home():
    
    color=''
    msgs=''
    msgg=[]
    msgg.clear()
    if request.method == 'POST':
        # Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,
        # Total_Protiens,Albumin,Albumin_and_Globulin_Ratio,Dataset
        Age=request.form["Age"]
        Gender=request.form['Gender']
        Total_Bilirubin=request.form['Total_Bilirubin']
        Direct_Bilirubin=request.form['Direct_Bilirubin']
        AP=request.form['Alkaline_Phosphotase']
        A_A=request.form['Alamine_Aminotransferase']
        Asp_Amino=request.form['Aspartate_Aminotransferase']
        Total_Protiens=request.form['Total_Protiens']
        Albumin=request.form['Albumin']
        Albumin_and_Globulin_Ratio=request.form['Albumin_and_Globulin_Ratio']
        if Age=='' or  Gender=='' or Total_Bilirubin=='' or Direct_Bilirubin=='' or AP=='' or A_A =='' or Asp_Amino=='' or Total_Protiens=='' or Albumin=='' or Albumin_and_Globulin_Ratio=='':
            flash("All input must be filled.",'error')
            return redirect(url_for("home"))
        # if Gender=='Male' or  Gender =='male':
        #     Gender=1
        # elif Gender=='female' or Gender=='Female':
        #     Gender=2
        # else:
        #     Gender=0
        msg=f"{Age},{Gender},{Total_Bilirubin},{Direct_Bilirubin},{AP},{A_A},{Total_Protiens},{Albumin},{Albumin_and_Globulin_Ratio}"
        # context['msg']=msg
        data={'Age':[float(Age)],
                'Gender':[float(Gender)],
                'Total_Bilirubin':[float(Total_Bilirubin)],
                'Direct_Bilirubin':[float(Direct_Bilirubin)],
                'Alkaline_Phosphotase':[float(AP)],
                'Alamine_Aminotransferase':[float(A_A)],
                'Aspartate_Aminotransferase':[float(Asp_Amino)],
                'Total_Protiens':[float(Total_Protiens)],
                'Albumin':[float(Albumin)],
                'Albumin_and_Globulin_Ratio':[float(Albumin_and_Globulin_Ratio)]}
    
        df=pd.DataFrame(data)
        print(df)
        prediction=model.predict_proba(df)
        print(prediction)
        output='{0:.{1}f}'.format(prediction[0][0],2)
        print(output)
        # msg=output
        if output<str(0.5):
            msgs="Liver Disease is not present."
            msg1="Percentage of occuring the liver Disease is {:.2f}%".format(float(output)*100)
            msg2="your liver is healty enough and no need to worry  "
            msg3="consume healthy food with balanced diet and take care"
            msgg=[msg1,msg2,msg3]
            color="no"


        elif output>str(0.5) and output<str(0.85) :
            msgs="Liver Disease present."
            msg1="Percentage of occuring the liver Disease is {:.2f}%".format(float(output)*100)
            msg2="You are in 2nd stage and consult the docter and follow the instructions strictly ."
            msg3="Taking vitamins,Exercising ,losing weight and medicine prescribed by your health care provider."
            msg4="avoid consumption of food that affects the liver (like alcohol,added sugar,fried foods ,salt...)"
            msg5="Avoid risky behaviour and get vacinated."
            msgg=[msg1,msg2,msg3,msg4,msg5]
            color="mod"
        elif output>str(0.85):
            msgs="Liver Disease is Present."
            msg1="Percentage of occuring the liver Disease is {:.2f}%".format(float(output)*100)
            msg2="You are in last stage and consult the docter immediately."
            msg3="For acute(sudden) liver failure,treatment includes."
            msg4="1.Inravenous(IV) fluide to maintain blood pressure."
            msg5="2.Medications such as laxatives or enemas to help flush toxins(posions) out."
            msg6="3.Blood glucose(sugar) monitoring-glucose is given to the patient if blood sugar drops"
            msg7="4.for Chronic liver failure take treatments like liver transplant Surgery"
            msgg=[msg1,msg2,msg3,msg4,msg5,msg6,msg7]
            color="yes"

    for i in range(len(msgg)):

        print(f"{msgg[i]}")
    context={
        'title':'Home',
        'msg':msgg,
        'msgs':msgs,
        'color':color,
        'total':buildmsg,
       
    }

    return render_template("home.html",context=context)




if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)