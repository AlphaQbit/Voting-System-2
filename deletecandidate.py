import addcandidate

def delete_candidate(name):
    if name in addcandidate.candidates:
        addcandidate.candidates.remove(name)
        if name in addcandidate.votes:
            del addcandidate.votes[name]
        return True
    return False