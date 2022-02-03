from assignments import get_user_permissions


def test_existing_user_with_some_available_features_have_right_permissions(
    apps, app_features, user_features
):
    result = get_user_permissions(1, apps, app_features, user_features)
    assert result == {
        "user_id": 1,
        "application_permissions": [
            {"app_id": 1, "features_allowed": [1, 2]},
            {"app_id": 2, "features_allowed": [5]},
            {"app_id": 3, "features_allowed": []},
            {"app_id": 126, "features_allowed": []},
        ],
    }


def test_non_existing_user_have_none_permissions(apps, app_features, user_features):
    result = get_user_permissions(100, apps, app_features, user_features)
    assert result == {
        "user_id": 100,
        "application_permissions": [
            {"app_id": 1, "features_allowed": []},
            {"app_id": 2, "features_allowed": []},
            {"app_id": 3, "features_allowed": []},
            {"app_id": 126, "features_allowed": []},
        ],
    }


def test_existing_user_without_available_features_have_none_permissions(
    apps, app_features, user_features
):
    result = get_user_permissions(3, apps, app_features, user_features)
    assert result == {
        "user_id": 3,
        "application_permissions": [
            {"app_id": 1, "features_allowed": []},
            {"app_id": 2, "features_allowed": []},
            {"app_id": 3, "features_allowed": []},
            {"app_id": 126, "features_allowed": []},
        ],
    }
