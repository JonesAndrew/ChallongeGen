from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from gen.models import Player,Tournament,TournamentList
from .forms import BracketForm
import operator, re

def update(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BracketForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            url = form.cleaned_data['bracket_url']
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
                    parts[p["id"]] = player;
                except:
                    player = Player()
                    player.name = p["name"];
                    player.mu = 25.0;
                    player.sigma = 8.333333333;
                    parts[p["id"]] = player;

            def tournament(tourney):
                tList = TournamentList.load()

                for t in tList.tournaments.all():
                    if t.name == tourney:
                        return None

                t = Tournament()
                t.name = tourney
                t.save()
                tList.tournaments.add(t)
                tList.save()

                participants = challonge.participants.index(tourney)

                for p in participants:
                    addPlayer(p)

                # Retrieve a tournament by its id (or its url).
                matches = challonge.matches.index(tourney)

                for m in matches:
                    score = re.findall(r'\d+', m["scores-csv"])
                    id1 = m["player1-id"]
                    id2 = m["player2-id"]
                    parts[id1].Gwins+=int(score[0])
                    parts[id1].Glosses+=int(score[1])
                    parts[id2].Gwins+=int(score[1])
                    parts[id2].Glosses+=int(score[0])
                    if m["winner-id"] == id2:
                        temp = id1
                        id1 = id2
                        id2 = temp

                    r1 = Rating(mu=float(parts[id1].mu),sigma=float(parts[id1].sigma))
                    r2 = Rating(mu=float(parts[id2].mu),sigma=float(parts[id2].sigma))

                    r1, r2 = rate_1vs1(r1, r2)

                    parts[id1].mu = r1.mu
                    parts[id1].sigma = r1.sigma
                    parts[id2].mu = r2.mu
                    parts[id1].safe = parts[id1].mu-(3*parts[id1].sigma)
                    parts[id2].sigma = r2.sigma
                    parts[id2].safe = parts[id2].mu-(3*parts[id1].sigma)
                    parts[id1].Swins+=1
                    parts[id2].Slosses+=1

            tournament(url)

            for k, p in parts.iteritems():
                print(p)
                p.save()

            print(url)
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BracketForm()

    return render(request, 'gen/update.html', {'form': form})

def index(request):

    players = Player.objects.order_by("-safe")

    return render(request, 'gen/index.html', context = {'elo_players': players, "tournaments": TournamentList.load().tournaments.all()})
