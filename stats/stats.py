import collections
import statistics

vector = [34000, 45000, 40000, 33000, 51000, 100000, 65000, 431000, 19000, 86000]


def mean(vector):
    return sum(vector) / len(vector)


def mode(vector):
    vector = collections.Counter(vector)
    return max(vector, key=vector.get) 



def median(vector):
    vector = sorted(vector)
    len2 = len(vector)//2
    return vector[len2] if len(vector) % 2 == 1 else mean([vector[len2-1], vector[len2]])
    #vector = sorted(vector)
    #if len(vector) % 2 >= 1:
    #    return vector[math.ceil(len(vector) / 2) - 1]
    #return mean([vector[math.ceil(len(vector) / 2 - 1)], vector[math.floor(len(vector) / 2) - 1]])


def range(vector):
    return max(vector) - min(vector)


def mad(vector):
    vector = sorted(vector)
    x = []
    med = mean(vector)
    # print(med)
    for i in vector:
        x.append(abs(med - i))

    return mean(x)


def IQR(vector):
    len2 = len(vector) // 2
    vector = sorted(vector)
    q3 = median(vector[-len2:])
    q1 = median(vector[0:len2])
    return q1, q3, q3-q1


if mad([1, 1, 1, 2, 2, 3, 3, 5, 7, 9]) == 2.16:
    print("The MAD of this data is: " + str(mad(vector)))

print("The IQR of this data is: " + str(IQR(vector)))

if sorted([0, 5, 10]) == [0, 5, 10]:
    print("This data sorted is " + str(sorted(vector)))

if mean([0, 5, 10, 20, 25]) == 12:
    print("The mean of this data is " + str(mean(vector)))

if mode([1, 1, 1, 2]) == 1:
    print("The mode of this data is " + str(mode(vector)))

if median([1, 2, 3]) == 2:
    print("The median of this data is " + str(median(vector)))

if range([6, 7, 8, 9, 10]) == 4:
    print("The range of this data is " + str(range(vector)))

print("test")

