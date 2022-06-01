# pressing a button returns one direction ("n", "s", "e" or "w")
# walking a block takes 1min
# create an app that returns True if the walk took exactly 10min and returned you to starting point

def ten_min_walk(walk):
    count_n = walk.count("n")
    count_s = walk.count("s")
    count_e = walk.count("e")
    count_w = walk.count("w")
    steps = count_w + count_e + count_s + count_n
    if count_w == count_e and count_s == count_n and steps == 10:
        return True
    else:
        return False


print(ten_min_walk(["w", "w", "e", "e", "w", "w", "e", "e", "s", "n"]))
