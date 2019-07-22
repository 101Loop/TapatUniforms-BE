from rest_framework import serializers


class IndentSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Indent

        model = Indent
        fields = ('id', 'name', 'num_of_boxes', 'shipping_from',
                  'shipping_to', 'shipping_from_lat', 'shipping_from_long',
                  'indent_request')


class IndentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import IndentRequest
        model = IndentRequest
        fields = ('id', 'school')


class IndentRequestDetailSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import IndentRequestDetail
        model = IndentRequestDetail
        fields = ('id', 'product', 'quantity', 'indent_request')


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import Box
        model = Box
        fields = ('id', 'name', 'box_code', 'female_items', 'male_items',
                  'total_item', 'indent')


class BoxItemSerializer(serializers.ModelSerializer):
    class Meta:
        from .models import BoxItem
        model = BoxItem
        fields = ('id', 'product', 'num_of_item', 'item_scanned',
                  'box')
