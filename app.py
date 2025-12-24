from flask import Flask,request,jsonify, render_template
from datetime import date
from flask_cors import CORS
import calendar
app = Flask(__name__)
CORS(app)


@app.route('/',methods=['POST'])
def index():
    data = request.get_json()
    year = int(data["year"])
    month = int(data["month"])
    cal = calendar.monthcalendar(year, month)
    obj={
        "year": year,
        "month": month,
        "weeks": cal
    }
    if data.get('day') and int(data['day']):
        day=int(data['day'])
        obj['day']=date(year,month,day).strftime('%A')
        obj['monthName']=date(year,month,day).strftime('%B')
    return jsonify(obj)

 