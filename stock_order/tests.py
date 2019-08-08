import json

from django.test import TestCase
from drf_user.models import User
from rest_framework.test import APIClient

from school.models import School


class TestStockOrder(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="lohitbura",
                                       mobile="9729018415",
                                       email="lohitbura@gmail.com")
        cls.school = School.objects.create(name="MPPS", longitude="27.2323232",
                                           lat="72.324234",
                                           address="Kurukshetra",
                                           created_by=cls.user)
        cls.register = User.objects.create(username="klaus", name="Niklaus",
                                           email="lohit1216230@jmit.ac.in",
                                           mobile="7015363438",
                                           password="pbkdf2_sha256$150000$yDiDfYSGMrOj$2GUA98z75VWb2W"
                                                    "i7NMsGQqjb0/p6hQlx05Yj/tfCKME=")

    def test_api(self):
        client = APIClient()
        my_user = User.objects.last()
        my_user.is_active = True
        my_user.save()

        response = client.post('/api/user/login/', data=json.dumps(
            {'username': 'klaus', 'password': 'klaus@123'}),
                               content_type='application/json')
        assert response.status_code == 200
        token_data = json.loads(response.content.decode("utf-8"))["token"]
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token_data)

        data = {'school': self.school.id}

        response = client.post('/api/stockOrder/indentRequest/',
                               json.dumps(data),
                               content_type='application/json')
        assert response.status_code == 201
        request = client.get('/api/stockOrder/indentRequest/')

        assert request.status_code == 200
