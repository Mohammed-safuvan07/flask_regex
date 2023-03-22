from flask import Flask,render_template,request
import re
app = Flask('__main__')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/details', methods=["POST"])
def detail_fun():
    if request.method == 'POST':
        text = request.form.get('texts')
        pattern = request.form.get('pattern') 
        result = re.findall(pattern,text)
        count = len(result)
    return render_template('details.html',text=text,pattern=pattern,count=count)          


if __name__ == '__main__':
    app.run(debug=True)