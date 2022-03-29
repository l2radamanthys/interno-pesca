from rest_framework.test import APITestCase
from interno.models.especies import Especie


class APIEspecieTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/especies')
        self.assertEqual(len(response.data['result']), 0)
