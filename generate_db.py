import csv
import random
from dataclasses import astuple
from typing import Optional, Tuple

from record import Action, Device, Record


class DBSeeder:
    MAX_USER_ID = 1000
    MAX_DATE_ACTIONED = 100000

    @classmethod
    def record_factory(
        cls,
        user_id: Optional[int] = None,
        device: Optional[Device] = None,
        action=Optional[Action],
        date_actioned: Optional[int] = None,
    ) -> Record:
        """
        Factory method to generate single DB record.

        :param user_id: user id
        :type user_id: int
        :param device: device
        :type device: str
        :param action: action
        :type action: Action
        :param date_actioned: when action occurred
        :type date_actioned: int
        :return: database record
        :rtype Record
        """

        if not user_id:
            user_id = random.randint(1, cls.MAX_USER_ID)
        if not device:
            device = random.choice(list(Device))
        if not action:
            action = random.choice(list(Action))
        if not date_actioned:
            date_actioned = random.randint(0, cls.MAX_DATE_ACTIONED)

        return Record(
            user_id=user_id, device=device, action=action, date_actioned=date_actioned
        )

    def create_random_user_records(self) -> Tuple[Record, Record]:
        """
        Creates two records for random user on random device with start and stop actions.

        :return: tuple containing two records
        :rtype: tuple
        """

        user_id = random.randint(1, 1000)
        device = random.choice(list(Device))
        start_time = random.randint(0, 100000)
        end_time = random.randint(0, 1000) + start_time
        return (
            self.record_factory(
                user_id=user_id,
                device=device,
                action=Action.start,
                date_actioned=start_time,
            ),
            self.record_factory(
                user_id=user_id,
                device=device,
                action=Action.end,
                date_actioned=end_time,
            ),
        )

    def seed(self, count: int = 1000):
        """

        :param count: count of record pairs to generate.
        :type count: int
        :return: None
        """

        records = []

        for i in range(count):
            records.extend(self.create_random_user_records())

        records.sort(key=lambda record: record.date_actioned)

        with open("db.csv", "w") as db:
            writer = csv.writer(db)
            for record in records:
                writer.writerow(astuple(record))


if __name__ == "__main__":
    seeder = DBSeeder()
    seeder.seed()
