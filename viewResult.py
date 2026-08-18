# Calayag, Edward P.
# View Results

import addcandidate

def show_results():
    print("\n--- Voting Results ---")
    
    if not addcandidate.candidates:
        print("No candidates available")
        return
    
    total = 0
    for candidate in addcandidate.candidates:
        votes = addcandidate.votes.get(candidate, 0)
        print(f"{candidate}: {votes} votes")
        total += votes
    
    print(f"Total votes: {total}")
    print("-" * 30)