class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

## tehtävä 2:

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value
    
class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return False

        return True
    
class All:
    def __init__(self):
        pass

    def test(self, player):
        return True

## tehtävä 3:

class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if matcher.test(player):
                return True

        return False

# tehtävä 4:

class QueryBuilder:
    def __init__(self, pino = All(), kaskyhistoria=[All()]):
        self.pino_olio = pino
        self.kaskyhistoria = kaskyhistoria # esim. [PlaysIn("SEA"), HasAtLeast(3, "goals")]

    def build(self):
        return self.pino_olio

    def playsIn(self, team):
        self.kaskyhistoria.append(PlaysIn(team))
        return QueryBuilder(And(*self.kaskyhistoria))
    
    def hasAtLeast(self, value, attr):
        self.kaskyhistoria.append(HasAtLeast(value, attr))
        return QueryBuilder(And(*self.kaskyhistoria))
    
    def hasFewerThan(self, value, attr):
        self.kaskyhistoria.append(HasFewerThan(value, attr))
        return QueryBuilder(And(*self.kaskyhistoria))
