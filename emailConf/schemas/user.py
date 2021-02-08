from ma import ma
from models.user import UserModel

# ModelSchema replaced in latest version..
class UserSchema(ma.ModelSchema):
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id", "activated")
