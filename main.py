import random
words=["rainbow","blood","death","yoyo","fun","joy","happy","joyful","love","Depression"]
print(len(words))
word=random.choice(words)

p1=input("Enter player 1 name:")
p2=input("Enter player 2 name:")
p1s=0
p2s=0
a=int(len(words)/2)
b=a*2
for turn in range(b):
    if(turn%2==0):
        word=random.choice(words)
        jumbled="".join(random.sample(word,len(word)))
        print(p1,"your turn")
        print(f"The jumnled word is {jumbled}")
        ans=input("Whats on ur mind?\n")
        if(ans==word):
            p1s=p1s+1
            print("your score is:",p1s)
        else:
            print("Better luck next time, I thought",word)
        c=int(input("press 1 to continue,0 to exit\n"))
        if c==0:
            break
        else:
            continue
    else:
        word=random.choice(words)
        jumbled="".join(random.sample(word,len(word)))
        print(p2,"your turn")
        print(f"The jumnled word is {jumbled}")
        ans=input("Whats on ur mind?\n")
        if(ans==word):
            p2s=p2s+1
            print("your score is:",p2s)
        else:
            print("Better luck next time, I thought",word)
        c=int(input("press 1 to continue,0 to exit\n"))
        if c==0:            
            break
        else:
            continue


print(p1,"your score:",p1s)
print(p2,"your score:",p2s)
print("Thank you for playing")
    
