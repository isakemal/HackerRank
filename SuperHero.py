# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

# battle_state = namedtuple('battle_state', 'level_index', 'battle_index', 'pre_initial',
#                                            'post_initial', 'pre_acquired', 'post_acquired',
#                                            'pre_total', 'post_total' )

def get_min_bullets(levels, enemies, powers, bullets):
    """
    The way this works is that it creates several pathways through the battles
    Once it has all of the pathways completed, it will take the best segments from each pathway
    to build the final pathway and final score
    """
    backward = get_backward_path(levels, enemies, powers, bullets)
    forward = get_forward_path(levels, enemies, powers, bullets)

    """
    # DEBUG
    print "backward"
    for path in backward:
        print path
    """
    """
    print "forward"
    for path in forward:
        print path
    # DEBUG
    """

    # Now I have two paths to compare
    # What I want to do is find all of the levels where they battle the same enemy
    # Where they exist, I want to pick the path where the "pre_initial" delta is least.

    # Find levels where battle_index is the same
    []


    return ('backward',backward[-1]["pre_initial"], 'forward', forward[-1]["pre_initial"])


def get_forward_path (levels, enemies, powers, bullets):
    """
    Identifies the best path starting with first battle and working forwards
    battle choice is based on minimum power
    """
    forward_path = []

#    min_power, battle_index = min((powers[0][i], i) for i in xrange(len(powers[0])))
    current_battle = {"level_index": -1, "power": 0, "pre_initial": 0, "post_initial": 0, "post_acquired": 0}

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
    for battle in backward_path[1:]:
        battle['pre_initial']= previous_battle['post_initial']
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
    #I could do it this way, but I want to capture all of the battles

    for i, (power, bullet) in enumerate (level_info):
        battle_result = {"battle_index": i, "power":power, "post_acquired":bullet }
        battle_result["pre_initial"]=battle_result["post_initial"]=battle_before_this_one["post_initial"]
        if battle_before_this_one["post_acquired"] < power:
            battle_result["post_initial"] += (power - battle_before_this_one["post_acquired"])

        battle_results.append(battle_result)
    # -post_acquired to get the max value for post acquired in the event of a tie
    # min_set = min([(x['power'], -x['post_acquired'], i) for i, x in enumerate(battle_results)])
    min_set = min([(x['power'],i) for i, x in enumerate(battle_results)])
    return battle_results[min_set[1]]

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
def defeatEnemy(power, bullets, pre_initial, pre_acquired):
    """
    Returns post_initial and post_acquired after defeating enemy
    """

    # always true
    post_acquired = bullets

    # Post initial will depend on whether we had enough acquired bullets for the battle
    post_initial = pre_initial

    # This will go negative if we don't know what the pre_initial is (that is, if we are going backward)
    if pre_acquired < power:
        post_initial = post_initial - (power - pre_acquired)

    return post_initial, post_acquired




###################################
# Get optimal starting point, that defeats enemy an has enough to defeat next enemy
def what_should_player_start_with(power, bullet, minimum_needed_for_next, next_enemy_power):
    """
    Returns the best case scenario of what a player should start with
    In order to beat the next enemy
    power = enemy power
    bullets = enemy bullets
    next_enemy_power = next enemy's power
    start = the amount of the starting ammo you need to retain
        even if there is sufficient bullets remaining
    """
    pre_total = power  # have to have enough to defeat the enemy

    # Ideally, net_bullets will be sufficient for the next enemy, which means
    # I don't have to use any of the ones I started with

    # In order to defeat this enemy, the sum needs to be greater than or equal to 'power'
    # and there needs to be enough left over to defeat the next enemy
    increment = minimum_needed_for_next - bullet
    initial_increment = next_enemy_power - bullet

    pre_initial = 0

    if increment > 0:
        pre_total = pre_total + increment

    if initial_increment > 0:
        pre_initial = initial_increment


    # working backwards, start get's used when there aren't
    # enough bullets in current level to defeat next level
    return pre_initial, pre_total


###################################
def pick_the_best_battle(ps, bs, ml, np):
    """
    Returns the starting bullets for the battle is the least amount of the ammunition required
    in order to defeat the next level.

    ps: array of powers for the level
    bs:  array of bullets for the level
    ml: minimum_for_next_level:  minimum ammunition needed to defeat next level
    np: next enemy power:  power of next enemy (different than minimum needed for next level)
    """
    ret = []

    for i, (power, bullet) in enumerate(zip(ps, bs)):
        start_to_retain, bullets_needed  = what_should_player_start_with(power, bullet, ml, np )
        # print (bullets_needed)
        ret.append(((start_to_retain, bullets_needed, power),i))

    # Need to order by start_to_retain and then bullets needed
    # The best one is the one is the battle that has to *start*
    # with the lowest in order to be larger than ml
    return min(ret)


###################################
def get_min_bullets_backward(levels, enemies, powers, bullets):
    min_bullets, battle_index =  min( (powers[levels - 1][i],i) for i in xrange(len(powers[levels - 1])))
    next_enemy_power = min_bullets
    start_to_retain = 0
    for level in reversed(xrange(levels - 1)):
        power_for_level = powers[level]
        bullet_for_level = bullets[level]
        (start, min_bullets, next_enemy_power), battle_index = pick_the_best_battle(power_for_level, bullet_for_level, min_bullets, next_enemy_power)
        start_to_retain = start_to_retain + start
        print level, ' level - ', battle_index, ' battle_index - ', min_bullets, ' min bullets - ', start_to_retain, ' start_to_retain'
        # print min_bullets

    return  powers[0][battle_index] + start_to_retain

###################################
if __name__ == '__main__':

    levels = 3
    enemies = 3
    powers = []
    bullets = []
    powers.append(map(int,"3 2 1".split(' '))) #power
    powers.append(map(int,"1 2 3".split(' '))) #power
    powers.append(map(int,"3 2 1".split(' '))) #power

    bullets.append(map(int,"1 2 3".split(' '))) #bullets
    bullets.append(map(int,"3 2 1".split(' '))) #bullets
    bullets.append(map(int,"1 2 3".split(' '))) #bullets

    levels2 = 3
    enemies2 = 3
    powers2 = []
    bullets2 = []
    powers2.append(map(int,"3 2 5".split(' '))) #power
    powers2.append(map(int,"8 9 1".split(' '))) #power
    powers2.append(map(int,"4 7 6".split(' '))) #power

    bullets2.append(map(int,"1 1 1".split(' '))) #bullets
    bullets2.append(map(int,"1 1 1".split(' '))) #bullets
    bullets2.append(map(int,"1 1 1".split(' '))) #bullets
    """
    tests = int(raw_input().strip())  # number of test cases

    for a0 in xrange(tests):
        powers = []
        bullets = []
        levels, enemies = map(int, raw_input().strip().split(' '))  # number of levels, number of enemies on each level
        for a1 in xrange(levels):
            powers.append(map(int, raw_input().strip().split(' ')))  # power
        for a2 in xrange(levels):
            bullets.append(map(int, raw_input().strip().split(' ')))  # bullets
    """
    # print get_min_bullets_backward(levels, enemies, powers, bullets)
    # print get_min_bullets_backward(levels2, enemies2, powers2, bullets2)

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

            my_answer = get_min_bullets_backward(levels, enemies, powers, bullets)
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