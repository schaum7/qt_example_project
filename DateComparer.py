class DateComparer(object):
    from datetime import datetime

    def is_equal(self, first_date: datetime,
                 second_date: datetime) -> bool:
        return first_date == second_date
