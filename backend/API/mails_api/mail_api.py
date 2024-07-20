from .mails_utils import *
from flask import Blueprint, jsonify, request


mail_api = Blueprint('mailApi', __name__)

@mail_api.route('/contact', methods=['POST'])
def contact():
    try:
        datas= request.get_json()
        subject = datas['subject']
        body = datas['body']
        sender = datas['sender']
        if send_me_email(subject, body, sender):
            return jsonify({"message": "Mail sent successfully"}), 201
    except Exception as e:
        print(f"error: {e}")
        return jsonify({"error": "Failed to send mail"}), 500
        
        
        