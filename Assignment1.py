# Create a terminal based application that has two functions of finding Union and Intersection from a Set of number 

class SetOperations:
    def __init__(self, *sets):
        self.sets = sets # initializing class with any amount of sets (*sets) dynamically
    
    def union_the_sets(self):
        finalset = set() # an empty set

        for s in self.sets: # for loop to loop through eachelemnt in self.sets
            for x in s:
                finalset.add(x)  # union the current element with the result set
        return finalset
    
    def intersection_the_sets(self):
        if not self.sets: # if no sets r given
            return set() # return an empty set ]
        
        finalset = self.sets[0] # give it the first set

        for s in self.sets[1:]: # slices the self.sets (skips first set cuz alr stored)
            new = set() # new is just empty

            for x in finalset: # every element in the first set
                if x in s: # if its in the current set
                    new.add(x)  # add element to new

            finalset = new  # update finalset with the new
        
        return finalset

def main(): # basic main
    set1 = {2, 4, 5, 6}
    set2 = {2, 4, 6, 7, 8}
    set3 = {2, 4, 7, 8, 9, 10}
    setss = SetOperations(set1, set2, set3) # created an instance

    while True:
        print("\n Menu:")
        print("1. Find Union")
        print("2. Find Intersection")
        print("3. Leave")
        choice = input("Enter a number: ") # getting user choice 
        
        if choice == '1':
            result = setss.union_the_sets()
            print("Union of sets:", result)
        elif choice == '2':
            result = setss.intersection_the_sets()
            print("Intersection of sets:", result)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Try again.")

if __name__ == "__main__":
    main()
