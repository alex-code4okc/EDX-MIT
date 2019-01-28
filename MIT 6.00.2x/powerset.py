def powerSet(items):
    N = len(items)
    # enumerate the 2**N possible combinations
    for i in range(2**N):
        combo = []
        for j in range(N):
            # test bit jth of integer i
            print('i: ',i,'j: ',j)
            if (i >> j) % 2 == 1:
                combo.append(items[j])
                print(items[j])
        yield combo
