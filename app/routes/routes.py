from flask import redirect, jsonify, render_template, request
import pandas as pd
from app.models import db, Onlinefeedback
from flask import Blueprint
import requests
from sqlalchemy import desc
import emoji


routes_bp = Blueprint(
    'routes_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
@routes_bp.route('/')
def home():

    # Assuming Onlinefeedback is your SQLAlchemy model for the table
    text_to_clouds = Onlinefeedback.query.order_by(desc(Onlinefeedback.date)).limit(10).all()
    text = ""
    for text_to_cloud in text_to_clouds:
        text = text + " " + str(text_to_cloud.feedback)
    str(text)
    ten_reviews =  Onlinefeedback.query.order_by(desc(Onlinefeedback.date)).all()
    Tex = ""
    for last_ten_reviews in ten_reviews:
        Tex = Tex + " " + str(last_ten_reviews.feedback)
    str(Tex)

    return render_template('home.html', text_to_cloud=text, last_ten=Tex)

@routes_bp.route('/get_posts', methods=['GET'])
def get_posts():

        return render_template('getposts.html')

@routes_bp.route('/settings')
def import_csv():
    title = 'Import Datasets'
    return render_template('import_csv.html',title=title)


@routes_bp.route('/import/upload_file',methods={'POST'})
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        parse_csv(uploaded_file.filename)
    return redirect('/settings')

def parse_csv(file_path):
    csv_data = pd.read_csv(file_path)
    for i, row in csv_data.iterrows():
        onlinefeedback = Onlinefeedback(
            date=row['Date'],
            customer_name=row['Customer Name'],
            customer_email=row['Customer Email'],
            rating=row['Rating (Stars)'],
            feedback=row['Feedback']
        )
        db.session.add(onlinefeedback)
    db.session.commit()

@routes_bp.route('/home')
def overview():
    return render_template('home.html')


@routes_bp.route('/reviews')
def reviews():
    text_to_clouds = Onlinefeedback.query.order_by(desc(Onlinefeedback.date)).limit(10).all()
    text = ""
    for text_to_cloud in text_to_clouds:
        text = text + " " + str(text_to_cloud.feedback)
    str(text)
    return render_template('reviews.html', text_to_cloud=text)

@routes_bp.route('/wordcloud')
def wordcloud():
    text_to_clouds = Onlinefeedback.query.order_by(desc(Onlinefeedback.date)).limit(10).all()
    text = ""
    for text_to_cloud in text_to_clouds:
        text = text + " " + str(text_to_cloud.feedback)
    str(text)
    return render_template('wordcloud.html', text_to_cloud=text)

@routes_bp.route('/api/reviews')
def get_reviews():
    return {'data': [review.to_dict() for review in Onlinefeedback.query]}

@routes_bp.route('/api/reviews/last10')
def get_reviews_last10():
    return {'data': [review.to_dict() for review in Onlinefeedback.query]}

def get_recent_entries():
    # Query the database to get the most recent 10 entries
    recent_entries = (
        session.query(YourModel)
        .order_by(YourModel.timestamp.desc())
        .limit(10)
        .all()
    )
    return recent_entries


#api implamentation below
def get_access_token():
    # Implement a function to retrieve the access token from your authentication mechanism
    # This can be through Azure AD authentication or any other method based on your app's setup
    # Return the access token for authentication with Microsoft Graph API
    # Ensure to handle token expiration and refresh logic as needed
    pass

# Microsoft Graph API endpoint for retrieving channel messages
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages"


@routes_bp.route('/get_posts_api', methods=['GET'])
def get_posts_api():
    team_id = '6ef14084-6f86-45c2-a593-ce9d6f460cdf'
    channel_id = "19%3a0efe0fa61d764fa38f0d8c88dca38f15%40thread.tacv2"
    access_token = get_access_token()  # Implement this function to retrieve access token

    headers = {
        'Authorization': 'Bearer ' + 'access_token',
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Make a GET request to retrieve messages from the specified channel
    response = requests.get(GRAPH_API_ENDPOINT.format(team_id=team_id, channel_id=channel_id), headers=headers)

    if response.status_code == 200:
        posts = response.json()
        return jsonify(posts),render_template('getposts.html')
    else:
        return jsonify({'error': 'Failed to retrieve posts'}), response.status_code