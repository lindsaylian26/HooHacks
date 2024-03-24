from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Advisee, Advisor
from .serializers import AdviseeSerializer, AdvisorSerializer

class MatchView(APIView):
    def get(self, request):
        advisees = Advisee.objects.all()
        advisors = Advisor.objects.all()
        matches = []

        for advisee in advisees:
            for advisor in advisors:
                if set(advisee.interests.all()) & set(advisor.expertise_areas.all()):
                    # Check if advising styles match
                    if advisee.preferred_advising_style in advisor.advising_styles:
                        matches.append({
                            'advisee': AdviseeSerializer(advisee).data,
                            'advisor': AdvisorSerializer(advisor).data
                        })

        return Response({'matches': matches})