'''Player class to record stats for individual players
'''


class Player:
    '''Models Players of the football teams.

    Parameters
    ----------------------------------------
    name : str
        actual player name
    yards : int
        how many yards the player ran/passed the ball
    touchdowns : int
        how many touchdowns the player scored
    safety : int
        how many safeties the player forced
    interceptions : int
        How many times the player intercepted the ball
    field goals : int
        how many field goals the player achieved

    '''
    def __init__(self, name=None, yards=120, touchdowns=5, safety=1,
                 interceptions=0, field_goals=3):
        self.name = name
        self.yards = yards
        self.touchdowns = touchdowns
        self.safety = safety
        self.interceptions = interceptions
        self.field_goals = field_goals


class Quarterback(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to quarterbacks
    '''
    def __init__(self, name=None, yards=130, touchdowns=5, completed_passes=20,
                 interceptions=4, safety=None, field_goals=None):
        super().__init__(name=name, yards=yards, touchdowns=touchdowns,
                         safety=safety, interceptions=interceptions)
        self.completed_passes = completed_passes

    def passing_score(self):
        '''This is a random formula... FYI
        '''
        score = self.completed_passes - (2 * self.interceptions)
        return score

class Defense(Player):
    '''Override certain parameters of the default Player class and add some
    functionality unique to defensive player
    '''
    def __init__(self, name=None, tackles=10, sacks=5, interceptions=2, safety=3):
        super().__init__(name=name, yards=0, touchdowns=0,
                        safety=safety, interceptions=interceptions)
        self.tackles = tackles
        self.sacks = sacks


# TODO - refine the default player stats and/or make a defensive player default
# with number of tackles, sacks, interceptions etc.
John = Defense()
print(John.sacks)
print(John.name)
qb = Quarterback(Player())