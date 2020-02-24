
def friends_teams(friends, team_size:int = 2, order_does_matter:bool = False):
    import itertools
    if order_does_matter:
        return list(itertools.permutations(friends, team_size))
    else:
        return list(itertools.combinations(friends, team_size))
        
