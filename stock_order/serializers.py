from rest_framework import serializers


class IndentSerializer(serializers.ModelSerializer):
    from school.serializers import SchoolSerializer

    school = SchoolSerializer(many=False)

    class Meta:
        from .models import Indent

        model = Indent
        fields = ('id', 'name', 'price', 'num_of_boxes', 'num_of_items',
                  'shipping_from', 'shipping_from_lat', 'shipping_from_long',
                  'school', 'shipped_on', 'received_on')


class IndentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import IndentRequest

        model = IndentRequest
        fields = ('id', 'product', 'quantity', 'school')


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Box

        model = Box
        fields = ('id', 'name', 'box_code', 'female_items', 'male_items',
                  'total_item', 'indent')


class BoxItemSerializer(serializers.ModelSerializer):
    from outlet.serializers import OutletSubProductSerializer

    product = OutletSubProductSerializer(many=False)

    class Meta:
        from .models import BoxItem

        model = BoxItem
        fields = ('id', 'product', 'num_of_item', 'item_scanned', 'box')
