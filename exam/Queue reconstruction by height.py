def queuekey(person):
    height, count = person
    return -height, count

def queue_2(people):
    result = []
    for person in sorted(people, key=queuekey):
        _, count = person
        result.insert(count, person)
    print(result)
queue_2([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
queue_2([[12,0],[6,3],[3,4],[9,2], [11,1],[1,5]])
queue_2([ [2,4], [5,1], [3,3], [1,5], [4,2], [6,0]])