from rest_framework.test import APITestCase
from interno.models.torneos import Torneo


class APITorneoTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/torneos")
        self.assertEqual(len(response.data["result"]), 0)
