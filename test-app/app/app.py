from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
  msg = os.getenv('APP_MESSAGE')
  return render_template('index.html', message=msg)

if __name__ == '__main__':
  app.run(host="0.0.0.0", debug=True)