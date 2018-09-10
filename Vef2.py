#from sys import argv

from bottle import *

@route("/")
def index():
    return """
    <h2>Verkefni 2</h2>
    <a href="/a">Liður A</a>
    <a href="/b">Liður B</a>
    """

@route("/a")
def a():
    return """ 
        <h2>Verkefni 2 Liður A</h2>
        <a href = "/sida/1">Síða 1.</a> 
        <a href = "/sida/2">Síða 2.</a>  
        <a href = "/sida/3">Síða 3.</a>  
    """

@route("/sida/<id>")
def page(id):
    if id == '1':
        return "Þetta er síða 1<br><a href = '/a'><Til baka</a>"
    if id == '2':
        return "Þetta er síða 2<br><a href = '/a'><Til baka</a>"
    if id == '3':
        return "Þetta er síða 3<br><a href = '/a'><Til baka</a>"
    else:
        abort(404,"<h2 style = 'color red'>þessi Síða finnst ekki")


@route("/b")
def b():
    return """ 
        <h2>Verkefni 2 Liður B</h2>
        <h4>Veldu uppáhalds bókstafinn þinn</h4>
        <a href ="/sida2?bokstafur=a<img src = 'myndir2/A'.jpg></a>
        <a href ="/sida2?bokstafur=b<img src = 'myndir2/B'.jpg></a>
        <a href ="/sida2?bokstafur=c<img src = 'myndir2/C'.jpg></a>
        <a href ="/sida2?bokstafur=d<img src = 'myndir2/D'.jpg></a>
        """
    

@route("/sida2")
def page():
    l = request.query.bokstafur
    if l == 'a':
        return"<h3>Minn uppáhalds bókstafur er:</h3><img src = 'myndir2/A'.jpg>"
    if l == 'b':
        return"<h3>Minn uppáhalds bókstafur er:</h3><img src = 'myndir2/B'.jpg>"
    if l == 'c':
        return"<h3>Minn uppáhalds bókstafur er:</h3><img src = 'myndir2/C'.png>"
    if l == 'd':
        return"<h3>Minn uppáhalds bókstafur er:</h3><img src = 'myndir2/D'.png>"


@route('/myndir2/<skra>')
def static_skra(skra):
    return static_file(skra, root='myndir2')







@error(404)
def villa(error):
    return "<h2 style = color:red>Þessi síða finnst ekki</h2>"



run(host = 'localhost',port= 8080, reloader=True, debug=True)




















#run(host='localhost', port=5000)
