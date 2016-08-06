from flask import Flask,render_template

app = Flask(__name__,static_url_path='')


from mongoengine import *

connect('blog',host='mongodb://langbam.us:khanhdz@ds145395.mlab.com:45395/thuoc')

class Benh(Document):
    name = StringField()
    link = StringField()

listBenh = []
for benh in Benh.objects():
    listBenh.append(benh)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/than')
def than():
    return render_template("button.html",listBenh = listBenh)

@app.route('/panadol.html')
def thuoc():
    return render_template("panadol.html")



@app.route('/1_Mat nao.html')
def a():
    return render_template("1_Mat nao.html")

@app.route('/Berberin.html')
def b():
    return render_template("Berberin.html")

@app.route('/2_Dau long.html')
def c():
    return render_template("2_Dau long.html")

@app.route('/2_Dau tim.html')
def d():
    return render_template("2_Dau tim.html")
@app.route('/Lá Lốt (Đau Nhức Xương Khớp).html')
def e():
    return render_template("Lá Lốt (Đau Nhức Xương Khớp).html")
@app.route('/Vitamin C.html')
def f():
    return render_template("Vitamin C.html")
@app.route('/Chườm Lạnh.html')
def g():
    return render_template("Chườm Lạnh.html")
@app.route('/Aspirin.html')
def h():
    return render_template("Aspirin.html")

if __name__ == '__main__':
    app.run()
