"""
Program Name: game_stats.py
Author: Shrrayash Srinivasan
Purpose: Defined settings for the Alien Invasion game, including screen dimensions, asset paths, ship and bullet behavior, 
and initial ship placements
. 
Date: November 22, 2025
"""

class GameStats():

    def __init__(self, hero_ships_limit):
        self.hero_ships_left = hero_ships_limit