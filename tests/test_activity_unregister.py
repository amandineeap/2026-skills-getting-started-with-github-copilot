def test_unregister_success_removes_participant(client):
    email = "daniel@mergington.edu"

    response = client.delete("/activities/Chess Club/signup", params={"email": email})

    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from Chess Club"

    activities = client.get("/activities").json()
    assert email not in activities["Chess Club"]["participants"]


def test_unregister_rejects_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_rejects_unknown_participant(client):
    response = client.delete(
        "/activities/Chess Club/signup",
        params={"email": "not-enrolled@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"


def test_signup_then_unregister_flow(client):
    email = "temp-student@mergington.edu"

    signup_response = client.post("/activities/Robotics Team/signup", params={"email": email})
    assert signup_response.status_code == 200

    unregister_response = client.delete("/activities/Robotics Team/signup", params={"email": email})
    assert unregister_response.status_code == 200

    activities = client.get("/activities").json()
    assert email not in activities["Robotics Team"]["participants"]
