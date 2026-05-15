from djongo import models


class Team(models.Model):
    id = models.ObjectIdField()
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    id = models.ObjectIdField()
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=150)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='members')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email


class Activity(models.Model):
    id = models.ObjectIdField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    type = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    distance_km = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'activities'


class LeaderboardEntry(models.Model):
    id = models.ObjectIdField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.IntegerField(default=0)
    rank = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'leaderboard'


class Workout(models.Model):
    id = models.ObjectIdField()
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    name = models.CharField(max_length=200)
    exercises = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'workouts'
