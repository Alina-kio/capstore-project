from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
from capstore.models import *
from capstore.serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,   # get
    ListCreateAPIView,    # post
    RetrieveUpdateDestroyAPIView,    # put delete
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
# Create your views here.





@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def brand_view(request):
    print(request.user)
    if request.method == 'GET':
        brands = PopularBrand.objects.all()
        data = PopularBrandSerializer(brands, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = BrandValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = serializer.validated_data.get('title') 
        product = Product.objects.create(
            title=name
        )
        return Response(data=ProductSerializer(product).data)


class BrandAPIViewSet(ModelViewSet):
    queryset = PopularBrand.objects.all()
    serializer_class = PopularBrandSerializer
    pagination_class = PageNumberPagination


@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        data = ProductSerializer(products, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = serializer.validated_data.get('name')  # Sumka Louis Vitton
        brand_id = serializer.validated_data.get('brand_id')  # 100
        original_price = serializer.validated_data.get('original_price')  # None
        discount_price = serializer.validated_data.get('discount_price')
        product = Product.objects.create(
            title=name,
            brand_id=brand_id,
            original_price=original_price,
            discount_price=discount_price
        )
        return Response(data=ProductSerializer(product).data)



@api_view(['GET', 'PUT', 'DELETE'])
def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductDetailSerializer(product).data
        return Response(data=data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = request.data.get('name')  # Sumka Louis Vitton
        brand_id = request.data.get('brand_id')  # 100
        original_price = request.data.get('original_price')  # None
        discount_price = request.data.get('discount_price')
        size = request.data.get('size')
        description = request.data.get('description')
        is_best_seller = request.data.get('is_best_seller')
        is_favorite = request.data.get('is_favorite')
        name = request.data.get('name')  # Sumka Louis GUCCI
        product.title = name
        product.brand = brand_id
        product.original_price = original_price
        product.discount_price = discount_price
        product.size = size
        product.description = description
        product.is_best_seller = is_best_seller
        product.is_favorite = is_favorite
        product.save()
        return Response(data=ProductSerializer(product).data)



@api_view(['GET'])
def bestseller_view(request):
    bestsellers = Product.objects.filter(is_best_seller=True)
    data = BestsellerValidateSerializer(bestsellers, many=True).data
    return Response(data=data)


@api_view(['GET'])
def favorite_view(request):
    favorites = Product.objects.filter(is_favorite=True)
    data = FavoriteValidateSerializer(favorites, many=True).data
    return Response(data=data)


@api_view(['GET'])
def sale_view(request):
    sales = Product.objects.filter(discount_price__isnull=False)
    data = SaleValidateSerializer(sales, many=True).data
    return Response(data=data)


@api_view(['GET'])
def order_view(request):
    order = Order.objects.all()
    data = OrderValidateSerializer(order, many=True).data
    return Response(data=data)


@api_view(['GET'])
def orderitem_view(request):
    orderitem = OrderItem.objects.all()
    data = OrderItemValidateSerializer(orderitem, many=True).data
    return Response(data=data)