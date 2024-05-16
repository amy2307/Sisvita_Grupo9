from flask import Flask
from utils.db import db
from services.persona import personas
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DATABASE_CONNECTION

#SQLAlchemy(app)
db.init_app(app)
app.register_blueprint(personas)

with app.app_context():
    db.create_all

if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True,port=5000)