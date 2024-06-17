from flask import Flask 
"""
To view the output of this navigate to : http://127.0.0.1:5000/
"""

app = Flask(__name__) #Flask constructor


@app.route('/')
def hello():
    return "Hello!"


@app.route('/resume')

def my_resume():
    return "This would be my resume"

if __name__ == "__main__":
    app.run()
