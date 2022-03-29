from rest_framework.test import APITestCase
from interno.models.especies_por_fecha import EspeciePorFecha


class APIEspeciePorFechaTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/especiesporfecha')
        self.assertEqual(len(response.data['result']), 0)
