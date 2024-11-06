length=[]
words=[]
def rebuild_sentence(words,length):
    for i in range(len(length)):
        for j in range (length[i]):
            print(words[i][j],end="")
        print(end=" ")
            
rebuild_sentence( [ "the", "sky", "is", "blue" ] , [ 3, 2, 2, 1 ] ) 
