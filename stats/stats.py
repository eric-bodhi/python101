import collections

vector = [10, 15, 20, 30, 50]


def mean(vector):
    return sum(vector) / len(vector)


def mode(vector):
    vector = collections.Counter(vector)
    return max(vector, key=vector.get)


def median(vector):
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
    return median(vector[-len2:]) - median(vector[0:len2])


if mad([1, 1, 1, 2, 2, 3, 3, 5, 7, 9]) == 2.16:
    print("The MAD of this data is: " + str(mad(vector)))

if IQR([1, 3, 1,6, 9])
print("The IQR of this data is: " + str(IQR(vector)))
print("This data sorted is " + str(sorted(vector)))
print("The mean of this data is " + str(mean(vector)))
print("The mode of this data is " + str(mode(vector)))
print("The median of this data is " + str(median(vector)))
print("The range of this data is " + str(range(vector)))