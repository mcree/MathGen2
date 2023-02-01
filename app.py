import random

from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = b'_5#y1A"FdQ2z\n\xec]/'


@app.route('/osztas', methods=['GET', 'POST'])
def osztas():
    app.logger.warning(request.form)

    def gen(b_min, b_max, c_min, c_max):
        b = random.randrange(b_min, b_max + 1)
        c = random.randrange(c_min, c_max + 1)
        a = b * c
        return {'A': a, 'B': b, 'C': c}

    e = []
    for i in range(1, request.form.get('count', type=int)):
        e.append(gen(request.form.get('b_min', type=int),
                     request.form.get('b_max', type=int),
                     request.form.get('c_min', type=int),
                     request.form.get('c_max', type=int)))

    return render_template('osztas.html', e=e)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
