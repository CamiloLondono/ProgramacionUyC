from rest_framework.serializers import ModelSerializer
from chats.models import Mensaje


class ChatsSerializer(ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'