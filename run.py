import math
from flask import Flask, render_template, request
from flask import jsonify
import paint

app = Flask(__name__)
app.config['SECRET_KEY'] = "dfdfdffdad"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mylist',methods=['GET', 'POST'])
def mylist():
    fs = request.files["genes"]
    myindex = int(request.form.get("index"))
    print(myindex)
    name = fs.filename
    fs.save(fs.filename)
    fs = open(fs.filename)
    count = len(fs.readlines()) - 1
    matrix = [[0 for i in range(3)] for i in range(count)]
    out_matrix = [[0 for i in range(4)] for i in range(count + 1)]
    fin = open(name)
    str1 = fin.readline()
    for i in range(count):
        str1 = fin.readline()
        matrix[i][0] = str1.split()[0]
        matrix[i][1] = str1.split()[1]
        matrix[i][2] = str1.split()[2]
    if(myindex==1):
        paint.paint(matrix)
    out_matrix[0][0] = "gene_id      "
    out_matrix[0][1] = "control_sample    "
    out_matrix[0][2] = "treat_sample  "
    out_matrix[0][3] = "log_2[FC]"
    for i in range(count):
        v1 = float(matrix[i][1])
        v2 = float(matrix[i][2])
        for j in range(3):
            out_matrix[i + 1][j] = matrix[i][j]
        if (v1 == 0 or v2 == 0):
            out_matrix[i + 1][3] = "null"
        else:
            out_matrix[i + 1][3] = math.log(v2 / v1, 2)
    print(matrix[0][0])
    print(out_matrix[0][1])
    if(count>100):
        return_matrix = [[0 for i in range(4)] for i in range(100)]
        for i in range(100):
            for j in range(4):
                return_matrix[i][j] = out_matrix[(myindex - 1) * 100 + i][j]
    else:
        return_matrix = [[0 for i in range(4)] for i in range(10)]
        for i in range(10):
            for j in range(4):
                return_matrix[i][j] = out_matrix[(myindex - 1) * 10 + i][j]

    return jsonify(return_matrix)


if __name__ == '__main__':
    app.run()