from .models import Visit
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import UserVisitSerializer



class UserVisitsView(ListAPIView):
    models = Visit
    serializer_class = UserVisitSerializer

    def get_queryset(self):
        query_set = Visit.objects.get_visits_by_user()
        return query_set

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
