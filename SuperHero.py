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
    for (power, bullet) in zip(powers, bullets):
        for player in players:
            ret.append(defeatEnemy(power, bullet, player[0], player[1]))

    return ret


###################################
def getMinBulletsBruteForce(levels, enemies, powers, bullets):
    plays = [(0, 0)]

    for level in xrange(levels):
        power_for_level = powers[level]
        bullet_for_level = bullets[level]
        plays = get_battle_combinations(power_for_level, bullet_for_level, plays)

    return -max(plays)[0]


###################################
if __name__ == '__main__':
    print defeatEnemy(1, 1, 1, 0) == (0, 1)
    print defeatEnemy(1, 1, 1, 1) == (1, 1)
    print defeatEnemy(1, 2, 1, 1) == (1, 2)
    print defeatEnemy(2, 1, 1, 1) == (0, 1)
    print defeatEnemy(2, 2, 1, 1) == (0, 2)
    print defeatEnemy(2, 1, 1, 2) == (1, 1)
    print defeatEnemy(3, 1, 1, 2) == (0, 1)
    print defeatEnemy(5, 1, 1, 2) == (-2, 1)

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
    print getMinBulletsBruteForce(levels, enemies, powers, bullets)
    print getMinBulletsBruteForce(levels2, enemies2, powers2, bullets2)

