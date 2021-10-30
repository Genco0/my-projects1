from flask import Flask

app = Flask(__name__) # obje oluşturduk

@app.route('/')  # ilk karşımıza çıkacak sayfayı düzenliyoruz
def hello():
    return "Hello world from Flask!!!"

@app.route('/second')
def second():
    return "bize her yer ankara!!!" # searcha localhost:2000/second yazınca browserde ankarayı göreceğiz

@app.route('/third/subthird')
def third():
    return 'This is the subpage of third page'

@app.route('/fourt/<string:id>')
def forth(id) :
    return f"Id number of this page {id}"







if __name__ == '__main__' :
    app.run(host='0.0.0.0', port= 80)# flask çatısı bu şekilde localhost:2000 de çalışacak
