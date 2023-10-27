from flask import redirect, jsonify, render_template, request
import pandas as pd
from app.models import db, Onlinefeedback
from flask import Blueprint
import requests

routes_bp = Blueprint(
    'routes_bp', __name__,
    template_folder='templates',
    static_folder='static'
)
@routes_bp.route('/')
def home():
    return render_template('home.html')

@routes_bp.route('/get_posts', methods=['GET'])
def get_posts():

        return 'test'

@routes_bp.route('/import')
def import_csv():
    title = 'Import Datasets'
    return render_template('import_csv.html',title=title)


@routes_bp.route('/import/upload_file',methods={'POST'})
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
        parse_csv(uploaded_file.filename)
    return redirect('/import')

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
    return 'test'

@routes_bp.route('/reviews')
def reviews():
    return render_template('reviews.html')

@routes_bp.route('/api/reviews')
def get_reviews():
    return {'data': [review.to_dict() for review in Onlinefeedback.query]}


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
    channel_id = "Contactless%2520Pickup%2520Arrival?"
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