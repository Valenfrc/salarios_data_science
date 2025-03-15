from flask import flask, request, render_template
import json
from xgboost import XGBRegressor


app= Flask(__name__)
model=XGBRegressor()
model.load_model('../xgboost_model.json')

with open('../data/processed/dic_cl.json', 'r', encoding='utf-8') as archivo:
    dic_cl=json.load(archivo)

with open('../data/processed/dic.json', 'r', encoding='utf-8') as archivo:
     dic=json.load(archivo)

with open('../data/processed/dic_et.json', 'r', encoding='utf-8') as archivo:
     dic_et=json.load(archivo)

with open('../data/processed/dic_er.json', 'r', encoding='utf-8') as archivo:
     dic_er=json.load(archivo)

with open('../data/processed/dic_cs.json', 'r', encoding='utf-8') as archivo:
     dic_cs=json.load(archivo)

@app.route("/",methods=["GET","POST"])
def index():
     if request.method=="POST":
          val1=float(request.from["val1"])