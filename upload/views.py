from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from .models import FileUpload
from .serializers import FileUploadSerializer
from django.utils.encoding import smart_str
from PIL import Image

def get_image(request, image_id):
	db_image = FileUpload.objects.get(pk=image_id)
	image = "../" + str(db_image.datafile)
	return render(request, 'upload/show_image.html', {'image': image})

class FileUploadViewSet(ModelViewSet):
	
	queryset = FileUpload.objects.all()
	serializer_class = FileUploadSerializer
	parser_classes = (MultiPartParser, FormParser,)

	def create(self, serializer):
		try:
			serializer.save(datafile=self.request.data.get('datafile'))
		except Exception,e: 
			print str(e)

	def retrieve(self, request, pk, format=""):
		# if format:
		# 	im = str(format)
		# 	image = Image.open(im)
		# 	response = HttpResponse(content_type='application/force-download')
		# 	response['Content-Disposition'] = 'attachment; filename=%s' % smart_str("image.jpg")
		# 	image.save(response, "jpeg")
		# 	return response
		# else:
		# 	images = []
		# 	db_image = FileUpload.objects.filter(username=pk)
		# 	for each in db_image:
		# 		images.append(str(each.datafile))
		# 	return render(request, 'upload/show_image.html', {'images': images, 'username': pk})
		images = []
		db_image = FileUpload.objects.filter(username=pk)
		for each in db_image:
			images.append(str(each.datafile))
		return render(request, 'upload/show_image.html', {'images': images, 'username': pk})
