import unittest
from models.client import Client

class TestClient(unittest.TestCase):

    def setUp(self):
        self.client = Client("CodeClan","IT education","morag_mac@codeclan.com")

    def test_client_has_client_name(self):
        self.assertEqual("CodeClan",self.client.client_name)

    def test_client_has_type_of_business(self):
        self.assertEqual("IT education",self.client.type_of_business)

    def test_client_has_contact_details(self):
        self.assertEqual("morag_mac@codeclan.com",self.client.contact_details)