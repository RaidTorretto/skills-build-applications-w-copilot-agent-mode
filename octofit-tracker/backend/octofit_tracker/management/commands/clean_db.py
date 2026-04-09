from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Clean all octofit_db collections (raw MongoDB)'

    def handle(self, *args, **kwargs):
        db = connection.cursor().db_conn
        for collection in ['users', 'teams', 'activities', 'workouts', 'leaderboard']:
            db[collection].drop()
        self.stdout.write(self.style.SUCCESS('All octofit_db collections dropped.'))
