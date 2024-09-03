from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    brands = ['BMW', 'KAWASAKI', 'HONDA', 'HERO', 'Royal Enfield', 'JAWA', 'Ducati', 'Triumph']
    return render_template('index.html', brands=brands)

@app.route('/calculate', methods=['POST'])
def calculate():
    brand = request.form['brand']
    model = request.form['model']
    question = request.form['question']

    answer = f"Here's the answer for your {brand} {model}:\n\n"
    answer += "This is a placeholder answer. In a real application, "
    answer += "you would process the question and generate a response based on the manual."

    return render_template('result.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
