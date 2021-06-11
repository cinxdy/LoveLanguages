from flask import Flask, jsonify, request, Response, render_template
import json

app = Flask(__name__)


with open("data.json") as f:
    data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test():
    return render_template('test.html',data=data['lovelanguage'])

@app.route('/result', methods=['POST'])
def result():
    point = {'A':0,'B':0,'C':0,'D':0,'E':0,'noanswer':0}

    for num, item in enumerate(data['lovelanguage']):
        answer = request.form['question'+str(num+1)]
        point[answer]+=1
    return render_template('result.html',point=point)
    
if __name__== "__main__":
    app.run(host='0.0.0.0',debug=True)
