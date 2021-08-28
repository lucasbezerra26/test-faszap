from .models import Client, Attendance, Message
from .serializer import ClientSerializer, AttendanceSerializer, MessageSerializer

from rest_framework import viewsets, generics, mixins

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceFilterViewSet(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    def get_queryset(self):
        """  """
        queryset = Attendance.objects.filter(client__id=self.kwargs['client'])
        return queryset


class MessageViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageFilterViewSet(generics.ListAPIView):
    serializer_class = MessageSerializer
    def get_queryset(self):
        """  """
        queryset = Message.objects.filter(attendance__id=self.kwargs['attendance'])
        return queryset

""" outro app """
