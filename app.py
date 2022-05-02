# -*- coding: utf-8 -*-
import sys 
import os
from scripts.spell_check import *
from flask import Flask,render_template, request, session
from spello.model import SpellCorrectionModel 
sp = SpellCorrectionModel(language='en')    
sp.load('model/en_large.pkl')

app = Flask(__name__)
 


c = []


def hindi(t):
    corpus=loadCorpus(c)
    words = t.strip().split()
    corrected=[]
    for word in words:
        if word not in corpus :
            corrected.append(getCorrectWord(word,corpus))
        else:
            corrected.append(word)    
    result=' '.join(corrected)
    return result
def english(t):  
    res=sp.spell_correct(t)  
    return res['spell_corrected_text']

@app.route('/', methods=['GET'])
def index():
	return render_template('login.html')

@app.route('/output', methods=['GET','POST'])
def process_input():
        
    if request.method == 'POST':
        t=request.form['input_text']
        if request.form.get('action1')=='eng':
            res=english(t)
        elif request.form.get('action2')=='hin':
            res=hindi(t) 
    
        return render_template("login.html",prediction =res)

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
