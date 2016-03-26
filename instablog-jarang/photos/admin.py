from django.contrib import admin

from .models import Photo
from .models import Like


admin.site.register(Photo)
admin.site.register(Like)
# logger = logging.getLogger('django')

# class PhotoSerializer(serializer.ModelSerializer):
# 	class Meta:
