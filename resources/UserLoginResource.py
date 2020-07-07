from flask_restful import Resource, request
from flask import make_response, jsonify

from api.api import api, db
from models.user import User
from schemas.UserSchema import user_schema, users_schema


class UserLoginResource(Resource):
    def post(self):
        # get the post data
        post_data = request.get_json()
        try:
            # fetch the user data
            user = User.query.filter_by(
                username=post_data.get('username')
              ).first()
            user.check_password(post_data.get('password'))
            auth_token = user.encode_auth_token(user.id)
            if auth_token:
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged in.',
                    'auth_token': auth_token.decode(),
                    'uid': user.id
                }
                return make_response(jsonify(responseObject), 200)
        except Exception as e:
            print(e)
            responseObject = {
                'status': 'fail',
                'message': 'Try again'
            }
            return make_response(jsonify(responseObject), 500)

api.add_resource(UserLoginResource, '/auth/login')
