from rest_framework import serializers
from django.db.models import Q

from .models import Goods, GoodsCategory, GoodsImage, Banner, GoodsCategoryBrand, IndexAd


class GooodsCategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"