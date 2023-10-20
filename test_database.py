import unittest
from io import StringIO
import sys
import database as app

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = app.Database()
        self.saved_stdout = sys.stdout
        sys.stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_set_and_get(self):
        self.db.set("A", 10)
        self.assertEqual(self.db.get("A"), 10)

    def test_unset(self):
        self.db.set("B", 20)
        self.db.unset("B")
        self.assertEqual(self.db.get("B"), "NULL")

    def test_counts(self):
        self.db.set("A", 10)
        self.db.set("C", 10)
        self.assertEqual(self.db.count(10), 2)

    def test_find(self):
        self.db.set("A", 10)
        self.db.set("B", 20)
        self.db.set("C", 10)
        self.assertEqual(self.db.find(10), "A C")

    def test_nested_transactions(self):
        self.db.set("A", 10)
        self.db.begin()
        self.db.set("A", 20)
        self.db.begin()
        self.db.set("A", 30)
        self.assertEqual(self.db.get("A"), 30)
        self.db.rollback()
        self.assertEqual(self.db.get("A"), 20)
        self.db.commit()
        self.assertEqual(self.db.get("A"), 20)


if __name__ == '__main__':
    unittest.main()
