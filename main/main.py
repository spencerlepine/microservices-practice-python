from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQL_DATABSE_URI"] = 'mysql://root:root@db/main'

@app.route('/')
def index():
  return 'Hello'

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')