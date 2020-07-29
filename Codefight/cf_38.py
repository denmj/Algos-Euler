"""
Caring for a plant can be hard work, but since you tend to it regularly, you have a plant that grows consistently.
Each day, its height increases by a fixed amount represented by the integer upSpeed. But due to lack of sunlight,
the plant decreases in height every night, by an amount represented by downSpeed.

Since you grew the plant from a seed, it started at height 0 initially. Given an integer desiredHeight,
your task is to find how many days it'll take for the plant to reach this height.

Example

For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be
growingPlant(upSpeed, downSpeed, desiredHeight) = 10.

"""


def growingPlant(upSpeed, downSpeed, desiredHeight) -> (
        "Number of days"):
    day_count = 0
    init_height = 0
    while init_height < desiredHeight:
        init_height += upSpeed
        print("day: ", init_height)
        if init_height >= desiredHeight:
            day_count += 1
            break
        else:
            init_height -= downSpeed
            print("night: ", init_height)

        day_count += 1
        print("day:", day_count)

    return day_count


print(growingPlant(10, 9, 4))

print(growingPlant.__annotations__)
