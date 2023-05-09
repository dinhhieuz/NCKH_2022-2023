from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '11092001Phanhuynam'
app.config['MYSQL_DB'] = 'quanlibaithi'

mysql = MySQL(app)

cursor = mysql.connection.cursor()
cursor.execute("SELECT * FROM sinhvien")
data = cursor.fetchall()
print(data)

if __name__ == '__main__':
    app.run(debug=True)

# Tạo trang HTML để hiển thị dữ liệu
# @app.route('/')
# def index():
#     return render_template('index3.html', sinhvien=data)

# @app.route('/insert', methods = ['POST'])
# def insert():
#     # print("insert-data")
#     # data = request.form
#     # print(data.get("MASINHVIEN"))
#     # print(data)
#     # return "done"
#     if request.method == "POST":
#         flash("Data Inserted Successfully")
#         MASINHVIEN = request.form['MASINHVIEN']
#         TENSINHVIEN = request.form['TENSINHVIEN']
#         NGAYSINH = request.form['NGAYSINH']
#         SDT = request.form['SDT']
#         LOP = request.form['LOP']
#         KHOA = request.form['KHOA']
#         cur = mysql.connection.cursor()
#         cur.execute("INSERT INTO sinhvien (masinhvien, tensinhvien, ngaysinh, sdt, lop, khoa) VALUES (%s, %s, %s, %s, %s, %s)", (MASINHVIEN, TENSINHVIEN, NGAYSINH, SDT, LOP, KHOA))
#         cur.connection.commit()
#         return redirect(url_for('index'))

# if __name__ == '__main__':
#     app.run(debug=True)



