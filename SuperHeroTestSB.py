import SuperHero as sh
import os
import SuperHeroBruteForce as bf

if __name__ == '__main__':
    files = []
    files.append(os.path.join("SuperHeroFiles", "SuperHeroIndividualInput39.txt"))
    files.append(os.path.join("SuperHeroFiles", "SuperHeroIndividualInput67.txt"))
    files.append(os.path.join("SuperHeroFiles", "SuperHeroIndividualInput40.txt"))
    files.append(os.path.join("SuperHeroFiles", "SuperHeroIndividualInput38.txt"))
    files.append(os.path.join("SuperHeroFiles", "SuperHeroIndividualInput60.txt"))
    for file in files:
        print '\n', file
        with open(file) as f:
            tests, correct_score = map(int,(f.readline().strip().split(' ')))  # number of test cases
            for a0 in xrange(tests):
                powers = []
                bullets = []
                levels, enemies = map(int,
                                      f.readline().strip().split(' '))  # number of levels, number of enemies on each level
                for a1 in xrange(levels):
                    powers.append(map(int, f.readline().strip().split(' ')))  # power
                for a2 in xrange(levels):
                    bullets.append(map(int, f.readline().strip().split(' ')))  # bullets

                my_answer = sh.get_min_bullets(levels, enemies, powers, bullets)
                #brute_force_answer = bf.getMinBulletsBruteForce(levels, powers, bullets)

    #print 'test 39 is different: his 88, mine 42.  levels 7, enemies 2'

        print my_answer, ' my answer, and it should be ', correct_score
    #print brute_force_answer, ' brute_force_answer'

"""
test 39 is different: his 88, mine 42.  levels 7, enemies 2
42  my answer
88  brute_force_answer

# well, where did I go wrong.  Brute force agrees.
"""
"""
Test
2743  my answer, but it should be  416
416  brute_force_answer

"""