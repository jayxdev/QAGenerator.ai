from flask import Flask, request, render_template, flash, redirect, url_for
from AI import main, generateTest
from AI.subjective import SubjectiveTest

app = Flask(__name__, static_folder="web/static", template_folder="web/templates")

app.secret_key = 'aica2'


# import nltk
# nltk.download("all")
# exit()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test_generate', methods=["POST"])
def test_generate():
    if request.method == "POST":
        inputText = request.form["itext"]
        testType = request.form["test_type"]
        noOfQues = request.form["noq"]
        payload = {
            "input_text": inputText,
            "max_questions": noOfQues
        }
        if testType == "objective":
            qg = main.QGen()
            objective_generator = qg.predict_mcq(payload)
            question_list, answer_list = generateTest.generate_test(objective_generator)
            testgenerate = zip(question_list, answer_list)
            return render_template('generatedtestdata.html', cresults=testgenerate)
        elif testType == "subjective":
            subjective_generator = SubjectiveTest(inputText, noOfQues)
            question_list, answer_list = subjective_generator.generate_test()
            testgenerate = zip(question_list, answer_list)
            return render_template('generatedtestdata.html', cresults=testgenerate)
        elif testType == "Yes-No":
            qe = main.BoolQGen()
            yesNo_generator = qe.predict_boolq(payload)
            question_list, answer_list = generateTest.generate_test(yesNo_generator)
            testgenerate = zip(question_list, answer_list)
            return render_template('generatedtestdata.html', cresults=testgenerate)
        elif testType == "Faq":
            qg = main.QGen()
            Fag_generator = qg.predict_shortq(payload)
            question_list, answer_list = generateTest.generate_test_faq(Fag_generator)
            testgenerate = zip(question_list, answer_list)
            return render_template('generatedtestdata.html', cresults=testgenerate)
        elif testType == "Predict Answer":
            qg = main.AnswerPredictor()
            answer = qg.predict_answer(payload)
            testgenerate = zip(noOfQues, answer)
            return render_template('generatedtestdata.html', cresults=testgenerate)
        else:
            flash('Error Ocuured!')
            return redirect(url_for('/'))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
