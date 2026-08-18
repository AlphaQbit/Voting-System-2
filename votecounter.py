import addcandidate
import deletecandidate
import viewResult

def cast_vote(name):
    if name in addcandidate.candidates:
        if name not in addcandidate.votes:
            addcandidate.votes[name] = 0
        addcandidate.votes[name] += 1
        return True
    return False

def get_results():
    return addcandidate.votes

if __name__ == "__main__":
    while True:
        print("\n--- Voting System ---")
        print("1. Add Candidate")
        print("2. Vote")
        print("3. View Results")
        print("4. Delete Candidate")
        print("5. Exit")
        
        choice = input("Choose (1-5): ")
        
        if choice == "1":
            name = input("Enter candidate name: ")
            if addcandidate.add_candidate(name):
                print(f"Added {name}")
            else:
                print("Candidate already exists")
        
        elif choice == "2":
            if not addcandidate.candidates:
                print("No candidates available")
                continue
            
            for i, c in enumerate(addcandidate.candidates, 1):
                print(f"{i}. {c}")
            
            num = input("Select candidate number: ")
            if num.isdigit() and 1 <= int(num) <= len(addcandidate.candidates):
                candidate = addcandidate.candidates[int(num) - 1]
                if cast_vote(candidate):
                    print(f"Vote for {candidate} recorded")
            else:
                print("Invalid choice")
        
        elif choice == "3":
            viewResult.show_results()
        
        elif choice == "4":
            if not addcandidate.candidates:
                print("No candidates to delete")
                continue
            
            for i, c in enumerate(addcandidate.candidates, 1):
                print(f"{i}. {c}")
            
            num = input("Select candidate to delete: ")
            if num.isdigit() and 1 <= int(num) <= len(addcandidate.candidates):
                candidate = addcandidate.candidates[int(num) - 1]
                if deletecandidate.delete_candidate(candidate):
                    print(f"Deleted {candidate}")
            else:
                print("Invalid choice")
        
        elif choice == "5":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice")