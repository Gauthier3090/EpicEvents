from django.core.management import BaseCommand
from users.models import Team


class Command(BaseCommand):
    help = "Create teams in database."

    def handle(self, *args, **options):
        if options["verbosity"] != 0:
            self.stdout.write(f"Creating all teams in database...")
            self.create_teams()

    def create_teams(self):
        teams = ('MANAGEMENT', 'SALES', 'SUPPORT')
        for team in teams:
            if Team.objects.filter(name=team).count() > 0:
                self.stdout.write(f"{team} team already exists in database...")
            else:
                management = Team.objects.create(
                    name=team
                )
                management.save()
