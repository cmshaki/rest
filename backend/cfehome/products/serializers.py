from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title, validate_title_no_hello


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk", read_only=True
    )
    title = serializers.CharField(read_only=True)


class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source="user", read_only=True)
    # related_products = ProductInlineSerializer(
    #     source="user.product_set.all", read_only=True, many=True
    # )
    # my_discount = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validate_title, validate_title_no_hello])
    body = serializers.CharField(source="content")
    # name = serializers.CharField(source="title", read_only=True)
    # email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Product
        fields = [
            "owner",
            "pk",
            "title",
            "body",
            "price",
            "public",
            "sale_price",
            "path",
            "endpoint",
            # "my_discount",
            # "related_products",
        ]

    # def validate_title(self, value):
    #     request = self.context.get("request")
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    # def create(self, validated_data):
    #     email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     return super().update(instance, validated_data)
    def get_my_user_data(self, obj):
        return {"username": obj.user.username}

    def get_edit_url(self, obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, "id"):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
