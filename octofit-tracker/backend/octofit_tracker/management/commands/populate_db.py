from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, UserProfile, Activity, LeaderboardEntry, Workout


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        teams = [
            {
                'name': 'marvel',
                'description': 'Marvel team',
                'members': ['Iron Man', 'Spider-Man', 'Thor', 'Hulk', 'Black Widow'],
            },
            {
                'name': 'dc',
                'description': 'DC team',
                'members': ['Batman', 'Superman', 'Wonder Woman', 'Flash', 'Aquaman'],
            },
        ]

        activity_templates = [
            ('run', 30, 5.0),
            ('cycle', 45, 12.0),
        ]

        users = []

        for team_index, team_data in enumerate(teams, start=1):
            team, _ = Team.objects.update_or_create(
                name=team_data['name'],
                defaults={'description': team_data['description']},
            )

            for member_index, member_name in enumerate(team_data['members'], start=1):
                email = member_name.replace(' ', '').lower() + f'@{team_data["name"]}.com'
                user, _ = UserProfile.objects.update_or_create(
                    email=email,
                    defaults={'name': member_name, 'team': team},
                )
                users.append((user, team_index, member_index))

        for user, team_index, member_index in users:
            for activity_index, (activity_type, base_duration, base_distance) in enumerate(activity_templates, start=1):
                Activity.objects.update_or_create(
                    user=user,
                    type=activity_type,
                    duration_minutes=base_duration + team_index * 5 + member_index + activity_index,
                    distance_km=round(base_distance + team_index + (member_index * 0.5) + (activity_index * 0.25), 2),
                )

            Workout.objects.update_or_create(
                user=user,
                name=f'{user.name} starter workout',
                defaults={'exercises': [{'name': 'pushups', 'reps': 20}, {'name': 'squats', 'reps': 15}]},
            )

            LeaderboardEntry.objects.update_or_create(
                user=user,
                defaults={'points': (team_index * 100) + (member_index * 10), 'rank': member_index},
            )

        self.stdout.write(self.style.SUCCESS('Database populated with sample data.'))
