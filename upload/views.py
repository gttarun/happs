from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from django.shortcuts import render
from .models import FileUpload
from .serializers import FileUploadSerializer

def get_image(request, image_id):
    db_image = FileUpload.objects.get(pk=image_id)
    image = "../" + str(db_image.datafile)
    return render(request, 'upload/show_image.html', {'image': image})

class FileUploadViewSet(ModelViewSet):
	
	queryset = FileUpload.objects.all()
	serializer_class = FileUploadSerializer
	parser_classes = (MultiPartParser, FormParser,)

	def perform_create(self, serializer):
		serializer.save(datafile=self.request.data.get('datafile'))
