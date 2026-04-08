def test_get_activities_returns_activity_map(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()

    assert isinstance(activities, dict)
    assert "Chess Club" in activities
    assert "Programming Class" in activities

    for details in activities.values():
        assert "description" in details
        assert "schedule" in details
        assert "max_participants" in details
        assert "participants" in details
        assert isinstance(details["participants"], list)
