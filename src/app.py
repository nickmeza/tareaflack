from flask import Flask
from UsuariDAO import Usuario
app = Flask(__name__)
user=Usuario()
@app.route("/list",methods=['GET'])
def hello():
    print(user.readAll())
    return user.readAll()

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=4000,debug=True)

