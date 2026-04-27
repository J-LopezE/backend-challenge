from flask_restx import Namespace, Resource, fields
from flask import request
from app.services.user_service import UserService
from app.routes.dtos.user_dto import create_user_dtos

us = Namespace("users", description="User management endpoints")
user_input_model, user_output_model = create_user_dtos(us)
@us.route("/")
class UserList(Resource):
    @us.marshal_with(user_output_model)       
    def get(self):
        service = UserService()
        users = service.get_all()
        return [{"id": u.id, "email": u.email, "username": u.username} for u in users]
    @us.expect(user_input_model)
    @us.marshal_with(user_output_model)
    def post(self):
        service = UserService()
        body = request.json          
        email = body.get("email")
        username = body.get("username")
        if not email or not username:
            return {"error": "email and username are required"}, 400
        user = service.create(email, username)
        return {"id": user.id, "email": user.email, "username": user.username},201
    
@us.route("/<int:id>")
class UserDetail(Resource):
    @us.marshal_with(user_output_model)
    def get(self,id):
        service = UserService()
        user =service.get_by_id(id)
        if not user:
           return {"error": "User not found"}, 404
        return {"id": user.id, "email": user.email, "username": user.username}
    @us.expect(user_input_model)   
    @us.marshal_with(user_output_model)
    def put(self,id):
        service = UserService()
        user = service.get_by_id(id)
        if not user:
            return {"error": "User not found"}, 404
        body = request.json
        email = body.get("email")
        if email is not None and email == "":
            return {"error": "email cannot be empty"}, 400
        username = body.get("username")
        if username is not None and username == "":
            return {"error": "username cannot be empty"}, 400
        user = service.update(id, email, username)
        return {"id": user.id, "email": user.email, "username": user.username}
       
        
    def delete(self,id):
        service = UserService()
        user =service.get_by_id(id)
        if not user:
           return {"error": "User not found"}, 404
        service.delete(id)
        return {"message": "User deleted"}, 200