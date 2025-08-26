###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    cow_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            name, weight = line.split(",")
            cow_dict[name] = int(weight)
    return cow_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    total_trips = []
    sorted_cows = {k: v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse=True)}
    weight_total = 0
    local_trip = []
    for cow, weight in sorted_cows.items():
        if weight_total + weight <= limit:
            local_trip.append(cow)
            weight_total += weight
        else:
            total_trips.append(local_trip)
            weight_total = weight
            local_trip = [cow]
    total_trips.append(local_trip)
    return total_trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    eligible_combos = []
    for item in get_partitions(list(cows.keys())):
        eligible_combos.append(item)
        for cow_combo in item:
            total_weight = 0
            for cow in cow_combo:
                total_weight += cows[cow]
            if total_weight > limit:
                if len(eligible_combos) > 0:
                    eligible_combos.pop()
                else:
                    continue
    return min(eligible_combos, key=len)
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    start = time.time()
    print(f"Number of Greedy trips: {len(greedy_cow_transport(cows=cows, limit=10))}")
    end = time.time()
    print(f"Greedy Algorithm took {end - start} seconds")
    start = time.time()
    print(f"Number of Brute trips: {len(brute_force_cow_transport(cows=cows, limit=10))}")
    end = time.time()
    print(f"Brute Force Algorithm took {end - start} seconds")

if __name__ == "__main__":
    compare_cow_transport_algorithms()