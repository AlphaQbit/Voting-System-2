candidates = ["Mary Grace Piattos", "Fernando Tempura", "Carlos Miguel Oishi", "Chippy McDonald", "Pia Piatos-Lim", "Renan Piatos"]
votes = {}

def add_candidate(name):
    if name not in candidates:
        candidates.append(name)
        votes[name] = 0
        return True
    return False

def get_candidates():
    return candidates