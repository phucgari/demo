from flask import Flask,render_template,request
import mongoengine
from mongoengine import *
app = Flask(__name__)
#mongodb://<dbuser>:<dbpassword>@ds133358.mlab.com:33358/flask
host = "ds133358.mlab.com"
port = 33358
db_name = "flask"
user_name = "admin"
password = "admin"
mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

class User(Document):
    name= StringField()
    des= StringField()
    img= StringField()
    link= StringField()

@app.route('/')
def hello_world():
    return render_template("intro.html")
@app.route("/game")
def hobby():
    game=[
        {
            "name":"League of Legend",
            "des":"A very famous MOBA game - most played pc game right now with 100 million players a month",
            "img":"http://www.legalsportsreport.com/wp-content/uploads/2015/02/LeagueofLegends-600x400.jpg",
            "link":"https://lienminh.garena.vn/"
        },
        {
            "name":"Hearthstone",
            "des":"A A fast-paced strategy card game for everyone - more than 50 million players log in per month",
            "img":"http://sohanews.sohacdn.com/thumb_w/600/2016/1-sau-co-vay-va-starcraft-den-luot-hearthstone-tro-thanh-muc-tieu-de-may-tinh-danh-bai-loai-nguoi-1459278008494-0-41-360-581-crop-1459278077832.jpg",
            "link":"http://us.battle.net/hearthstone/en/"
        },
        {
            "name":"Overwatch",
            "des":" first-person shooter with unique, creative characters like superman",
            "img":"http://image1.redbull.com/rbcom/010/2015-11-16/1331759970098_2/0010/1/600/400/2/overwatch-is-the-new-esports-shooter-game-from-blizzard.jpg",
            "link":"https://playoverwatch.com/"
        },
        {
            "name":"Dota2",
            "des":"Another very good game with an impressive number of player - most played on steam ",
            "img":"http://wlp.ninja/wallpaper/Dota-2-wallpaper-1920x1080-07-600x400.jpg",
            "link":"http://blog.dota2.com/"
        }

    ]
    return render_template("game.html",game_list=game)
@app.route("/addgame", methods=["GET","POST"])
def adding():
    if request.method=="GET":
        return render_template("adding.html")
    elif request.method=="POST":
        namex=request.form["name"]
        desx=request.form["des"]
        imgx=request.form["img"]
        linkx=request.form["link"]
        game=User(name=namex, img=imgx ,des=desx,link=linkx)
        game.save()
        return "thank for your add"

if __name__ == '__main__':
    app.run()
