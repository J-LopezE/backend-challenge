from flask_restx import Namespace, Resource, fields
from flask import request
from app.models import db, User

us = Namespace("users", description="User management endpoints")
user_model = us.model("User", {
    "email":    fields.String(required=True, description="User email"),
    "username": fields.String(required=True, description="Username"),
})
@us.route("/")
class UserList(Resource):
    def get(self):
        users = User.query.all()
        return [{"id": u.id, "email": u.email, "username": u.username} for u in users]
    @us.expect(user_model)
    def post(self):
        body = request.json
        email = body.get("email", None)
        username = body.get("username", None)
        if not email or not username:
            return {"error": "email and username are required"}, 400
        
        new_user = User(email=email, username=username)
        db.session.add(new_user)
        db.session.commit()
        return {"id": new_user.id, "email": new_user.email, "username": new_user.username},201
    
@us.route("/<int:id>")
class UserDetail(Resource):
    def get(self,id):
        user =User.query.get(id)
        if not user:
           return {"error": "User not found"}, 404
        return {"id": user.id, "email": user.email, "username": user.username}
       
    @us.expect(user_model)
    def put(self,id):
        user = User.query.get(id)
        if not user:
            return {"error": "User not found"}, 404
        body = request.json
        email = body.get("email")
        if email is not None and email == "":
            return {"error": "email cannot be empty"}, 400
        if email:
            user.email = email
        username = body.get("username")
        if username is not None and username == "":
            return {"error": "username cannot be empty"}, 400
        if username:
            user.username = username
        user.email = body.get("email")
        user.username = body.get("username")
        db.session.commit()
        return {"id": user.id, "email": user.email, "username": user.username}
       
        
    def delete(self,id):
        user =User.query.get(id)
        if not user:
           return {"error": "User not found"}, 404
        db.session.delete(user)
        db.session.commit()
        return {"message": "User deleted"}, 200