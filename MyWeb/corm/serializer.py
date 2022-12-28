from rest_framework import serializers
from corm.models import Report, Category


class CategorySerializer(serializers.ModelSerializer):
    owner_len = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"

    def get_owner_len(self, object):
        return len(object.owner)

    def validate(self, data):
        if len(data['name']) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return data

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        else:
            return value


class ReportSerializer(serializers.Serializer):
    name = serializers.CharField()
    ref_table = serializers.CharField()
    # category = serializers.CharField()
    category = CategorySerializer()
    active = serializers.BooleanField()
    modified = serializers.DateTimeField(format="%Y-%m-%d")

    # for save()
    def create(self, data):
        print(data)
        category = data.get("category").get("name")
        c = Category.objects.get(pk=category)
        data['category'] = c
        print(data)
        return Report.objects.create(**data)
