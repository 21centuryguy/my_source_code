from bottle import route, run

@route('/hello')
def hello():
    return "Hello World!<br>(hosting by bottle)"

# run(host='localhost', port=8080, debug=True)
run(host='172.20.10.2', port=8080, debug=True)
