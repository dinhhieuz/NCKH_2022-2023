from flask import Flask, render_template, request, flash, url_for, redirect
from werkzeug.utils import redirect
import pymysql

app = Flask(__name__)
app.secret_key = 'many random bytes'
# Kết nối tới cơ sở dữ liệu
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='11092001Phanhuynam',
                             db='quanlibaithi')

# Tạo trang HTML để hiển thị dữ liệu
@app.route('/')
def index():
    mysql = connection.cursor()
    mysql.execute("SELECT * FROM sinhvien")
    data = mysql.fetchall()
    return render_template('index3.html', sinhvien=data)


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        MASINHVIEN = request.form['MASINHVIEN']
        TENSINHVIEN = request.form['TENSINHVIEN']
        NGAYSINH = request.form['NGAYSINH']
        SDT = request.form['SDT']
        LOP = request.form['LOP']
        KHOA = request.form['KHOA']
        cur = connection.cursor()
        cur.execute("INSERT INTO sinhvien (masinhvien, tensinhvien, ngaysinh, sdt, lop, khoa) VALUES (%s, %s, %s, %s, %s, %s)", (MASINHVIEN, TENSINHVIEN, NGAYSINH, SDT, LOP, KHOA))
        cur.connection.commit()
        return redirect(url_for('index'))

@app.route('/delete/<string:MASINHVIEN>', methods = ['GET'])
def delete(MASINHVIEN):
    flash("Record Has Been Deleted Successfully")
    cur = connection.cursor()
    cur.execute("DELETE FROM sinhvien WHERE MASINHVIEN=%s", (MASINHVIEN,))
    connection.commit()
    return redirect(url_for('index'))

@app.route('/update', methods= ['POST', 'GET'])
def update():
    if request.method == 'POST':
        MASINHVIEN = request.form['MASINHVIEN']
        TENSINHVIEN = request.form['TENSINHVIEN']
        NGAYSINH = request.form['NGAYSINH']
        SDT = request.form['SDT']
        LOP = request.form['LOP']
        KHOA = request.form['KHOA']

# request.form này sẽ lấy từ name bên file html
        cur = connection.cursor()
        cur.execute("""
        UPDATE sinhvien SET TENSINHVIEN=%s, NGAYSINH=%s, SDT=%s, LOP=%s, KHOA=%s
        WHERE MASINHVIEN=%s
        """, (TENSINHVIEN, NGAYSINH, SDT, LOP, KHOA, MASINHVIEN))
        connection.commit()
        flash("Data Updated Successfully")
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)