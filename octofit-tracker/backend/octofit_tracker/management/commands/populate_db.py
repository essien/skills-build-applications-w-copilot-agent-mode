from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, calories=300, date='2025-09-25')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, calories=450, date='2025-09-24')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, calories=600, date='2025-09-23')
        Activity.objects.create(user=users[3], type='Yoga', duration=40, calories=200, date='2025-09-22')

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.', difficulty='Hard')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.', difficulty='Medium')

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=750)
        Leaderboard.objects.create(team=dc, points=800)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
