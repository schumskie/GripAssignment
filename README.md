# Grip Assignment

Assignment for grip interview.

## Description

Assignments are located under `assignments.py`.

Tests are under `tests` folder.

### Possible improvements and Limitations


- `get_users` - If this function is meant to be used often on huge datasets, possible improvement could be to use
  adapted binary search for finding left-most and rightmost record, and then filter everything between.
  In worst case scenario complexity would be a bit worse than it is now `O(N*logN)` but in practice it could perform 
  much better especially in cases where length of desired output is much smaller than whole dataset. 
- `get_playback_time` - Not recognized possible improvements. (Except to throw an Exception for bad data).
- Known limitation for first two functions is that they won't work if input list is **not ordered**. `get_playback_time`
  can not produce reliable results if some user records do not have its pair record (start or end action). It expects
  that data is not miss formatted so to speak.
- `get_user_permissions` - Not recognized possible improvements in terms of optimisation. Possible improvement would be
  to use dataclasses as I did in first two tasks.

## Getting Started

### Dependencies

* Python 3

### Executing program

How to install dependencies:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

How to seed database (CSV file):

```
python generate_db
```

How to run tests (database seeding not required):

```
pytest tests/
```