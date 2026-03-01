import os
from flask import Flask
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY") or "secret_for_team_project"
# Auth blueprints
from auth.signup import signup_bp
from auth.login import login_bp
from auth.forget_pass import password_bp
# Syllabus blueprint
from syllabus.routes import syllabus_bp
#timer blueprint
from session_tracker.services.timer_routes import study_timer_bp
# Register auth blueprints
app.register_blueprint(signup_bp)
app.register_blueprint(login_bp)
app.register_blueprint(password_bp)
# Register syllabus blueprint
app.register_blueprint(syllabus_bp)
# Register context blueprint
from auth.context import context_bp
app.register_blueprint(context_bp)
#Register timer blueprint
app.register_blueprint(study_timer_bp)
#Register ct avg blueprint
from ct_average.ct_routes import ct_bp
app.register_blueprint(ct_bp)
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )
