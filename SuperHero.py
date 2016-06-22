# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


###################################
# Get optimal starting point, that defeats enemy an has enough to defeat next enemy
def what_should_player_start_with(power, bullets, next_enemy_power):
    """
    Returns the best case scenario of what a player should start with
    In order to beat the next enemy
    power = enemy power
    bullets = enemy bullets
    next_enemy_power = next enemys power
    """
    # start with aquired
    ret = power  # have to have enough to defeat the enemy
    # In order to defeat this enemy, the sum needs to be greater than or equal to 'power'
    # and there needs to be enough left over to defeat the next enemy
    increment = next_enemy_power - bullets
    if increment > 0:
        ret = ret + increment

    return ret


###################################
def pick_the_best_battle(ps, bs, ml):
    """
    Returns the starting bullets for the battle is the least amount of the ammunition required
    in order to defeat the next level.

    ps: array of powers for the level
    bs:  array of bullets for the level
    ml: minimum_for_next_level:  minimum ammunition needed to defeat next level
    """
    ret = []
    for i, (power, bullet) in enumerate(zip(ps, bs)):
        bullets_needed = what_should_player_start_with(power, bullet, ml)
        # print (bullets_needed)
        ret.append(bullets_needed)

    # The best one is the one is the battle that has to *start*
    # with the lowest in order to be larger than ml
    return min(ret)


###################################
def get_min_bullets_backward(levels, enemies, powers, bullets):
    min_bullets = min(powers[levels - 1])
    for level in reversed(xrange(levels - 1)):
        power_for_level = powers[level]
        bullet_for_level = bullets[level]
        min_bullets = pick_the_best_battle(power_for_level, bullet_for_level, min_bullets)
        # print min_bullets

    return min_bullets
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
    print get_min_bullets_backward(levels, enemies, powers, bullets)
    print get_min_bullets_backward(levels2, enemies2, powers2, bullets2)

