from rest_framework import generics

from api.mixins import StaffEditorPermissionMixin, UserQuerysetMixin

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(
    UserQuerysetMixin, StaffEditorPermissionMixin, generics.ListCreateAPIView
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # email = serializer.validated_data.pop("email")
        # print(email)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)

    # def get_queryset(self, *args, **kwargs):
    #     qs = super().get_queryset(*args, **kwargs)
    #     request = self.request
    #     print(request.user)
    #     return qs.filter(user=request.user)


product_list_create_view = ProductListCreateAPIView.as_view()


class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = "pk"


product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIView(StaffEditorPermissionMixin, generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


product_detail_view = ProductListAPIView.as_view()


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


product_destroy_view = ProductDestroyAPIView.as_view()


# class ProductMixinView(
#     mixins.CreateModelMixin,
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_field = "pk"

#     def get(self, request, *args, **kwargs):
#         pk = kwargs.get("pk")
#         if pk is not None:
#             return self.retrieve(request, *args, **kwargs)
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# product_mixin_view = ProductMixinView.as_view()


# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         if pk is not None:
#             # detail view
#             obj = get_object_or_404(Product, pk=pk)
#             data = ProductSerializer(obj, many=False).data  # many is false by default
#             return Response(data)

#         # list view
#         queryset = Product.objects.all()
#         data = ProductSerializer(queryset, many=True).data
#         return Response(data)

#     if method == "POST":
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             title = serializer.validated_data.get("title")
#             content = serializer.validated_data.get("content") or None
#             if content is None:
#                 content = title
#             serializer.save(content=content)
#             return Response(serializer.data)
#         return Response({"invalid": "not good data"}, status=400)
