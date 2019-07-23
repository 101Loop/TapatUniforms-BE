from rest_framework import serializers


class StockManagerSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    box_code = serializers.CharField()
    outlet = serializers.CharField()
    outlet_product = serializers.CharField()
    outlet_sub_product = serializers.CharField()
    item_count = serializers.IntegerField()