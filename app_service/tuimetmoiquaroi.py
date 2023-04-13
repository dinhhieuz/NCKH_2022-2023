from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.utils import redirect
import pymysql

app = Flask(__name__)

# Kết nối tới cơ sở dữ liệu
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='11092001Phanhuynam',
                             db='quanlibaithi')

# Truy vấn dữ liệu từ bảng users
mysql = connection.cursor()
mysql.execute("SELECT * FROM sinhvien")
data = mysql.fetchall()

# Tạo trang HTML để hiển thị dữ liệu
@app.route('/')
def index():
    return render_template('index3.html', sinhvien=data)


@app.route('/insert', methods = ['POST'])
def insert():
    # print("insert-data")
    # data = request.form
    # print(data.get("MASINHVIEN"))
    # print(data)
    # return "done"
    if request.method == "POST":
        flash("Data Inserted Successfully")
        MASINHVIEN = request.form['MASINHVIEN']
        TENSINHVIEN = request.form['TENSINHVIEN']
        NGAYSINH = request.form['NGAYSINH']
        SDT = request.form['SDT']
        LOP = request.form['LOP']
        KHOA = request.form['KHOA']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sinhvien (masinhvien, tensinhvien, ngaysinh, sdt, lop, khoa) VALUES (%s, %s, %s, %s, %s, %s)", (MASINHVIEN, TENSINHVIEN, NGAYSINH, SDT, LOP, KHOA))
        cur.connection.commit()
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)