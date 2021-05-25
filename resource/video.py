from flask_restful import Resource


class Video(Resource):
    def get(self, id):
        return {"data": id}, 200

    def put(self, id):
        return {"data": id}, 200

    def patch(self, id):
        return {"data": id}, 200

    def delete(self, id):
        return {"data": id}, 200
