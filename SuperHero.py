# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# battle_state = namedtuple('battle_state', 'level_index', 'battle_index', 'pre_initial',
#                                            'post_initial', 'pre_acquired', 'post_acquired',
#                                            'pre_total', 'post_total' )
"""
def get_min_bullets(levels, enemies, powers, bullets):
    forward = get_forward_path(levels, enemies, powers, bullets)

    # This gives us the best score based as measured by the least amount of bullets
    # spent per level (maximizing for number of bullets acquired)

    # The next loop has us going backwards
    # and picking battles that may spend a bit more but set's us up for savings down the road.

    for i, fwd_battle in reversed(list(enumerate(forward))):
        #check to see if the battle cost anything
        battle_cost = fwd_battle['post_initial'] - fwd_battle['pre_initial']
        if battle_cost > 0:
            # we have a situation where we might be able to do better
            power_to_beat = fwd_battle['power']

            prev_level_info = zip(powers[i-1], bullets[i-1])

            for i, (power, bullet) in enumerate(prev_level_info):
            # Are there any choices where the potential bullets are more than the next cost?
                if(bullet >= power_to_beat):


"""
def get_min_bullets(levels, enemies, powers, bullets):
    """
    The way this works is that it creates several pathways through the battles
    Once it has all of the pathways completed, it will take the best segments from each pathway
    to build the final pathway and final score
    """
    backward = get_backward_path(levels, enemies, powers, bullets)
    forward = get_forward_path(levels, enemies, powers, bullets)

    #print backward
    #print forward

    """
    """
    # DEBUG
    print "backward"
    for path in backward:
        print path
    print "forward"
    for path in forward:
        print path
    # DEBUG

    # Now I have two paths to compare
    # What I want to do is find all of the levels where they battle the same enemy
    # Where they exist, I want to pick the path where the "pre_initial" delta is least.
    b_initial = f_initial = initial_so_far = 0
    pick_next_true = False
    index_of_last_snapshot = -1
    for i, (b, f) in enumerate(zip(backward, forward)):
        if b['battle_index'] == f['battle_index']:
            if pick_next_true:
                index_of_last_snapshot = i
                b_delta = b['post_initial'] - b_initial
                f_delta = f['post_initial'] - f_initial
                b_initial = b['post_initial']
                f_initial = f['post_initial']
                initial_so_far += min(b_delta, f_delta)
                pick_next_true = False
        else:
            pick_next_true = True

    if index_of_last_snapshot < len(backward)-1:
        # We need to capture the final distance
        b_delta = backward[-1]['post_initial'] - b_initial
        f_delta = forward[-1]['post_initial'] - f_initial
        initial_so_far += min(b_delta, f_delta)

    return initial_so_far


def get_forward_path (levels, enemies, powers, bullets):
    """
    Identifies the best path starting with first battle and working forwards
    battle choice is based on minimum power
    """
    forward_path = []

#    min_power, battle_index = min((powers[0][i], i) for i in xrange(len(powers[0])))
    current_battle = {"level_index": -1, "power": 0, "pre_initial": 0, "post_initial": 0, "post_acquired": 0, "pre_total":0, "pre_acquired":0}

    for level in xrange(0, levels):
        level_info = zip(powers[level], bullets[level])
        next_battle = pick_battle_with_min_power(level_info, current_battle)
        next_battle["level_index"] = level
        forward_path.append(next_battle)
        current_battle = next_battle

    return forward_path

def get_backward_path(levels, enemies, powers, bullets):
    """
    Identifies the best path starting with last battle and working backwards
    battle choice is based on minimum pre ammunition required
    """

    backward_path = []
    # start at last battle and move backwards
    # minimum bullets as selection criteria

    min_bullets, battle_index = min((powers[levels - 1][i], i) for i in xrange(len(powers[levels - 1])))
    last_battle = {"level_index":levels-1,"battle_index":battle_index, "power":min_bullets, "pre_total":min_bullets, "pre_initial":0, "post_initial":0}

    backward_path.append(last_battle)

    for level in reversed(xrange(levels - 1)):
        level_info = zip(powers[level], bullets[level])
        previous_battle = pick_battle_with_min_bullets(level_info, last_battle)
        previous_battle["level_index"] = level
        backward_path.append(previous_battle)
        last_battle = previous_battle


    #update pre and post data now that we have completed the path
    backward_path = sorted(backward_path, key=lambda k: k["level_index"])
    previous_battle = backward_path[0]
    previous_battle['pre_initial'] = 0
    previous_battle['post_initial'] = -previous_battle['post_initial'] + previous_battle['power']
    previous_battle['pre_acquired'] = 0
    for battle in backward_path[1:]:
        battle['pre_initial']= previous_battle['post_initial']
        battle['pre_acquired'] = previous_battle['post_acquired']
        battle['post_initial'] = battle['pre_initial'] - battle['post_initial']
        previous_battle = battle
    return backward_path

def pick_battle_with_min_power(level_info, battle_before_this_one):
    """
    Choose battle that requires the least amount of bullets
    (the one with the least power)
    """
    #This is a relatively easy one to pick.  What this ends up being
    # is a way to stage the next battle state
    # min_power, battle_index = min((powers[0][i], i) for i in xrange(len(powers[0])))


    battle_results = []

    for i, (power, bullet) in enumerate (level_info):
        battle_result = {"battle_index": i, "power":power, "post_acquired":bullet }
        battle_result["pre_initial"]=battle_result["post_initial"]=battle_before_this_one["post_initial"]
        battle_result["pre_acquired"]=battle_before_this_one["post_acquired"]

        if battle_before_this_one["post_acquired"] < power:
            battle_result["post_initial"] += (power - battle_before_this_one["post_acquired"])

        battle_result["pre_total"] = battle_before_this_one["post_initial"] + battle_before_this_one["post_acquired"]
        battle_results.append(battle_result)
    # -post_acquired to get the max value for post acquired in the event of a tie
    # min_set = min([(x['power'], -x['post_acquired'], i) for i, x in enumerate(battle_results)])

    #The order of precedence is:
    #pick the minimum delta in acquired, and if there is a tie, pick the one that provides the best 'post acquired'

    min_set = min([(x['post_initial']-x['pre_initial'], -x['post_acquired'], i) for i, x in enumerate(battle_results)])
    return battle_results[min_set[2]]

    #min_set = min([(x['power'],i) for i, x in enumerate(battle_results)])
    #return battle_results[min_set[1]]

def pick_battle_with_min_bullets(level_info, battle_after_this_one):
    """
    Chooses battle that requires the least amount of bullets to start
    returns battle state
    """
    # for each possible battle, calculate as much of the state as possible
    battle_results = []
    for i, (power, bullet) in enumerate(level_info):
        battle_result = {"battle_index":i, "power":power, "post_acquired":bullet}

        # Let's start the calculation.   Things we can get from each battle
        # 'pre_initial',
        #'post_initial',  'post_acquired',
        #'pre_total', 'post_total'


        increment =  battle_after_this_one["pre_total"] - bullet
        initial_increment =  battle_after_this_one["power"]- bullet

        battle_result["pre_total"] = power #Need at least enough to defeat this enemy
        if increment > 0:
            battle_result["pre_total"] += increment

        battle_result["pre_initial"] = battle_result["post_initial"]= 0

        if initial_increment > 0:
            battle_result["pre_initial"] += initial_increment
            battle_result["post_initial"] -= initial_increment

        battle_results.append(battle_result)

    #Now I have all of the possible results.  Pick the one who's pre_initial is lowest.
    #in case of a tie, pick the next one whose pre_total is the lowest
    # This one seems to be less useful
    # min_set = min([(x['pre_total'], x['pre_initial'], i) for i, x in enumerate(battle_results)])
    min_set = min([(x['pre_initial'], x['pre_total'], i) for i, x in enumerate(battle_results)])
    return battle_results[min_set[2]]

###################################
if __name__ == '__main__':

    with open("SuperHeroOutput00.txt") as f:
        correct_answers = [int(line) for line in f]

    my_answers = []
    with open("SuperHeroInput00.txt") as f:
        tests = int(f.readline().strip())  # number of test cases
        for a0 in xrange(tests):
            powers = []
            bullets = []
            levels, enemies = map(int,
                                  f.readline().strip().split(' '))  # number of levels, number of enemies on each level
            for a1 in xrange(levels):
                powers.append(map(int, f.readline().strip().split(' ')))  # power
            for a2 in xrange(levels):
                bullets.append(map(int, f.readline().strip().split(' ')))  # bullets

            my_answer = get_min_bullets(levels, enemies, powers, bullets)
            if my_answer <> correct_answers[a0]:
                print "test {} is different: his {}, mine {}.  levels {}, enemies {} ".format(a0, correct_answers[a0], my_answer, levels, enemies)

            my_answers.append(my_answer)


"""
print len(correct_answers), len(my_answers)
for i, (his, mine) in enumerate(zip(correct_answers, my_answers)):
    print i, his, mine, his-mine

"""
#lots of correct answers, but some *way* off
# index 2 is off by 2

"""
test 2 is different: his 14, mine 12.  levels 44, enemies 9
test 15 is different: his 32, mine 28.  levels 24, enemies 5
test 19 is different: his 70, mine 20.  levels 45, enemies 3
test 33 is different: his 14, mine 13.  levels 36, enemies 5
test 37 is different: his 93, mine 77.  levels 8, enemies 4
test 38 is different: his 4, mine 1.  levels 10, enemies 11
test 39 is different: his 88, mine 42.  levels 7, enemies 2
test 43 is different: his 50, mine 15.  levels 28, enemies 4
test 48 is different: his 38, mine 20.  levels 20, enemies 2
test 56 is different: his 790, mine 475.  levels 36, enemies 1
test 60 is different: his 416, mine 336.  levels 16, enemies 1
"""
# Lets take test 39, 7 levels