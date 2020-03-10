from DateComparer import DateComparer
from datetime import datetime, timedelta
import unittest

now = datetime.now()
now_plus_20d = now + timedelta(days=20)

unittest.TestCase().assertTrue(DateComparer().is_equal(now, now))
unittest.TestCase().assertFalse(DateComparer().is_equal(now, now_plus_20d))
