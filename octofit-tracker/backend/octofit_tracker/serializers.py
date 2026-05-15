from bson import ObjectId
from rest_framework import serializers
from .models import Team, UserProfile, Activity, LeaderboardEntry, Workout


class ObjectIdSerializerField(serializers.Field):
    def to_representation(self, value):
        if value is None:
            return None
        return str(value)

    def to_internal_value(self, data):
        if data in (None, ''):
            return None

        try:
            return ObjectId(str(data))
        except Exception as exc:
            raise serializers.ValidationError('Invalid ObjectId value.') from exc


class TeamSerializer(serializers.ModelSerializer):
    id = ObjectIdSerializerField(read_only=True)

    class Meta:
        model = Team
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    id = ObjectIdSerializerField(read_only=True)
    team = ObjectIdSerializerField(required=False, allow_null=True)

    class Meta:
        model = UserProfile
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    id = ObjectIdSerializerField(read_only=True)
    user = ObjectIdSerializerField()

    class Meta:
        model = Activity
        fields = '__all__'


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    id = ObjectIdSerializerField(read_only=True)
    user = ObjectIdSerializerField()

    class Meta:
        model = LeaderboardEntry
        fields = '__all__'


class WorkoutSerializer(serializers.ModelSerializer):
    id = ObjectIdSerializerField(read_only=True)
    user = ObjectIdSerializerField()

    class Meta:
        model = Workout
        fields = '__all__'
