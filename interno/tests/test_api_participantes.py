from rest_framework.test import APITestCase
from interno.models.participantes import Participante


class APIParticipanteTestCase(APITestCase):
    def setUp(self):
        pass

    def test_puede_listar(self):
        response = self.client.get('/api/participantes')
        self.assertEqual(len(response.data['result']), 0)
