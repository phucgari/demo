from flask import Flask,render_template
from flask_restful import Resource, Api, reqparse
from mongoengine import *
import json
import mongoengine

app = Flask(__name__)
api = Api(app)
parser= reqparse.RequestParser()
parser.add_argument("name",type=str,location="json")
parser.add_argument("des",type=str,location="json")
parser.add_argument("img",type=str,location="json")
parser.add_argument("link",type=str,location="json")
mongoengine.connect("flask",host="ds133358.mlab.com",port = 33358,username ="admin",password ="admin")

class Game(Document):
    name=StringField()
    des=StringField()
    img=StringField()
    link=StringField()

@app.route('/')
def hello_world():
    return render_template("index.html")


class GameListRes(Resource):
    def get(self):
        return [json.loads(game.to_json()) for game in Game.objects]
    def post(self):
        args=parser.parse_args()
        name=args["name"]
        des=args["des"]
        img=args["img"]
        link=args["link"]
        print(name,des,img,link)
        game=Game(name=name,des=des,img=img,link=link)
        game.save()
        return{"adfadf":"sdfdsf"}
class GameRes(Resource):
    def get(self,game_id):
        return json.loads(Game.objects().with_id(game_id).to_json())
    def delete(self,game_id):
        Game.objects().with_id(game_id).delete()
        return{"code":1,"status":"OK"},200
    def put(self,game_id):
        args=parser.parse_args()
        name=args["name"]
        des=args["des"]
        img=args["img"]
        link=args["link"]
        game=Game.objects().with_id(game_id)
        game.update(set__name=name, set__des=des, set__img=img,set__link=link)

api.add_resource(GameListRes, "/api/game")
api.add_resource(GameRes,"/api/game/<game_id>")


if __name__ == '__main__':
    app.run()