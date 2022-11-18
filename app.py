import json
f=open("quiz-data.json")
data=json.load(f)
print(data)




total_ques=0
correct_ans=0


for ques in data:

    print(ques.get("question"))

    print("options")

    choices=ques.get("choices")

    for i,choice in enumerate(choices):

        print(i,":",choice)

    user_choice=int(input("enter your choice : "))
    total_ques+=1
    if user_choice>3 or user_choice<0:
        print("Invalid")
    else:
        if choices[user_choice]==ques.get("correct_ans"):
            print("Your answer is correct : ",ques.get("correct_ans"))
            correct_ans+=1
        else:
            print("Your answer is wrong")
            print("The correct answer is : ",ques.get("correct_ans"))

    


    print()

print("Total Attempted ques:",total_ques)
print("Total correct answers:",correct_ans)