from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route("/demo")
def demo():
    return render_template("demo.html")
@app.route("/school")
def school():
    return redirect("http://techkids.vn")
@app.route("/bmi/<int:weight>/<int:height>")
def bmi(weight,height):
    a=weight/(height*height)*10000
    if a < 16:
        b = "Serevely underweight"
    elif a <= 18.5:
        b = "Underweight"
    elif a <= 25:
        b = "Normal"
    elif a <= 30:
        b = "Overweight"
    else:
        b = "Obese"
    return "bmi={0},{1}".format(a,b)
if __name__ == '__main__':
    app.run()
