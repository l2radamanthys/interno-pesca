from rest_framework.test import APITestCase
from interno.models.resultados_fecha import ResultadoFecha


class APIResultadoFechaTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get("/api/resultadosfecha")
        self.assertEqual(len(response.data["result"]), 0)
