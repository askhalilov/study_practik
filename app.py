from __future__ import annotations

import os
import time
from pathlib import Path
from werkzeug.utils import secure_filename
from flask import Flask, jsonify, render_template, request

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif", "zip", "docx"}


def create_app(testing: bool = False) -> Flask:
    app = Flask(__name__)
    app.config.update(
        TESTING=testing,
        MAX_CONTENT_LENGTH=10 * 1024 * 1024,  # 10 MB
        UPLOAD_FOLDER=str(UPLOAD_DIR),
    )
    UPLOAD_DIR.mkdir(exist_ok=True)

    @app.get("/")
    def index():
        return render_template("index.html")

    @app.post("/upload")
    def upload():
        file = request.files.get("file")

        if file is None or file.filename == "":
            return jsonify({"success": False, "message": "Файл не выбран"}), 400

        filename = secure_filename(file.filename)
        extension = filename.rsplit(".", 1)[-1].lower() if "." in filename else ""

        if extension not in ALLOWED_EXTENSIONS:
            return jsonify({"success": False, "message": "Этот тип файла не поддерживается"}), 400

        if not app.config["TESTING"]:
            time.sleep(2)  # имитация обработки файла, чтобы была видна анимация

        save_path = Path(app.config["UPLOAD_FOLDER"]) / filename
        file.save(save_path)

        return jsonify({
            "success": True,
            "message": f"Файл {filename} успешно загружен",
            "filename": filename,
        })

    return app


app = create_app(testing=os.getenv("FLASK_TESTING") == "1")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
