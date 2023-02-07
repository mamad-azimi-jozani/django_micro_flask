from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://mohammad:12345678@postgres:5432/django'
CORS(app)
db = SQLAlchemy(app)


class ProductFlask(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(255))
    image = db.Column(db.String(255))


class ProductUserFlask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', 'product_id', name='user_product_unique')

# product = ProductUserFlask(id=1, title='persil', image='persil')
app.app_context().push()
db.create_all()




@app.route('/')
def index():
    product = ProductFlask.query.all()
    return f"hello world {product}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)