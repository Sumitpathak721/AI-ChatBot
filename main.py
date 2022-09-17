#Agenda---> Creating AI chatbot who can work as per past data and multiple way you as the same question
while True:
    questions_r=open("questions.txt",'r')
    answers_r = open("answers.txt","r")
    user_question = input("Question:").lower()
    user_question_lst = user_question.split()
    if(user_question=="quit"):
        break
    else:
        max_possibility = 0
        min_length_question = 1e+10
        found_question_lst = []
        questions_r_lst = questions_r.readlines()
        for question in questions_r_lst:
            question_db=(question.rstrip("\n")).lower()
            question_db_lst = question_db.split()
            possibility = 0
            for word in user_question_lst:
                if word in question_db_lst:
                    if user_question_lst.count(word)>question_db_lst.count(word):
                        possibility+=question_db_lst.count(word)
                    else:
                        possibility+=user_question_lst.count(word)
            if possibility==max_possibility:
                if len(question_db)<min_length_question:
                    min_length_question = len(question_db)
                    found_question_lst=[[question_db,questions_r_lst.index(question)]]
                if len(question_db)==min_length_question:
                    found_question_lst.append([question_db,questions_r_lst.index(question)])
            elif possibility>max_possibility:
                min_length_question=len(question_db_lst)
                found_question_lst=[[question_db,questions_r_lst.index(question)]]
                max_possibility=possibility
        answers_r_lst = answers_r.readlines()
        if len(found_question_lst)==1:
            print("Its seems like you search for this question")
            print("Question:"+found_question_lst[0][0])
            print("Answer:"+answers_r_lst[found_question_lst[0][1]])
            response = input("Is this answer correct or not (type y/n for response)")
            if response=="y":
                print("Thanks")
            else:
                print("Could you please provide me its answer for future usage..")
                user_answer = input("Answer write here-->")
                if(user_answer == "" or user_answer == " "):
                    print("Don't interupt data :/")
                else:
                    questions_a = open("questions.txt","a")
                    answers_a = open("answers.txt","a")
                    questions_a.write(user_question+"\n")
                    answers_a.write(user_answer+"\n")
                    questions_a.close()
                    answers_a.close()
                    print("Thanks for showing your kindness....:)")
        elif len(found_question_lst)>1:
            print("There is multiple question possibility choose which one belong to yours..")
            for i in found_question_lst:
                print(f"Question{found_question_lst.index(i)+1}:"+i[0])
            user_question_query=input("Press the question no. or just enter if no match found:")
            if user_question_query=="":
                def no_match():
                    print("I'm sorry to say but... I don't have answer for this question...:(")
                    print("Could you please provide me its answer for future usage")
                    user_answer = input("Answer write here-->")
                    if(user_answer == "" or user_answer == " "):
                        print("Don't interupt data :/")
                    else:
                        questions_a = open("questions.txt","a")
                        answers_a = open("answers.txt","a")
                        questions_a.write(found_question_lst[user_question_query-1][0]+"\n")
                        answers_a.write(user_answer.lower()+"\n")
                        questions_a.close()
                        answers_a.close()
                        print("Thanks for showing your kindness...:)")
                no_match()
            else:
                user_question_query=int(user_question_query)
                print("Question:"+found_question_lst[user_question_query-1][0])
                print("Answer:"+answers_r_lst[found_question_lst[user_question_query-1][1]])
                questions_a = open("questions.txt","a")
                answers_a = open("answers.txt","a")
                questions_a.write(found_question_lst[user_question_query-1][0]+"\n")
                answers_a.write(answers_r_lst[found_question_lst[user_question_query-1][1]])
                questions_a.close()
                answers_a.close()
    questions_r.close()
    answers_r.close()