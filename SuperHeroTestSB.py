import SuperHero as sh
import SuperHeroBruteForce as bf

if __name__ == '__main__':

    with open("SuperHero39_input.txt") as f:
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

            my_answer = sh.get_min_bullets_backward(levels, enemies, powers, bullets)
            brute_force_answer = bf.getMinBulletsBruteForce(levels, enemies, powers, bullets)

    print 'test 39 is different: his 88, mine 42.  levels 7, enemies 2'
    print my_answer, ' my answer'
    print brute_force_answer, ' brute_force_answer'

"""
test 39 is different: his 88, mine 42.  levels 7, enemies 2
42  my answer
88  brute_force_answer

# well, where did I go wrong.
"""