from blaseball_mike.models import Player
import argparse
import math

parser = argparse.ArgumentParser(description='Compute simsim blessing effects')
parser.add_argument('player_list', type=argparse.FileType('r'),
                    help='File with a list of player names')

args = parser.parse_args()

player_names = args.player_list.read().split('\n')
if player_names[-1] == '':
    player_names.pop()
players = [Player.make_random(name=x,seed=x) for x in player_names]

def format_stars(star_count):
    result = ''
    for i in range(0, math.trunc(star_count)):
        result += '*'
    if star_count != math.trunc(star_count):
        result += '.'
    return result

def compute_blessing_effects(title, blessing_function):
    print('{:*^71}'.format(' ' + title + ' '))
    print('\nPlayer             Batting     Baserunning     Defense       Pitching\n')
    for player in players:
        blessed_player_name = blessing_function(player.name)
        blessed_player = Player.make_random(name=blessed_player_name, seed=blessed_player_name)
        print('{:15}  {:5} ({:+.1f})  {:5} ({:+.1f})  {:5} ({:+.1f})  {:5} ({:+.1f})'.format(blessed_player_name[0:15],
        format_stars(blessed_player.batting_stars), blessed_player.batting_stars - player.batting_stars,
        format_stars(blessed_player.baserunning_stars), blessed_player.baserunning_stars - player.baserunning_stars,
        format_stars(blessed_player.defense_stars), blessed_player.defense_stars - player.defense_stars,
        format_stars(blessed_player.pitching_stars), blessed_player.pitching_stars - player.pitching_stars
        ))
    print('\n')

def reflect_name(name):
    words = name.split(' ')
    words.reverse()
    return ' '.join(words)

compute_blessing_effects('Man In The Mirror', reflect_name)

compute_blessing_effects('Electric Boogaloo', lambda name: name + '... 2!')
compute_blessing_effects('The Youth Will Save Us', lambda name: name + ' Jr.')
compute_blessing_effects('All In The Family', lambda name: name + ' Sr.')
compute_blessing_effects('Scream and Shout', lambda name: name.upper())
compute_blessing_effects('This Is A Library', lambda name: name.lower())
compute_blessing_effects('The Lady Doth Protest Too Much Methinks', lambda name: '(definitely not) ' + name)
compute_blessing_effects('Mega Evolution', lambda name: 'Mega' + name)
compute_blessing_effects('Grand Entrance', lambda name: 'The ' + name)
