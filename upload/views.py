from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from .models import FileUpload
from .serializers import FileUploadSerializer


class FileUploadViewSet(ModelViewSet):
	
	queryset = FileUpload.objects.all()
	serializer_class = FileUploadSerializer
	parser_classes = (MultiPartParser, FormParser,)

	def perform_create(self, serializer):
		serializer.save(datafile=self.request.data.get('datafile'))
