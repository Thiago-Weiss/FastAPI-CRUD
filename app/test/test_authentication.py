import pytest

INVALID_AUTH = {"Authorization": "Bearer token_invalido"}
USER_DATA = {
        "name": "thiago",
        "email": "thiago@example.com",
        "password": "senha do thiago"
    }


BLOG_DATA = {
    "title": "Teste blog",
    "content": "Conteúdo de teste",
}
BLOG_DATA_ATT = {
    "title": "Teste blog",
    "content": "Conteúdo de teste"
}


created_blog_id = None


@pytest.mark.order(101)
def test_post_blog_no_auth(client):
    response = client.post("/post/", json=BLOG_DATA)
    assert response.status_code == 401

@pytest.mark.order(102)
def test_post_blog_invalid_token(client):
    response = client.post("/post/", json=BLOG_DATA, headers=INVALID_AUTH)
    assert response.status_code == 401

@pytest.mark.order(103)
def test_get_all_blogs_no_auth(client):
    response = client.get("/post/")
    assert response.status_code == 401

@pytest.mark.order(104)
def test_get_all_blogs_invalid_token(client):
    response = client.get("/post/", headers=INVALID_AUTH)
    assert response.status_code == 401

@pytest.mark.order(105)
def test_get_blog_id_no_auth(client):
    response = client.get(f"/post/{created_blog_id}")
    assert response.status_code == 401

@pytest.mark.order(106)
def test_get_blog_id_invalid_token(client):
    response = client.get(f"/post/{created_blog_id}", headers=INVALID_AUTH)
    assert response.status_code == 401

@pytest.mark.order(107)
def test_update_blog_no_auth(client):
    response = client.patch(f"/post/{created_blog_id}", json=BLOG_DATA_ATT)
    assert response.status_code == 401

@pytest.mark.order(108)
def test_update_blog_invalid_token(client):
    response = client.patch(f"/post/{created_blog_id}", json=BLOG_DATA_ATT, headers=INVALID_AUTH)
    assert response.status_code == 401

@pytest.mark.order(109)
def test_delete_blog_no_auth(client):
    response = client.delete(f"/post/{created_blog_id}")
    assert response.status_code == 401

@pytest.mark.order(110)
def test_delete_blog_invalid_token(client):
    response = client.delete(f"/post/{created_blog_id}", headers=INVALID_AUTH)
    assert response.status_code == 401
