
#strinf slicing
import re  # regular exp
def main():
    string = "yashod  p k o l he 345 34567 345678"
    print(string[0:8]+" "+string[8:]) #start : stop : take evry x charectore 
    print(string[1::2])

    print("white spcae count ", string.count(" "))
    print("count the numbers",len(re.sub("[^0-9]","",string))) # the sub is the substitite the 2nd parameter is replace in the place of the first parameter 
    print("coiunt of the latters ",len(re.sub("[^a-zA-Z]","",string)))
if __name__ == "__main__":
    main()