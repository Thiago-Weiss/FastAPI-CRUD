import pytest

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

autenticacao = None
user_id = None
created_blog_id = None


@pytest.mark.order(1)
def test_create_user(client):
    global user_id
    response = client.post("/user", json= USER_DATA)
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == USER_DATA["name"]
    assert data["email"] == USER_DATA["email"]
    assert  isinstance(data["id"], int)
    user_id = data["id"]




@pytest.mark.order(2)
def test_login(client):
    global autenticacao
    login_data = {"username": USER_DATA["email"], "password": USER_DATA["password"]}
    response = client.post("/login", data=login_data)
    assert response.status_code == 200
    token = response.json()["access_token"]
    autenticacao = {"Authorization": f"Bearer {token}"}


@pytest.mark.order(3)
def test_post_blog(client):
    global created_blog_id
    response = client.post("/post/", json=BLOG_DATA, headers= autenticacao)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == BLOG_DATA["title"]
    assert data["content"] == BLOG_DATA["content"]
    assert "id" in data
    created_blog_id = data["id"] 



@pytest.mark.order(4)
def test_get_all_blogs(client):
    response = client.get("/post/", headers= autenticacao)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(blog["id"] == created_blog_id for blog in data)


@pytest.mark.order(5)
def test_get_blog_id(client):
    response = client.get(f"/post/{created_blog_id}", headers= autenticacao)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == BLOG_DATA["title"]
    assert data["content"] == BLOG_DATA["content"]
    assert data["id"] == created_blog_id
    assert data["autor"] == {"name": USER_DATA["name"], "email": USER_DATA["email"], "id": user_id}


@pytest.mark.order(6)
def test_update_blog(client):
    response = client.patch(f"/post/{created_blog_id}", json=BLOG_DATA_ATT, headers= autenticacao)
    assert response.status_code == 202
    data = response.json()
    assert data["title"] == BLOG_DATA_ATT["title"]

@pytest.mark.order(7)
def test_get_blog_id_2(client):
    response = client.get(f"/post/{created_blog_id}", headers= autenticacao)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == BLOG_DATA_ATT["title"]
    assert data["content"] == BLOG_DATA_ATT["content"]
    assert data["id"] == created_blog_id
    assert data["autor"] == {"name": USER_DATA["name"], "email": USER_DATA["email"], "id": user_id}



@pytest.mark.order(8)
def test_delete_blog(client):
    response = client.delete(f"/post/{created_blog_id}", headers= autenticacao)
    assert response.status_code == 204
    response = client.get(f"/post/{created_blog_id}", headers= autenticacao)
    assert response.status_code == 404
