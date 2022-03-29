from rest_framework.test import APITestCase
from interno.models.fechas_de_pesca import FechaDePesca


class APIFechaDePescaTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/fechasdepesca")
        self.assertEqual(len(response.data["result"]), 0)
