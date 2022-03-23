# -*- coding: utf-8 -*-
import sys 
import os
from scripts.spell_check import *
from flask import Flask,render_template, request, session


app = Flask(__name__)
 

# Heroku
#from flask_heroku import Heroku
#heroku = Heroku(app)
c = []
# ======== Routing =========================================================== #
# -------- Login ------------------------------------------------------------- #
@app.route('/', methods=['GET'])
def index():
	return render_template('login.html')

@app.route('/output', methods=['GET','POST'])
def process_input():
    corpus=loadCorpus(c)
    print("done")
    if request.method == 'POST':
        t=request.form['input_text']

    words = t.strip().split()
    corrected=[]
    for word in words:
        if word not in corpus :
            corrected.append(getCorrectWord(word,corpus))
        else:
            corrected.append(word)    
    result=' '.join(corrected)
    return render_template("login.html",prediction =result)

# ======== Main ============================================================== #
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
