from .models import Visit
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import UserVisitSerializer

class UserVisitsView(ListAPIView):
    """ use of rest_framework to
        View to list all users in the system.
        * Requires token authentication.
        * Only admin users are able to access this view.
        """
    models = Visit
    serializer_class = UserVisitSerializer

    def get_queryset(self):
        """ To calculate users visits over a days to show the results
        on a new view  """
        query_set = Visit.objects.get_visits_by_user()
        return query_set

    def list(self, request, *args, **kwargs):
        """ Return a list of all users."""
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
