import unittest
from models.assignment import Assignment

class TestAssignment(unittest.TestCase):

    def setUp(self):
        self.assignment = Assignment("Jenny Pink","Tesco",20)

    def test_client_has_consultant(self):
        self.assertEqual("Jenny Pink",self.assignment.consultant)

    def test_client_has_client(self):
        self.assertEqual("Tesco",self.assignment.client)

    def test_client_has_days_required(self):
        self.assertEqual(20,self.assignment.days_required)