import unittest
from models.consultant import Consultant

class TestConsultant(unittest.TestCase):

    def setUp(self):
        self.consultant = Consultant("John Smith","Director","IT backend architect",550)

    def test_consultant_has_name(self):
        self.assertEqual("John Smith",self.consultant.name)

    def test_consultant_has_role(self):
        self.assertEqual("Director",self.consultant.role)

    def test_consultant_has_summary(self):
        self.assertEqual("IT backend architect",self.consultant.summary)

    def test_consultant_has_day_rate(self):
        self.assertEqual(550,self.consultant.day_rate)