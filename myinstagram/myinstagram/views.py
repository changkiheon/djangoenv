from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("Get Request")
        return render(request, "myinstagram/main.html")

    def post(self, request):
        print("Post Request")
        return render(request, "myinstagram/main.html")
