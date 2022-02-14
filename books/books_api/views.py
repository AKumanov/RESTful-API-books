from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import BookModel
from .serializers import BookSerializer


class BookListCreate(APIView):

    def get(self, request):
        books = BookModel.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response(book_serializer.data, status=status.HTTP_201_CREATED)
        return Response(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookGetUpdateDelete(APIView):

    def put(self, request, id):
        try:
            book = BookModel.objects.get(id=id)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)

        except:
            return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        try:
            book = BookModel.objects.get(id=id)

            book_serializer = BookSerializer(book)
            return Response(book_serializer.data, status=status.HTTP_200_OK)

        except:
            return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id):
        try:
            book = BookModel.objects.get(id=id)
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({'message': 'not found'}, status=status.HTTP_404_NOT_FOUND)
