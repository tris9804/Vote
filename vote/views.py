from rest_framework import viewsets
from rest_framework.response import Response
from .models import Candidate
from .serializers import CandidateSerializer
from rest_framework.decorators import action



class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    # @action(['POST'], True)
    # def creat_candidate(self, request):
    #     candidate = self.get_object()
    #     candidate.save()
    #     return Response('新增成功')



    @action(['PATCH'],True)
    def vote(self, request, pk):
        candidate = self.get_object()
        candidate.vote += 1
        candidate.save()
        return Response('投票成功')
        



