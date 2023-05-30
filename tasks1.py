import nltk

nltk.download('punkt')  


keywords = ['python', 'machine learning', 'data analysis', 'communication']

candidates = [
    {
        'name': 'John',
        'resume': "I have experience in Python and machine learning. I have worked on data analysis projects and possess excellent communication skills.",
    },
    {
        'name': 'Sarah',
        'resume': "My background includes Python programming and data analysis. I have strong communication skills and some knowledge of machine learning.",
    },
    {
        'name': 'Michael',
        'resume': "I am proficient in Python and have experience in machine learning. Additionally, I have excellent communication and data analysis skills.",
    }
]

scores = []
for candidate in candidates:
    resume = candidate['resume']
    tokens = nltk.word_tokenize(resume.lower())
    score = sum(keyword in tokens for keyword in keywords)
    scores.append(score)


best_candidate_index = scores.index(max(scores))
best_candidate = candidates[best_candidate_index]


print("Best Candidate: ", best_candidate['name'])
