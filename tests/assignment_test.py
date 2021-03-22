import unittest
from models.assignment import Assignment

class TestAssignment(unittest.TestCase):

    def setUp(self):
        self.assignment = Assignment("Build a web app","Jenny Pink","Tesco",20)

    def test_assignment_has_description(self):
        self.assertEqual("Build a web app",self.assignment.description)    

    def test_assignment_has_consultant(self):
        self.assertEqual("Jenny Pink",self.assignment.consultant)

    def test_assignment_has_client(self):
        self.assertEqual("Tesco",self.assignment.client)

    def test_assignment_has_days_required(self):
        self.assertEqual(20,self.assignment.days_required)