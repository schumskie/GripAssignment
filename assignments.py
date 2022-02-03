import csv
from typing import List

from record import Action, Record


def load_records(filename: str = "db.csv"):
    """
    Load records from CSV.

    :param filename: CSV filename
    :type filename: str
    :return: records from CSV
    :rtype: list[Record]
    """

    records = []
    with open(filename) as db:
        reader = csv.reader(db)
        for row in reader:
            user_id, device, action, date_actioned = row
            user_id = int(user_id)
            date_actioned = int(date_actioned)
            records.append(Record(user_id, device, action, date_actioned))

    return records


def get_users(records: List[Record], action: Action, start_time: int, end_time: int):
    """
    Returns the list of user ids (unordered) for given action,
    where action occurred between start_time and end_time (inclusive).

    :param records: List of database records
    :type records: list[Record]
    :param action: User action
    :type action: Action
    :param start_time:
    :type start_time: int
    :param end_time:
    :type end_time: int
    :return: List of unique user_ids
    :rtype: list[int]
    """

    user_ids = set()
    for record in records:
        if record.action == action and start_time <= record.date_actioned <= end_time:
            user_ids.add(record.user_id)

    return list(user_ids)


def get_playback_time(user_id: int, records: List[Record]) -> int:
    """
    Returns total “unique” playback time in seconds. Takes in a user_id and an array of all the database
    records.

    :param user_id: user id
    :type user_id: int
    :param records: list of database records
    :type records: list[Record]
    :return: Unique playback time in seconds.
    :rtype: int
    """
    total = 0
    stack = []

    for record in records:
        if record.user_id != user_id:
            continue

        if record.action == Action.start:
            stack.append(record.date_actioned)
            continue

        last = stack.pop()
        if len(stack) == 0:
            total += record.date_actioned - last

    return total


def get_user_permissions(
    user_id: int, apps: List[dict], app_features: List[dict], user_features: list[dict]
) -> dict:
    """
    Returns the list of permissions for a given user.

    :param user_id: id of user.
    :param apps: list of available user apps.
    :param app_features: list of available application features
    :param user_features: list of features provided to the user
    :return: User permissions.
    """
    # normalize data
    app_features_map = {
        record["app_id"]: set(record["features_available"]) for record in app_features
    }
    user_features_map = {
        record["user_id"]: set(record["features_allowed"]) for record in user_features
    }
    permissions = []
    for app in apps:
        features_allowed = []
        app_id = app["app_id"]
        if app_id in app_features_map and user_id in user_features_map:
            features_allowed = sorted(
                app_features_map[app_id].intersection(user_features_map[user_id])
            )
        permissions.append(
            {"app_id": app_id, "features_allowed": features_allowed}
        )
    return {"user_id": user_id, "application_permissions": permissions}
