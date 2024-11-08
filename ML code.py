import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

df = pd.read_csv('/kaggle/input/screen-time-dataset/sample_screen_time_dataset.csv')

X = df[['Age', 'Study_Hours', 'Emotional_Score']]
y = df['Screen_Time']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

def predict_screen_time(age, study_hours, emotional_score):
    input_data = np.array([[age, study_hours, emotional_score]])
    predicted_screen_time = model.predict(input_data)
    return predicted_screen_time[0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)


def calculate_emotional_score(conversation_text):
    sentiment = TextBlob(conversation_text).sentiment.polarity  
    emotional_score = round(((sentiment + 1) / 2) * 9 + 1)
    return min(max(emotional_score, 1), 10)

def chatbot():
    print("Hello! I'm here to chat with you and help recommend a suitable amount of screen time.")
    
    age = int(input("Please enter your age: "))
    study_hours = float(input("How many hours did you study today? "))
    
    initial_questions = [
        "How was school today?",
        "How was your tuition session?",
        "How did the food taste today?",
        "How did your exam go?",
        "What was the best part of your day?",
        "Did you do anything fun today?",
        "How are you feeling about your friends?",
        "Was there something challenging today?",
        "What did you learn today?",
        "How did you spend your free time?"
    ]
    
    follow_up_questions = {
        "How was school today?": [
            "What did you learn today?", 
            "Did anything interesting happen in school?", 
            "How were your friends today?", 
            "Did you like your teachers today?", 
            "Was there a subject you really enjoyed?", 
            "How was the atmosphere in school?", 
            "Was there something challenging at school?", 
            "What part of school do you look forward to the most?", 
            "Did you have any group activities today?", 
            "Was there something you didn't like about school today?"
        ],
        "How was your tuition session?": [
            "What did you cover in tuition today?", 
            "Did you find the tuition session helpful?", 
            "How was your tutor today?", 
            "Was there a topic you struggled with?", 
            "How do you feel about your tuition progress?", 
            "Do you feel like you're learning a lot?", 
            "Was there a subject you enjoyed today?", 
            "Did you get to ask questions in class?", 
            "How was the pace of the lesson?", 
            "What do you want to focus on in the next session?"
        ],
        "How did the food taste today?": [
            "What did you have for lunch?", 
            "Did you like the food?", 
            "Was there something special about today's food?", 
            "Did you try something new today?", 
            "How was the taste compared to usual?", 
            "Was the food prepared well?", 
            "Was there anything you didn't like about the food?", 
            "How would you rate the food today?", 
            "Did you feel satisfied after eating?", 
            "Did you have any snacks today?"
        ],
        "How did your exam go?": [
            "How did you prepare for the exam?", 
            "Were there any tough questions?", 
            "Do you feel confident about your exam performance?", 
            "How much time did you spend studying?", 
            "Was there a particular subject you felt unsure about?", 
            "How did you manage your time during the exam?", 
            "What part of the exam did you find the hardest?", 
            "Was there something you wish you had studied more?", 
            "Do you feel like the exam was fair?", 
            "Are you looking forward to the results?"
        ],
        "What was the best part of your day?": [
            "What made it the best part?", 
            "Who were you with during that moment?", 
            "What did you enjoy the most about it?", 
            "Was it something spontaneous?", 
            "Did it involve a lot of fun?", 
            "Would you like to experience it again?", 
            "How did you feel at that moment?", 
            "Was it something you’ve been looking forward to?", 
            "Do you think it’ll be a highlight of your week?", 
            "What would make it even better next time?"
        ],
        "Did you do anything fun today?": [
            "What was the most fun thing you did?", 
            "Was it something you’ve done before?", 
            "Did you do it with friends or family?", 
            "What made it so fun?", 
            "Was it something spontaneous?", 
            "How did it make you feel?", 
            "Would you like to do it again?", 
            "Did you try something new?", 
            "Was it relaxing or adventurous?", 
            "How did you feel after doing it?"
        ],
        "How are you feeling about your friends?": [
            "Are you spending time with your friends lately?", 
            "What makes you feel good about your friendships?", 
            "Did you talk to anyone today?", 
            "How are your friendships growing?", 
            "Have you had any disagreements with friends recently?", 
            "What do you enjoy doing together with your friends?", 
            "Have you made any new friends?", 
            "Do you feel supported by your friends?", 
            "Do you hang out with them outside of school?", 
            "Is there a special friend you spent time with today?"
        ],
        "Was there something challenging today?": [
            "What made it challenging?", 
            "How did you feel about it?", 
            "Did you overcome it?", 
            "What was the hardest part?", 
            "How did you handle the challenge?", 
            "Did anyone help you with it?", 
            "Would you approach it differently next time?", 
            "Do you feel better about it now?", 
            "What did you learn from this challenge?", 
            "Did you feel like giving up at any point?"
        ],
        "What did you learn today?": [
            "Was it something new?", 
            "Was it related to your school subjects?", 
            "Did you find it interesting?", 
            "How do you feel about learning that?", 
            "Was it difficult or easy to understand?", 
            "Can you apply it in real life?", 
            "Did you discuss it with anyone?", 
            "How does it relate to what you already know?", 
            "Do you want to learn more about it?", 
            "Was there something you struggled with?"
        ],
        "How did you spend your free time?": [
            "Did you relax or do something active?", 
            "Was it a productive break?", 
            "How do you feel after spending your free time?", 
            "Did you enjoy the time you had?", 
            "Was it enough for you?", 
            "Would you have liked more free time?", 
            "Did you get to do something you enjoy?", 
            "What would make your free time better?", 
            "Did you spend it alone or with others?", 
            "Was there something special you did during your free time?"
        ]
    }
    
    conversation_text = ""
    last_question = random.choice(initial_questions) 
    
    user_input = input(f"{last_question}: ")
    conversation_text += " " + user_input
    
    for _ in range(1):  
        follow_up = random.choice(follow_up_questions[last_question])
        user_input = input(f"{follow_up}: ")
        conversation_text += " " + user_input
        last_question = follow_up 
    
    emotional_score = calculate_emotional_score(conversation_text)
    predicted_screen_time = predict_screen_time(age, study_hours, emotional_score)
    print(f"Based on the provided information, your recommended screen time is: {predicted_screen_time:.2f} hours.")
    
chatbot()
