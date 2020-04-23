class question:
    def __init__(self,prompt,answer):
        self.prompt = prompt
        self.answer = answer
name = input('Enter your name:')
print("All the best: " + str(name))
question_prompt = [
"Who is the father of geometry? \n a) Aristotle\n b) Euclid \n c) Pythagoras \n d) Kpler \n ",
"Whem was telephone was invented? \n a) 1870s\n b) 1880s \n c) 1850s \n d) 1860s \n ",
"What's the only fruit to possess seeds on the exterior? \n a) Strawberry\n b) Pineapple \n c) Orange \n d) Kiwi \n ",
"Which crop is sown on the largest scale in india? \n a) Wheat\n b) Sugar \n c) Rice \n d) Maize \n ",
"The world smallest country is? \n a) Maldives\n b) Russia \n c) Canada \n d) Valtican City \n ",
"What is the world's most common religion? \n a) Muslim\n b) Hinduism \n c) Christianity \n d) Buddhism \n ",
"Durannd cup is associated with the game of? \n a) Cricket\n b) Football \n c) Hockey \n d) Volleyball\n ",
"20th Auguest is celebrated as? \n a) No Tobacco Day\n b) Sadbhavana divas \n c) Earth Day \n d) None of these \n ",
"15th January is celebrated as? \n a) Army day\n b) Ugadhi \n c) Teachers' day\n d) Republic day \n ",
"What Galileo invented? \n a) Pendulum clock\n b) Barometer \n c) Microscope \n d) Thermometer \n ",
]

questions = [question(question_prompt[0], "b"),
            question(question_prompt[1], "d"),
            question(question_prompt[2], "a"),
            question(question_prompt[3], "b"),
            question(question_prompt[4], "d"),
            question(question_prompt[5], "d"),
            question(question_prompt[6], "d"),
            question(question_prompt[7], "a"),
            question(question_prompt[8], "a"),
            question(question_prompt[9], "d"),
]
def test(questions):
    c = 0
    for q in questions:
        ans = input(q.prompt)
        if ans == q.answer:
            c +=1
    print(str(name)+ " got "+ str(c) + "/" +  str(len(questions)) + " correct")



test(questions)