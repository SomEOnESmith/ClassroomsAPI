from django.shortcuts import render
from rest_framework.generics import (ListAPIView, 
	RetrieveAPIView, CreateAPIView , RetrieveUpdateAPIView, DestroyAPIView)

from classes.models import Classroom

from .serializer import (ClassroomListSerializer, ClassroomDetailSerializer ,
 	ClassroomCreateSerializer )



class ClassroomList(ListAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomListSerializer


class ClassroomDetail(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomUpdate(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomDelete(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
	serializer_class = ClassroomCreateSerializer
	def perform_create(self, serializer):
		serializer.save(teacher = self.request.user)