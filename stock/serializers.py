from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Stock

        model = Stock.objects.all()
        fields = ('id', 'outlet_product', 'quantity', 'location')
        read_only_fields = fields
