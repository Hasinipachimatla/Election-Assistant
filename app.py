from flask import Flask, render_template, request

app = Flask(__name__)   # ✅ app must be defined FIRST

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/steps')
def steps():
    return render_template('steps.html')

@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    response = ""

@app.route('/timeline')
def timeline():
    return render_template('timeline.html')
    
    if request.method == 'POST':
        user_input = request.form['user_input'].lower()

        if "vote" in user_input:
            response = "To vote, you must be 18+ and registered as a voter."
        elif "register" in user_input:
            response = "You can register online through the official election website."
        elif "documents" in user_input:
            response = "You need ID proof like Aadhaar, PAN, or Voter ID."
        elif "eligibility" in user_input:
            response = "You must be an Indian citizen and at least 18 years old."
        else:
            response = "Sorry, I didn't understand. Please ask about voting, registration, or eligibility."

    return render_template('chatbot.html', response=response)

if __name__ == '__main__':
    import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
    

