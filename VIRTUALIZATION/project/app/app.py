import os
from flask import Flask
from flask import send_from_directory
from backend.routes import app_routes

app = Flask(__name__, static_folder="./frontend/build", static_url_path="/")
app.register_blueprint(app_routes)


# Static React App
@app.route("/")
def serve():
    return send_from_directory(app.static_folder, "index.html")


ENV_DEBUG = os.environ.get("APP_DEBUG", True)
ENV_PORT = os.environ.get("APP_PORT", 5174)

if __name__ == "__main__":
    app.run(
        use_reloader=ENV_DEBUG,
        host="0.0.0.0",
        port=ENV_PORT,
        debug=ENV_DEBUG,
        threaded=True,
    )
