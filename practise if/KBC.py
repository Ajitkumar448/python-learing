Questions = ["who is PM of india",       #KBC using list
              "t20 worldcup winner 2026",
              "Capital of Russia",
              "red planet",
              "who wrote Ramayana"]

Answers = ["Narendra Modi",
           "India",
           "Moscow",
           "Mars",
           "Tulsi Das"]

Prizes  = [1000,
           2000,
           5000,
           10000,
           20000]

def kbc():
    totalmoney= 0
    for i in range(len(Questions)):
        print(Questions[i])
        user_answer= input("enter answer: ").lower()
        if user_answer == Answers[i].lower():
         print("Correct answer")
         totalmoney= Prizes[i]
        else:
         print("Wrong answer")
         break
    print(f"you are taking home ${totalmoney}")
kbc()

Question =[{"question":"Capital of India", # KBC by list of dictonary
            "answer":"delhi",
            "prize":1000 },
            {"question":"President of India",
             "answer":"Droupdi Murmur",
             "prize":2000}]
def kbc():
    totalmoney = 0
    for q in Question:
        print(q["question"])
        user_answer= input("enter answer: ")
        if user_answer.lower() == q["answer"].lower():
            print("correct answer")
            totalmoney = q["prize"]
        else:
            print("Wrong answer")
            break
    print(f"you are taking ${totalmoney}")

kbc()


