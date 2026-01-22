from flask import Flask

from auth.signup import signup_bp

from auth.login import login_bp

from auth.forget_pass import password_bp



app = Flask(__name__)



app.register_blueprint(signup_bp)

app.register_blueprint(login_bp)

app.register_blueprint(password_bp)



if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0',port=5000)
    #fhdddddddddd