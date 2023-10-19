from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class onlinefeedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    customer name = db.Column(db.String)
    order number = db.Column(db.Integer)
    department = db.Column(db.Integer)
    rating = db.Column(db.String)
    feedback = db.Column(db.String)

    def to_dict(self):
        return {
            'date': self.date,
            'customer name': self.customer_name,
            'order number': self.order_number,
            'department': self.department,
            'rating': self.rating,
            'feedback': self.feedback
        }
