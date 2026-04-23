from  flask_restx import Namespace, Resource

ns = Namespace("health", description="Health check endpoints")
@ns.route("/")
class HealthResource (Resource):
    def get(self):
        return {"status": "ok"}

