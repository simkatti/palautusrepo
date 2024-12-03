from matchers import And, HasAtLeast, PlaysIn, HasFewerThan, Not, All, Or


class QueryBuilder:
    def __init__(self, query=All()):
        self._query = query

    def plays_in(self, team):
        return QueryBuilder(And(self._query, PlaysIn(team)))
    
    def has_at_least(self, value, attribute):
        return QueryBuilder(And(self._query, HasAtLeast(value, attribute)))
    
    def has_fewer_than(self, value, attribute):
        return QueryBuilder(And(self._query, HasFewerThan(value, attribute)))
    
    def one_of(self, *queries):
        return QueryBuilder(Or(*queries))

    def build(self):
        return self._query