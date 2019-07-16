from django.test import TestCase
from school.models import School
from django.test import Client


class StockOrderTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.school = School.objects.create(name="MPPS", longitude="27.2323232", latitude="72.2323232",
                                           address="Kurukshetra")

    def indent_request_test(self):
        c = Client()
        response = c.post('/api/stock/request/', {"school": self.school})
        print(response)
        print(response.content)

