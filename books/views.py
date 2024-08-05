from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action


class BooksViewset(GenericViewSet):
    @action(detail=False, methods=["GET"], url_path="get-books")
    def get_books_api(self, request):
        print(request.query_params)
        return Response({"message": "hello"}, status=200)
