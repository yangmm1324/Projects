from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func
from prediction import *

app=Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"]='postgresql://postgres:postgres@localhost/Height_Collector'
app.config["SQLALCHEMY_DATABASE_URI"]='postgres://ydmmijlcbexjzd:34bef09bd1cf637a7db9f749cd9df3299d42f3a2bf8aee30bdd113b8f93bf1c5@ec2-52-205-99-67.compute-1.amazonaws.com:5432/dr9kjgcf9dstu?sslmode=require'
db=SQLAlchemy(app)
class Data(db.Model):
    __tablename__='data'
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_


@app.route('/')

def index():
    return render_template('index.html')

@app.route("/success", methods=["POST"])
def success():
    if request.method=="POST":
        vars=["MW","logs","logp","logd","hba","hbd","psa","strength",
            "total_excipients"]
        exps=request.form.getlist('excipient')
        exps+=[request.form["dosage"],request.form["release"],request.form["route"]]
        var_dic={var:request.form[var] for var in vars}
        for exp in exps:
            var_dic[exp]=1
        test=convert_test(var_dic)
        pred=predict(test)
        return render_template('success.html', result=pred)

if __name__=='__main__':
    app.debug=True
    app.run()
