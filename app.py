from flask import Flask, render_template, request, jsonify
import time


def create_app(testing=False):
    app = Flask(__name__)
    app.config["TESTING"] = testing

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/upload", methods=["POST"])
    def upload():
        file = request.files.get("file")

        if not file:
            return jsonify({
                "success": False,
                "message": "Файл не выбран"
            }), 400

        if not testing:
            time.sleep(1)

        return jsonify({
            "success": True,
            "message": f"Файл {file.filename} успешно загружен"
        })

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)