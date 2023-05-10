from pprint import pprint
page = {'questions': [{'answer': 'india',
                'context': 'India is a great country where people speak '
                           'different languages but the national language is '
                           'Hindi. India is full of different castes, creeds, '
                           'religion, and cultures but they live together. '
                           'That’s the reasons India is famous for the common '
                           'saying of “unity in diversity“.',
                'extra_options': ['Pakistan',
                                  'South Korea',
                                  'Nepal',
                                  'Philippines',
                                  'Zimbabwe'],
                'id': 1,
                'options': ['Bangladesh', 'Indonesia', 'China'],
                'options_algorithm': 'sense2vec',
                'question_statement': 'What is the country where people speak '
                                      'different languages but the national '
                                      'language is Hindi?',
                'question_type': 'MCQ'},
               {'answer': 'castes',
                'context': 'India is full of different castes, creeds, '
                           'religion, and cultures but they live together.',
                'extra_options': ['Ethnic Groups',
                                  'Cultural Practices',
                                  'Class Distinctions'],
                'id': 2,
                'options': ['Caste System', 'Brahmins', 'Societies'],
                'options_algorithm': 'sense2vec',
                'question_statement': 'What is the most common religion in '
                                      'India?',
                'question_type': 'MCQ'},
               {'answer': 'diversity',
                'context': 'That’s the reasons India is famous for the common '
                           'saying of “unity in diversity“.',
                'extra_options': [],
                'id': 3,
                'options': ['Inclusivity', 'Homogeneity', 'Overall Culture'],
                'options_algorithm': 'sense2vec',
                'question_statement': 'What is the common saying in India?',
                'question_type': 'MCQ'},
               {'answer': 'religion',
                'context': 'India is full of different castes, creeds, '
                           'religion, and cultures but they live together.',
                'extra_options': ['Religious Ideology'],
                'id': 4,
                'options': ['Islam', 'Belief System', 'Christianity'],
                'options_algorithm': 'sense2vec',
                'question_statement': 'What is the most common religion in '
                                      'India?',
                'question_type': 'MCQ'}],
 'statement': 'India is a great country where people speak different languages '
              'but the national language is Hindi. India is full of different '
              'castes, creeds, religion, and cultures but they live together. '
              'That’s the reasons India is famous for the common saying of '
              '“unity in diversity“. India is the seventh-largestcountry in '
              'the whole world.',
 'time_taken': 23.88989758491516
        }
def generate_test(page):
    individual_question = page["questions"]
    questions = []
    answer = []
    for i in range(len(individual_question)):
        questions.append(individual_question[i]["question_statement"] + " Options=" + str(individual_question[i]["options"]))
        answer.append(individual_question[i]["answer"])
    #pprint(questions)
    #pprint(answer)
    return questions, answer

def generate_test_faq(page):
    individual_question = page["questions"]
    questions = []
    answer = []
    for i in range(len(individual_question)):
        questions.append(individual_question[i]["Question"] + " Context=" + str(individual_question[i]["context"]))
        answer.append(individual_question[i]["Answer"])
    #pprint(questions)
    #pprint(answer)
    return questions, answer

generate_test(page)