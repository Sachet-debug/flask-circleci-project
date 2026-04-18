from flask import Flask, jsonify
import yaml
import os

app = Flask(__name__)

# Load config from YAML document
config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
with open(config_path, "r") as f:
    config = yaml.safe_load(f)

@app.route("/")
def home():
    return jsonify({
        "message": config["app"]["message"],
        "version": config["app"]["version"],
        "author": config["app"]["author"],
        "environment": config["app"]["environment"]
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

@app.route("/config")
def show_config():
    return jsonify({
        "version": config["app"]["version"],
        "environment": config["app"]["environment"],
        "server_port": config["server"]["port"]
    })

if __name__ == "__main__":
    port = config["server"]["port"]
    debug = config["server"]["debug"]
    app.run(host="0.0.0.0", port=port, debug=debug)