from flask import Flask, render_template
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
    return render_template('k.html', sinhvien=data)

if __name__ == '__main__':
    app.run(debug=True)