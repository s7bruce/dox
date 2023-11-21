from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.orderinglist import ordering_list
from sqlalchemy import desc
from sqlalchemy import create_engine, Column, DateTime, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


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





# def get_recent_entries():
#     # Query the database to get the most recent 10 entries
#     recent_entries = (
#         session.query(YourModel)
#         .order_by(YourModel.timestamp.desc())
#         .limit(10)
#         .all()
#     )
#     return recent_entries

# Example usage
# recent_entries = get_recent_entries()
# for entry in recent_entries:
#     print(entry.timestamp)
