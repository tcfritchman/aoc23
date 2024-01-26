import math

test = [
{
        "time": 7,
        "distance": 9
    },
    {
        "time": 15,
        "distance": 40
    },
    {
        "time": 30,
        "distance": 200
    }
]

input_1 = [
    {
        "time": 59,
        "distance": 543
    },
    {
        "time": 68,
        "distance": 1020
    },
    {
        "time": 82,
        "distance": 1664
    },
    {
        "time": 74,
        "distance": 1022
    }
]


def calculate_distance(time_held, max_time):
    return (max_time - time_held) * time_held


def part_1(data):
    results = []
    for race in data:
        distances = [calculate_distance(n, race["time"]) for n in range(1, race["time"])]
        count_of_wins = len([d for d in distances if d > race["distance"]])
        results.append(count_of_wins)
    return math.prod(results)


def part_2(data):
    return 0


if __name__ == '__main__':
    # print("Part 1: %d" % (part_1(test)))
    print("Part 1: %d" % (part_1(input_1)))
    # print("Part 2: %d" % (part_2(input_2)))
