if __name__ == '__main__':
    l = []
    ls = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
        ls.append(score)
            
    s = sorted(set(ls),key = lambda x : [x])
    
    Alphabet = []
    
    for i in range(len(l)):
        if l[i][1] == s[1]:
            Alphabet.append(l[i][0])
    
    Alphabet.sort()
                
    for name in Alphabet:
        print(name) 
        
    
