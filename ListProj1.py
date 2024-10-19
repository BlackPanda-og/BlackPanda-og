Ques_List=["Who was the First President of India","Who was the First Person to Step On Moon","Who Proposed Theory of Relativity","Which is the Smallest Subatomic Partice discovered Till Date(including latest discovery)"]
Option_List=["A). John\nB). Rajendra Prasad\nC). Don\nD). Gone\n--------------","A). Neil Armstrong\nB). Buzz Aldrin\nC). Michael Collins\nD). Yuri Gagarin\n---------------",
    "A). Isaac Newton\nB). Albert Einstein\nC). Niels Bohr\nD). Galileo Galilei\n-------------------",
    "A). Electron\nB). Proton\nC). Neutron\nD). Quark\n--------------"
]
Ans_List=["Rajendra Prasad","Neil Armstrong","Albert Einstein","Quark"] 
Reward_List=[1000,5000,10000,100000]
for i in range(len(Ques_List)): # in this line the program is set to keep looping new ques till len of Ques_List is reached which is 4 as each ques is taken as 1 element
    print(Ques_List[i])
    print(Option_List[i])
    Ans=str(input("Enter Correct Ans: "))
    if Ans_List[i].lower() == Ans.lower():
        print("Congrats You Won",Reward_List[i])
        ch =str(input("Would You Like To Continue: Y/N: "))
        if ch.upper()=='Y':
            continue
        else:
            print("Thanks For Playing\n-------------------")
            break
    else:
        print("Wrong Ans!!!")
        break
