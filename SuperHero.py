# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

###################################
def defeatEnemy(power, bullets, ammunition_started, ammunition_acquired):
    """
    Returns new set of ammunition after defeating enemy
    Ammunition_started could be negative
    """
    # start with aquired
    _acquired = _power = 0

    _started = ammunition_started
    _power = power - ammunition_acquired

    if _power > 0:
        _started = ammunition_started - _power

    _acquired = bullets  # even if there is a surplus, we can't carry it forward

    return _started, _acquired

###################################
# Get optimal starting point, that defeats enemy an has enough to defeat next enemy
def what_should_player_start_with(power, bullets, minimum_needed_for_next, next_enemy_power):
    """
    Returns the best case scenario of what a player should start with
    In order to beat the next enemy
    power = enemy power
    bullets = enemy bullets
    next_enemy_power = next enemy's power
    start = the amount of the starting ammo you need to retain
        even if there is sufficient bullets remaining
    """
    ret = power  # have to have enough to defeat the enemy

    # Ideally, net_bullets will be sufficient for the next enemy, which means
    # I don't have to use any of the ones I started with

    # In order to defeat this enemy, the sum needs to be greater than or equal to 'power'
    # and there needs to be enough left over to defeat the next enemy
    increment = minimum_needed_for_next - bullets
    start_increment = next_enemy_power - bullets
    # print bullets, ' acquired ', increment, ' increment'
    start = 0
    if increment > 0:
        ret = ret + increment
    if start_increment > 0:
        start = start_increment


    # working backwards, start get's used when there aren't
    # enough bullets in current level to defeat next level

    return start, ret


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