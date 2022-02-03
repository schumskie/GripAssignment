from assignments import (get_playback_time, get_user_permissions, get_users,
                         load_records)
from record import Action

if __name__ == "__main__":
    # task 1
    db_records = load_records()
    print(get_users(db_records, Action.start, start_time=0, end_time=10000))

    # task 2
    print(get_playback_time(517, db_records))

    # task 6
    apps = [{"app_id": 1}, {"app_id": 2}, {"app_id": 3}, {"app_id": 126}]
    app_features = [
        {"app_id": 1, "features_available": [1, 2, 3]},
        {"app_id": 2, "features_available": [3, 4, 5, 7]},
        {"app_id": 3, "features_available": [3, 12]},
    ]
    user_features = [
        {"user_id": 1, "features_allowed": [1, 2, 5]},
        {"user_id": 2, "features_allowed": [1, 2, 3, 4]},
        {"user_id": 3, "features_allowed": []},
    ]
    print(get_user_permissions(1, apps, app_features, user_features))
