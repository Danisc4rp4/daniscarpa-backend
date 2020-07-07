from flask_restful import Resource, request
from flask import make_response, jsonify

from api.api import api, db
from models.user import User
from schemas.UserSchema import user_schema, users_schema

import datetime


class UserRegistrationResource(Resource):
    def post(self):
        # get the post data
        post_data = request.get_json()
        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()
        if not user:
            try:
                firstName = post_data.get('firstName')
                lastName = post_data.get('lastName')
                email = post_data.get('email')
                username = post_data.get('username')
                password = post_data.get('password')
                user = User(
                    firstName = firstName,
                    lastName = lastName,
                    email = email,
                    username = username
                )
                user.set_password(password)
                user.registered_on = datetime.datetime.now()
                user.admin = False

                # insert the user
                db.session.add(user)
                db.session.commit()
                # generate the auth token
                auth_token = user.encode_auth_token(user.id)
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully registered.',
                    'auth_token': auth_token.decode()
                }
                return make_response(jsonify(responseObject)), 201
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': 'Some error occurred. Please try again.'
                }
                return make_response(jsonify(responseObject)), 401
        else:
            responseObject = {
                'status': 'fail',
                'message': 'User already exists. Please Log in.',
            }
            return make_response(jsonify(responseObject)), 202

api.add_resource(UserRegistrationResource, '/auth/register')
