
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RSWKsite.settings")

import django
django.setup()


from basic_app.models import PastSeasons, CurrentSeason, Player
from basic_app.rswk_past import past_seasons
from basic_app.espn_api import db_update, db_load, owners

def add_player(li):
    stat = Player.objects.get_or_create(player_name=li)[0]
    stat.save()

def add_past(li):
    stat = PastSeasons.objects.get_or_create(year=int(li[0]), place=int(li[1]), team_name=li[2], owner=li[3], wins=int(li[5]), losses=int(li[6]), ties=int(li[7]), points_for=float(li[8]), points_against=float(li[9]))[0]

    stat.save()

def add_cur(li):
    stat = CurrentSeason.objects.get_or_create(game_week=li[0], team_abbrev=li[1], team_name=li[2], poinst_for=li[3], opponent=li[5], result=li[4], points_against=li[6], owner=li[7])[0]

    stat.save()



if __name__ == '__main__':
    print("populating script")
    for p in owners:
        add_player(p)
    for li in past_seasons:
        add_past(li)
    for i in db_load:
        add_cur(i)

    print("populating complete")
