from flask import Flask

# Auth blueprints
from auth.signup import signup_bp
from auth.login import login_bp
from auth.forget_pass import password_bp

# Syllabus blueprint
from syllabus.routes import syllabus_bp

app = Flask(__name__)

# Register auth blueprints
app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)
app.register_blueprint(password_bp)

# Register syllabus blueprint
app.register_blueprint(syllabus_bp)

# Register context blueprint
from auth.context import context_bp
app.register_blueprint(context_bp)


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
