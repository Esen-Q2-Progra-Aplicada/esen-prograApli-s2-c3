from flask_restful import Resource, reqparse
from logic.video_logic import VideoLogic


class Video(Resource):
    def __init__(self):
        self.video_put_args = self.createParser()

    def createParser(self):
        args = reqparse.RequestParser()
        args.add_argument("name", type=str, help="name of the video")
        args.add_argument("views", type=int, help="views of the video")
        args.add_argument("likes", type=int, help="likes of the video")
        return args

    def get(self, id):
        logic = VideoLogic()
        result = logic.getVideoById(id)
        if len(result) == 0:
            return {}
        return result[0], 200

    def put(self, id):
        video = self.video_put_args.parse_args()
        logic = VideoLogic()
        rows = logic.insertVideo(video)
        return {"rowsAffected": rows}, 200

    def patch(self, id):
        video = self.video_put_args.parse_args()
        logic = VideoLogic()
        rows = logic.updateVideo(id, video)
        return {"rowsAffected": rows}, 200

    def delete(self, id):
        logic = VideoLogic()
        rows = logic.deleteVideo(id)
        return {"rowsAffected": rows}, 200
