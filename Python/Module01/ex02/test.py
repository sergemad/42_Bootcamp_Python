from vector import Vector

def main():
    v = Vector(5)
    v1 = Vector((5,10))
    print(v / 5)
    print(v * v1)
    print(v + v1)
    print(v - v1)
    print(v.T())

main()