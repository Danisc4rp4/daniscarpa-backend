from flask_restful import Resource, request
from models.user import User
from api.api import api, db
from schemas.UserSchema import user_schema, users_schema

class UserResource(Resource):
    def get(self, user_id=False):
        if user_id:
            user = User.query.get_or_404(user_id)
            return user_schema.dump(user)
        users = User.query.all()
        return users_schema.dump(users)

    def post(self):
        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')
        user = User.query.filter_by(username = username).first()
        if user:
            check_password = user.check_password(password)
            if check_password:
                return True
            return False
        new_user = User(
            username = username,
            email = email
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        return user_schema.dump(new_user)

api.add_resource(UserResource, '/login', '/register', '/users', '/user/<int:user_id>')
