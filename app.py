from flask import Flask, render_template

app = Flask(__name__)

@app.route('/fizzbuzz')
def fizzbuzz():
    fizzbuzz_list = []  # Create an empty list to store FizzBuzz results
    for number in range(1, 101):  # Loop through numbers from 1 to 100
            if number % 3 == 0 and number % 5 == 0:
                fizzbuzz_list.append('FizzBuzz')
            elif number % 3 == 0:
                fizzbuzz_list.append('Fizz')
            elif number % 5 == 0:
                fizzbuzz_list.append('Buzz')
            else:
                fizzbuzz_list.append(str(number))  # Convert the number to a string and add it to the list
    return render_template('fizzbuzz.html', fizzbuzz_list=fizzbuzz_list)

if __name__ == '__main__':
    app.run()
