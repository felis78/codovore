from .utils_users import *
from flask import Blueprint, jsonify, request
import traceback


userApi = Blueprint('userApi', __name__)


@userApi.route('/get_users')
def get_all_users():
    connection = connect_mariadb()
    users = get_user(connection)
    return jsonify(users)


@userApi.route('/create_user', methods=['POST'])
def create_user():
    try:
        user = request.get_json()
        connection = connect_mariadb()
        username = user['username']
        email = user['email']
        level = user['level']
        password = hash_password(user['password'])
        
        if not username or not email or not  level or not password:
            return jsonify({"error": "All fields are required"}), 400 
        
        resp = create_users(connection, username, password, email, level)
        if  resp == True:
            return jsonify({"message":f"User { username } created successfully"}), 201
        else: 
            return jsonify({"error": "Failed to create user"}), 500
        
    except Exception as e:
        print(traceback.format_exc()) 
        return jsonify({"error": "An unexpected error occurred"}), 500


@userApi.route('/check_password', methods = ['POST'])
def check_password():
    try:
        datas = request.get_json()
        email = datas['email']
        password_to_verify = datas['password']
        connection = connect_mariadb()
        verify = verify_user(connection, email, password_to_verify)
        if verify:
            return jsonify({"message":f"User {email} with password {password_to_verify} accepted"}), 201
        return jsonify({"error": "Failed to verify user, bad username or password"}), 500
        
    except Exception as e:
        print(traceback.format_exc()) 
        return jsonify({"error": "An unexpected error occurred"}), 500
    
    
# @userApi.route('/deluser', methods = ['POST'])
# def del_user():
#     try:
#         datas = request.get_json()
#         email = datas['email']
        
