

def func(array):
    time = 1
    result = arrar[0]
    i = 1
    while i <= len(array)-1:
        if array[i] == result:
            time += 1
            i += 1
        else:
            time -= 1
            if time == 0:
                result = array[i+1]
                time = 1
                i += 2
            else:
                i += 1

