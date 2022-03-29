from rest_framework.test import APITestCase
from interno.models.especies_resultados import EspecieResultado


class APIEspecieResultadoTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/especiesresultados")
        self.assertEqual(len(response.data["result"]), 0)
