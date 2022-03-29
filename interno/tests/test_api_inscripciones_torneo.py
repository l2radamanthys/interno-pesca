from rest_framework.test import APITestCase
from interno.models.inscripciones_torneo import InscripcionTorne


class APIInscripcionTorneTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/inscripcionestorneo')
        self.assertEqual(len(response.data['result']), 0)
