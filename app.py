from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dalgonaceriadalgondalgandul@2020005010'

@app.route('/home', methods = ['POST', 'GET'])
def login():
    return render_template('index.html')

@app.route('/pelanggan', methods = ['POST', 'GET'])
def pelanggan():
    return render_template('data-pelanggan.html')

@app.route('/pemasok', methods = ['POST', 'GET'])
def pemasok():
    return render_template('data-pemasok.html')

@app.route('/barang', methods = ['POST', 'GET'])
def master_barang():
    return render_template('master-barang.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9500, debug=True)