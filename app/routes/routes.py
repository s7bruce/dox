from flask import redirect, jsonify, render_template
import pandas as pd
from app.models import db, onlinefeedback
from flask import Blueprint
import requests

routes_bp = Blueprint(
    'routes_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


# Microsoft Graph API endpoint for retrieving channel messages
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0/teams/{team_id}/channels/{channel_id}/messages"


@routes_bp.route('/get_posts', methods=['GET'])
def get_posts():
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


def get_access_token():
    # Implement a function to retrieve the access token from your authentication mechanism
    # This can be through Azure AD authentication or any other method based on your app's setup
    # Return the access token for authentication with Microsoft Graph API
    # Ensure to handle token expiration and refresh logic as needed
    pass

