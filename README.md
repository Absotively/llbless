# llbless
A very rough blessing effect calculator for the simsim's Larceny League (it's a blaseball thing)

```
usage: llbless.py [-h] [--emoji EMOJI] [--rebirth REBIRTH] player_list out

Compute simsim blessing effects. Pass - as the player list to read from stdin,
or as the output file to read from stdout.

positional arguments:
  player_list           File with a list of player names
  out                   Output file

optional arguments:
  -h, --help            show this help message and exit
  --emoji EMOJI, -e EMOJI
                        Emoji for Enamel Pins blessing
  --rebirth REBIRTH, -r REBIRTH
                        Prefix/suffix for Rebirth blessing
```
