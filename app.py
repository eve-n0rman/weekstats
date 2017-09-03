#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import default_app, route, run, get, template, view

import requests

@get('/')
@view('index')
def index():
    url = 'https://zkillboard.com/api/kills/allianceID/99003214/pastSeconds/604800/page/'
    page = 1
    more_kills = True
    characters = {}
    session = requests.session()
    while more_kills:
        request = url + str(page) + '/'
        print 'Fetching {}'.format(request)
        r = session.get(request)
        r.raise_for_status()
        kills = r.json()
        if kills:
            print 'Fetched {} kills'.format(len(kills))
            for kill in kills:
                killed = kill['victim']
                killers = kill['attackers']
                if killed.get('allianceName', None) == 'Brave Collective':
                    char = characters.setdefault(killed['characterName'], {'kills': 0, 'losses': 0, 'id': killed['characterID']})
                    char['losses'] += 1
                for killer in killers:
                    if killer.get('allianceName', None) == 'Brave Collective':
                        char = characters.setdefault(killer['characterName'], {'kills': 0, 'losses': 0, 'id': killer['characterID']})
                        char['kills'] += 1
            page += 1
        else:
            print 'No more kills'
            more_kills = False
    print characters
    return dict(characters=characters)

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True)

app = default_app()
