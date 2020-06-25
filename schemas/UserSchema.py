from api.api import ma

class UserSchema(ma.Schema):
    class Meta:
        fields = ("id", "username", "email")

user_schema = UserSchema()
users_schema = UserSchema(many=True)