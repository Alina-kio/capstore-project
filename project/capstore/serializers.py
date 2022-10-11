from capstore.models import *
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class PopularBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularBrand
        fields = 'id title'.split()


class ProductSerializer(serializers.ModelSerializer):
    brand = PopularBrandSerializer()

    class Meta:
        model = Product
        fields = 'id title brand original_price discount_price'.split()

class BrandValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)

    def validate_name(self, name):
        products = PopularBrand.objects.filter(title=name)
        if products.count() > 0:
            raise ValidationError('Brand must be unique!')
        return name


class ProductValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)
    brand_id = serializers.IntegerField(min_value=1)
    original_price = serializers.FloatField(min_value=0.1)
    discount_price = serializers.IntegerField(default=0)

    def validate_category_id(self, brand_id):  # 100
        try:
            PopularBrand.objects.get(id=brand_id)
        except PopularBrand.DoesNotExist:
            raise ValidationError('Popular does not exists!')
        return brand_id

    def validate_name(self, name):
        products = Product.objects.filter(title=name)
        if products.count() > 0:
            raise ValidationError('Product must be unique!')
        return name


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title brand original_price discount_price size description is_best_seller is_favorite'.split()


class BestsellerSerializer(serializers.Serializer):
    class Meta:
        model = Product
        field = 'title is_best_seller'


class BestsellerValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    is_best_seller = serializers.BooleanField(default=False)
    
    def validate_bestseller(self, is_best_seller, title):
        bestsellers = Product.objects.filter(is_best_seller=is_best_seller)
        if bestsellers == True:
            return title




class FavoriteSerializer(serializers.Serializer):
    class Meta:
        model = Product
        field = 'title is_favorite'


class FavoriteValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    is_favorite = serializers.BooleanField(default=False)
    
    def validate_bestseller(self, is_favorite, title):
        favorites = Product.objects.filter(is_favorite=is_favorite)
        if favorites == True:
            return title



class SaleSerializer(serializers.Serializer):
    class Meta:
        model = Product
        field = 'title original_price discount_price'


class SaleValidateSerializer(serializers.Serializer):
    title = serializers.CharField()
    original_price = serializers.FloatField(min_value=0.1)
    discount_price = serializers.IntegerField()

    # def validate_sale(self, title, discount_price):
    #     if discount_price != 0:
    #         return title


class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        field = 'user ordered created_at'

class OrderValidateSerializer(serializers.Serializer):
    user = serializers.CharField(max_length=50)
    ordered = serializers.BooleanField(default=True)
    created_at = serializers.CharField(max_length=20)


class OrderItemSerializer(serializers.Serializer):
    class Meta:
        model = OrderItem
        field = 'user product quantity'


class OrderItemValidateSerializer(serializers.Serializer):
    product = serializers.CharField()
    quantity = serializers.CharField(default=1)