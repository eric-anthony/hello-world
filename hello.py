import os

from flask import Flask, request
app = Flask(__name__)


    
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return "Post: " + str(post_id)
    
@app.route('/login', methods=['GET'])
def login():
    if request.values:
        return 'Username is ' + request.values["username"]
    else:
        return '<form method="get" action="/login"><input type="text" name="username"/><p><button type="submit">Submit</button></form>'
    
    
if __name__ == '__main__':
    host = os.getenv('IP','0.0.0.0')
    port = int(os.getenv('PORT',5000))
    app.debug = True
    app.run(host=host,port=port)

