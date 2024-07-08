my_list = [1, 2, 3, 4, 5]
my_set = {1, 2, 3, 4, 5}


def custom_iteration(sequence, action):
    iterator = iter(sequence)
    completed_iterating = False
    while not completed_iterating:
        try:
            action(next(iterator))
        except StopIteration:
            completed_iterating = True

def power_of_2(num):
    print(num ** 2)


class CustomIterTeams(object):
    def __init__(self, division, teams=[]):
        self._mng = division
        self._teams = teams
        self._index = -1

    def __iter__(self):
        return self
    
    def __next__(self):
        self._index += 1
        if self._index >= len(self._teams):
            self._index = -1
            raise StopIteration
        else:
            return self._teams[self._index]

prem_teams = CustomIterTeams('Premier League', ['Arsenal', 'Watford', 'Bournemouth', 'Man Utd', 'Liverpool'])



class CustomIterTeams2(object):

    def __init__(self, division, teams=[]):
        self._mng = division
        self._teams = teams

    def __iter__(self):
        return (t for t in self._teams)

prem_teams2 = CustomIterTeams2('Premier League', ['Arsenal', 'Watford', 'Bournemouth', 'Man Utd', 'Liverpool'])







def integer_check(method):
    def inner(ref):
        if not isinstance(ref._val1, int) or not isinstance(ref._val2, int):
            raise TypeError('val1 and val2 must be integers')
        else:
            return method(ref)
    return inner


class NumericalOps:
    def __init__(self, val1, val2):
        self._val1 = val1
        self._val2 = val2

    @integer_check
    def multiply_together(self):
        return self._val1 * self._val2
    
