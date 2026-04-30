from io import BytesIO

from app import create_app


def test_homepage_loads():
    app = create_app(testing=True)
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert "Загрузка файла" in response.get_data(as_text=True)


def test_upload_requires_file():
    app = create_app(testing=True)
    client = app.test_client()

    response = client.post("/upload", data={})

    assert response.status_code == 400
    assert response.json["success"] is False


def test_upload_file_success(tmp_path):
    app = create_app(testing=True)
    app.config["UPLOAD_FOLDER"] = str(tmp_path)
    client = app.test_client()

    response = client.post(
        "/upload",
        data={"file": (BytesIO(b"hello"), "example.txt")},
        content_type="multipart/form-data",
    )

    assert response.status_code == 200
    assert response.json["success"] is True
    assert (tmp_path / "example.txt").exists()
