#run this commands in terminal
# set FLASK_APP=app.py
#python -m flask run
import flask
from flask import Flask
from flask import render_template,request,redirect
app=Flask(__name__)
@app.route('/')
def main():
    return render_template('home.html')
@app.route('/results',methods=['POST','GET'])
def results():
    if request.method=="POST":
        entry=[]
        name=request.form.get("cells1")+" "+request.form.get("cells2")
        entry.append(name)
        for i in range(3,9):
                 cell=int(request.form.get(f"cells{i}"))
                 entry.append(cell)
        return render_template('results.html',entry=entry)
    return redirect('/')
    
            
        
