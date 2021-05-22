from flask import Flask

server = Flask(__name__)

@server.route("/")
 def hello():
    return "Hello World!"

@server.route("/version")
 def version():
   f = open("version.txt", "r")
   return f.read()

if __name__ == "__main__":
   server.run(host='0.0.0.0')