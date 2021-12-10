from matchers import All, And, HasAtLeast, PlaysIn, HasFewerThan, Or

class QueryBuilder:
    def __init__(self):
        self._matchers = All()
    
    def build(self):
        return self._matchers

    def playsIn(self, team):
        self._matchers = And(PlaysIn(team), self._matchers)
        return self
    
    def hasAtLeast(self, value, attr):
        self._matchers = And(HasAtLeast(value, attr), self._matchers)
        return self

    def hasFewerThan(self, value, attr):
        self._matchers = And(HasFewerThan(value, attr), self._matchers)
        return self

    def oneOf(self, team1, team2):
        self._matchers = Or(team1, team2)
        return self