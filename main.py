"""
Developed by - 
Shubh Pathak (MSM19B018)
"""

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('dashboard.html') 

@app.route('/about/')
def about():
   return render_template('about.html') 

if __name__ == '__main__':
   app.debug = True
   app.run(host="127.0.0.1",port=5000)