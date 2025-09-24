from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def setUp(self):
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', team=marvel)
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass', team=dc)
        Activity.objects.create(user=ironman, type='Run', duration=30)
        Workout.objects.create(name='Hero HIIT', description='High intensity for heroes')
        Leaderboard.objects.create(team=marvel, points=100)

    def test_user_team(self):
        self.assertEqual(User.objects.get(username='ironman').team.name, 'Marvel')
        self.assertEqual(User.objects.get(username='batman').team.name, 'DC')

    def test_activity(self):
        activity = Activity.objects.get(type='Run')
        self.assertEqual(activity.duration, 30)

    def test_workout(self):
        workout = Workout.objects.get(name='Hero HIIT')
        self.assertEqual(workout.description, 'High intensity for heroes')

    def test_leaderboard(self):
        leaderboard = Leaderboard.objects.get(team__name='Marvel')
        self.assertEqual(leaderboard.points, 100)
