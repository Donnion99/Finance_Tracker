from rest_framework.serializers import ModelSerializer
from .. import models

class PostSerializers(ModelSerializer):
    class Meta:
        model = models.Finance_Info
        fields = ('id','Amount','Category','Date','Desc')