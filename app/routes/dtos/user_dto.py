from flask_restx import fields


def create_user_dtos(ns):
    input_model = ns.model(
        "UserInput",
        {
            "email": fields.String(
                required=True, description="email", example="jorge@mail.com"
            ),
            "username": fields.String(
                required=True, description="username", example="george"
            ),
        },
    )

    output_model = ns.model(
        "UserOutput",
        {
            "id": fields.Integer(description="id_user"),
            "email": fields.String(description="email"),
            "username": fields.String(description="username"),
        },
    )

    return input_model, output_model
