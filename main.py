from assignments import get_users, load_records, get_playback_time
from record import Action

if __name__ == "__main__":
    db_records = load_records()
    print(get_users(db_records, Action.start, start_time=0, end_time=10000))
    print(get_playback_time(517, db_records))