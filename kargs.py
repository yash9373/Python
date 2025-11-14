
def avarafe(**kargs):
    values = list(kargs.values())
    avg =  sum(values)/len(values)
    return avg


def main():
    avg = avarafe(nums=1,nus=6)
    string = "this is the string for the temp"
    new_string = string.split()
    print(new_string)    
    joined_string = "fuck ".join(new_string)
    print(joined_string)

if __name__ == "__main__":
    main()