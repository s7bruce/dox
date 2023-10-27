from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Onlinefeedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Integer)
    customer_name = db.Column(db.String)
    customer_email = db.Column(db.String)
    #order_number = db.Column(db.Integer, nullable=True)
    #department = db.Column(db.Integer, nullable=True)
    rating = db.Column(db.String)
    feedback = db.Column(db.String)

    def to_dict(self):
        return {
            'date': self.date,
            'customer name': self.customer_name,
            'customer email': self.customer_email,
            #'order number': self.order_number,
            #'department': self.department,
            'rating': self.rating,
            'feedback': self.feedback
        }
