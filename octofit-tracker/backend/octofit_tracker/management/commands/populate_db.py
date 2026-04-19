from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='dc', description='DC Superheroes')

        # Create Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
        ]

        # Create Workouts
        workouts = [
            Workout.objects.create(name='Pushups', description='Do 50 pushups', suggested_for='marvel'),
            Workout.objects.create(name='Situps', description='Do 50 situps', suggested_for='dc'),
        ]

        # Create Activities
        Activity.objects.create(user=users[0], type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=users[1], type='cycle', duration=45, date=timezone.now().date())
        Activity.objects.create(user=users[2], type='swim', duration=60, date=timezone.now().date())
        Activity.objects.create(user=users[3], type='yoga', duration=20, date=timezone.now().date())

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], points=100, rank=1)
        Leaderboard.objects.create(user=users[1], points=90, rank=2)
        Leaderboard.objects.create(user=users[2], points=80, rank=3)
        Leaderboard.objects.create(user=users[3], points=70, rank=4)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
