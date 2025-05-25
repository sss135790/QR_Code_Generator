from flask import Flask, render_template, request, send_file
import qrcode

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        text=request.form['text'] 
        qrcode.make(text).save('.png') 
        return send_file('.png',mimetype='image/png') 
    return render_template('index.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

if __name__=='__main__':
    app.run(debug=True)