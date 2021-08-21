def test_info(client):
    response = client.get('/')
    result = response.get_json()
    assert result is not None
    assert "message" in result
    assert result["message"] == "FixxyStudioLineNotifyService"


def test_hello_greets_greetee(client):

    response = client.get("/sendlinenotify")
    result = response.get_json()

    assert response.status_code == 200
    assert result is not None
    assert "message" in result
    assert result['message'].index('ok') > 0
