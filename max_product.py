#
#  Problem: Given an array that contains both positive and negative integers, find the k pairs of distinct elements which are the maximum product of such array
#

def find_max_product(number_array, pairs_to_find):
    pairs = []
    for i in range(pairs_to_find):
        pairs.append((None,None,None))
    none_location = 0
    for i in range(len(number_array)-1):
        for j in range(i+1, len(number_array)):
            if none_location < pairs_to_find:
                pairs[none_location] = (number_array[i],number_array[j],number_array[i]*number_array[j])
                none_location += 1
                continue
            for k in range(pairs_to_find):
                if number_array[i] * number_array[j] > pairs[k][2]:
                    pairs[k] = (number_array[i],number_array[j],number_array[i]*number_array[j])
                    break
    return pairs


print find_max_product([-5,-2,-3,-1,1,2,3],3)
