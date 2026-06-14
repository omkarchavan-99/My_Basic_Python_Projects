questions = [
{
"prompt": "1.Which planet in our solar system has the shortest day?",
"options": ["A) Mars", "B) Saturn", "C) Jupiter", "D) Mercury"],
"answer": "C"
},
{
"prompt": "2.Who was the first Indian woman to win a Nobel Prize?",
"options": ["A) Sarojini Naidu", "B) Indira Gandhi", "C) Mother Teresa", "D) Kalpana Chawla"],
"answer": "C"
},
{
"prompt": "3.What is the capital city of Australia?",
"options": ["A) Sydney", "B) Melbourne", "C) Perth", "D) Canberra"],
"answer": "D"
},
{
"prompt": "4.Which element has the chemical symbol 'K'?",
"options": ["A) Krypton", "B) Potassium", "C) Calcium", "D) Cobalt"],
"answer": "B"
},
{
"prompt": "5.Who wrote the famous book 'The Discovery of India'?",
"options": ["A) Mahatma Gandhi", "B) Rabindranath Tagore", "C) Jawaharlal Nehru", "D) B. R. Ambedkar"],
"answer": "C"
},
{
"prompt": "6.Which is the only continent that lies entirely in the Southern Hemisphere?",
"options": ["A) Africa", "B) South America", "C) Australia", "D) Antarctica"],
"answer": "C"
},
{
"prompt": "7.How many players are there in a standard cricket team on the field?",
"options": ["A) 9", "B) 10", "C) 11", "D) 12"],
"answer": "C"
},
{
"prompt": "8.Which Mughal emperor built the Taj Mahal?",
"options": ["A) Akbar", "B) Aurangzeb", "C) Humayun", "D) Shah Jahan"],
"answer": "D"
},
{
"prompt": "9.Which is the largest internal organ in the human body?",
"options": ["A) Heart", "B) Brain", "C) Liver", "D) Lungs"],
"answer": "C"
},
{
"prompt": "10.What is the SI unit of electric current?",
"options": ["A) Volt", "B) Watt", "C) Ohm", "D) Ampere"],
"answer": "D"
}
]

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer = input("Enter your answer (A, B, C, D): ").upper()
        if answer == question['answer']:
            print("Correct Answer, Hooray!!\n")
            score += 1
        else:
            print("Wrong, LOSERR!!! The Correct Answer is", question['answer'], "\n")
    print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)