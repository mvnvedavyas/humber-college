from flask import Blueprint, jsonify

app_routes = Blueprint("app_routes", __name__)


@app_routes.route("/api")
def changeroute():
    return "Goodbye, World!"


@app_routes.route("/api/backup")
def backup():
    # Get data from firebase send to database
    return {"status": "success"}
