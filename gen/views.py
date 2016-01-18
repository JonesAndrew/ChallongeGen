from django.shortcuts import render
from django.http import HttpResponse
from gen.models import Player
import operator

def update(request):
    import challonge
    import pprint
    import django
    from challonge import api
    import math;
    from trueskill import Rating, quality_1vs1, rate_1vs1

    # Tell pychallonge about your [CHALLONGE! API credentials](http://api.challonge.com/v1).
    challonge.set_credentials("shifterj", "4E7wOHBx42sxz4upVGHCRyBpKiSltzjhFALfQLzi")

    parts = {}

    def addPlayer(p):
        try:
            player = Player.objects.get(name=p["name"])
        except:
            player = Player()
            player.name = p["name"];
            player.mu = 25.0;
            player.sigma = 8.333333333;
            parts[p["id"]] = player;

    def tournament(tourney):
        participants = challonge.participants.index(tourney)

        for p in participants:
            addPlayer(p)

        # Retrieve a tournament by its id (or its url).
        matches = challonge.matches.index(tourney)

        for m in matches:
            print(parts[m["player1-id"]].name + " vs " + parts[m["player2-id"]].name)
            print(parts[m["winner-id"]].name + " won!")
            id1 = m["player1-id"]
            id2 = m["player2-id"]
            if m["winner-id"] == id2:
                temp = id1
                id1 = id2
                id2 = temp

            r1 = Rating(mu=parts[id1].mu,sigma=parts[id1].sigma)
            r2 = Rating(mu=parts[id2].mu,sigma=parts[id2].sigma)

            r1, r2 = rate_1vs1(r1, r2)

            parts[id1].mu = r1.mu
            parts[id1].sigma = r1.sigma
            parts[id2].mu = r2.mu
            parts[id2].sigma = r2.sigma

    # tournament("TBBI")
    tournament("DownstairsI")

    for k, p in parts.iteritems():
        print(p)
        p.save()

    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):

    players = Player.objects.order_by("-mu")

    return render(request, 'gen/index.html', context = {'elo_players': players})
