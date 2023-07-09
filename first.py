def log_maker(base,value):
    dummy_1=value
    dummy =1
    if base==value :
        return dummy
    else :
        for i in range(int(value/base)):
            if dummy_1 >=1:
                if (dummy_1/base) == 1.0 :
                    return dummy
                else:
                    dummy+=1
                    dummy_1=(dummy_1/base)
                    continue
            else:
                return "invalid"

answer = log_maker(4,64)
print("-----",answer,"-----")