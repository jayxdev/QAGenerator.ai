from pprint import pprint
from AI import main, generateTest

payloadtext = "A mango is an edible stone fruit produced by the tropical tree Mangifera indica. It is believed to have originated between Northeastern India, Bangladesh and Northwestern Myanmar.[1] M. indica has been cultivated in South and Southeast Asia since ancient times resulting in two types of modern mango cultivars: the Indian type and the Southeast Asian type.[2][3] Other species in the genus Mangifera also produce edible fruits that are also called mangoes, the majority of which are found in the Malesian ecoregion."

print("1-Yes-No")
print("2-Mcq")
print("3-Faq")
print("4-Predict answer")

i = input("choice")

if i == '1':
    qe = main.BoolQGen()
    payload = {
        "input_text": payloadtext,
        "max_questions": 6
    }

    output = qe.predict_boolq(payload)
    pprint(output)
elif i == '2':
    qg = main.QGen()
    payload = {
        "input_text": payloadtext
    }
    output = qg.predict_mcq(payload)
    #pprint(output)
    pprint(generateTest.generate_test(output))
elif i == '3':
    qg = main.QGen()
    payload = {
        "input_text": payloadtext
    }
    output = qg.predict_shortq(payload)
    pprint(output)
elif i == '4':
    qg = main.AnswerPredictor()
    payload = {
        "input_text": payloadtext,
        "input_question": "what is mango?"
    }
    output = qg.predict_answer(payload)
    pprint(output)
