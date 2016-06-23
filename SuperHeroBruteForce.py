# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys


###################################
# I'm gonna brute force it for now
def defeatEnemy(power, bullets, ammunition_started, ammunition_aquired):
    """
    Returns new set of ammunition after defeating enemy
    Ammunition_started could be negative
    """
    # start with aquired
    _acquired = _power = 0

    _started = ammunition_started
    _power = power - ammunition_aquired

    if _power > 0:
        _started = ammunition_started - _power

    _acquired = bullets  # even if there is a surplus, we can't carry it forward

    return _started, _acquired


###################################
def get_battle_combinations(powers, bullets, players):
    # come back and make this a list comprehension
    ret = []
    for i, (power, bullet) in enumerate(zip(powers, bullets)):
        for player in players:
            ret.append((defeatEnemy(power, bullet, player[0][0], player[0][1]), player[1] + str(i)))

    return ret


###################################
def getMinBulletsBruteForce(levels, powers, bullets):
    plays = [((0, 0), '~')]

    for level in xrange(levels):
        power_for_level = powers[level]
        bullet_for_level = bullets[level]
        plays = get_battle_combinations(power_for_level, bullet_for_level, plays)

    for p in plays:
        print p[0][0], '\t', p[0][1], '\t', p[1]
    return -max(plays)[0][0]


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

    print getMinBulletsBruteForce(levels, powers, bullets)

# for chuckles, let's see how bruteforce compares
# ACTUALLY, DON'T.  IT QUICKLY SOAKS ALL MEMORY AND THEN SOME!
"""
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

        my_answer = getMinBulletsBruteForce(levels, enemies, powers, bullets)
        if my_answer <> correct_answers[a0]:
            print "test {} is different: his {}, mine {}.  levels {}, enemies {} ".format(a0, correct_answers[a0],
                                                                                          my_answer, levels, enemies)

        my_answers.append(my_answer)
"""