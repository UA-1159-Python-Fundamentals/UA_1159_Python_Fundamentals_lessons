"""Are You Playing Banjo?"""
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0] in "Rr" else f"{name} does not play banjo"