import json

def test_create_job(client):
    data = {
        "title": "FastAPI",
        "company": "McTech",
        "company_url": "https://mctech.tg",
        "location": "TOGO, Lomé",
        "description": "Test",
        "date_posted": "2021-10-18"

    }
    response = client.post("/job/create_job", json.dumps(data))
    assert response.status_code == 200