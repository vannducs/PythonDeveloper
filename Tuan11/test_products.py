from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_product_flow():
#create
    create_response = client.post(
        "/products/1",
        params={
            "name": "iPhone 15"
        }
    )

    assert create_response.status_code == 200

    create_data = create_response.json()

    assert create_data["id"] == 1
    assert create_data["name"] == "iPhone 15"


#get

    get_response = client.get("/products/1")

    assert get_response.status_code == 200

    get_data = get_response.json()

    assert get_data["name"] == "iPhone 15"


    delete_response = client.delete("/products/1")

    assert delete_response.status_code == 200

#ktra lại xem xóa xong thì có trả 404 ko
    get_again_response = client.get("/products/1")
    assert get_again_response.status_code == 404