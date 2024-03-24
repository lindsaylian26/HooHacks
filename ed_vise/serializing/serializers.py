from rest_framework import serializers
from .models import Advisee, Advisor, SubjectArea

class AdviseeSerializer(serializers.ModelSerializer):
    interests = serializers.SlugRelatedField(
        queryset=SubjectArea.objects.all(),
        slug_field='name',
        many=True
    )

    class Meta:
        model = Advisee
        fields = '__all__'

class AdvisorSerializer(serializers.ModelSerializer):
    expertise_areas = serializers.SlugRelatedField(
        queryset=SubjectArea.objects.all(),
        slug_field='name',
        many=True
    )

    class Meta:
        model = Advisor
        fields = '__all__'
