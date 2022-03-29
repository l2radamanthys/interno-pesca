from rest_framework.test import APITestCase
from interno.models.categorias import Categoria


class APICategoriaTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/categorias')
        self.assertEqual(len(response.data['result']), 0)
