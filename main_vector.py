from LA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([3, 4])
    print(vec)
    print(len(vec))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))
    vec2 = Vector([3, 7])

    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    # vec_wrong = Vector([1, 2, 3])
    # print("{} - {} = {}".format(vec, vec_wrong, vec - vec_wrong))

    print("{} * {} = {}".format(vec, [2.5], vec * [2.5]))
    print("{} * {} = {}".format(2, vec, 2 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    zero2 = Vector.zero(2)
    print(zero2)

    print("norm({}) = {}".format(vec, vec.norm()))

    print("normalize {} is {}".format(vec, vec.normalize()))
    print(vec.normalize().norm())

    print("{} / {} = {}".format(vec, 2, vec / 2))
    print(zero2.normalize())

    print("{} · {} = {}".format(vec, vec2, vec.dot(vec2)))

    print("{} * {} = {}".format(vec, vec2, vec * vec2))
