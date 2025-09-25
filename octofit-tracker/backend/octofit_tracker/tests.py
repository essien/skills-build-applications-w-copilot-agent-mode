from django.test import TestCase
from .models import Team, User, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='Desc', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=30, calories=200, date='2025-09-25')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')

    def test_activity_creation(self):
        self.assertEqual(self.activity.type, 'Run')

    def test_workout_creation(self):
        self.assertEqual(self.workout.difficulty, 'Easy')

    def test_leaderboard_creation(self):
        self.assertEqual(self.leaderboard.points, 100)
