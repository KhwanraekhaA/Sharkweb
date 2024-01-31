from flask import *
from predict import SHARK_DETECTION
from datetime import datetime

app = Flask(__name__)
# ใส่ path ของ model ของเรา
pred = SHARK_DETECTION(r'D:\Senoir Proj\yolo webapp\best.pt')

@app.route('/public/<path:path>')
def send_report(path):
    return send_from_directory('public', path)

@app.route("/")
def root():
    """
    Site main page handler function.
    :return: Content of index.html file
    """
    with open("index.html") as file:
        return file.read()
    
    
@app.route('/success', methods=['POST', 'GET'])
def successPOST():
    if request.method == 'POST':
        # โค้ดที่ใช้ในกรณี POST request
        f = request.files['file']
        date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")[:-3]
        filename = f"D:/Senoir Proj/yolo webapp/public/{date}.jpg"
        output = f"D:/Senoir Proj/yolo webapp/public/{date}_output.jpg"

        f.save(filename)
        pred(filename, output)


        # ส่งรูปภาพที่ถูก upload โดยตรงเป็น response
        return send_from_directory('public', f"{date}_output.jpg")
    else:
        # โค้ดที่ใช้ในกรณี GET request
        return render_template('success.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
