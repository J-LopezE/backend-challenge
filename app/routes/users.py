from flask_restx import Namespace, Resource
from flask import request
from app.services.user_service import UserService
from app.routes.dtos.user_dto import create_user_dtos
from app.exceptions.user_exceptions import DuplicateUserException, UserNotFoundException

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
        try:
            user = service.create(email, username)
            return {"id": user.id, "email": user.email, "username": user.username}, 201
        except DuplicateUserException as e:
            return {"error": str(e)}, 409


@us.route("/<int:id>")
class UserDetail(Resource):
    @us.marshal_with(user_output_model)
    def get(self, id):
        service = UserService()
        try:
            user = service.get_by_id(id)
            return {"id": user.id, "email": user.email, "username": user.username}, 200
        except UserNotFoundException as e:
            return {"error": str(e)}, 404

    @us.expect(user_input_model)
    @us.marshal_with(user_output_model)
    def put(self, id):
        service = UserService()
        body = request.json
        email = body.get("email")
        username = body.get("username")
        try:
            user = service.update(id, email, username)
            return {"id": user.id, "email": user.email, "username": user.username}, 200
        except UserNotFoundException as e:
            return {"error": str(e)}, 404
        except DuplicateUserException as e:
            return {"error": str(e)}, 409

    def delete(self, id):
        service = UserService()
        try:
            service.delete(id)
            return {"message": "User deleted"}, 200
        except UserNotFoundException as e:
            return {"error": str(e)}, 404
