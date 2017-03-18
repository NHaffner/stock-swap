from flask import Response, Flask, render_template, request, \
    redirect, url_for, send_from_directory, send_file, jsonify, session
from werkzeug import generate_password_hash, check_password_hash, secure_filename
import sqlite3
from dateutil import parser

sqlite_file = 'LocalDB/LocalDB.db'

app = Flask(__name__)


@app.route('/main_analytics/drive')
def drive():
    user_id = 1

    return render_template('drive.html')


@app.route('/main_analytics')
def main_analytics():
    user_id = 1

    return render_template('main_analytics.html')


@app.route('/drive_date', methods=['POST'])
def datedb():
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()
    user_id = request.form.get("patient")
    get_drive_score = "select rec_date,score from driveanalytics join driverecordings on driveanalytics.id = driverecordings.id where driverecordings.user_id = {} order by rec_date".format(
        user_id)
    cursor.execute(get_drive_score)
    drive_score = cursor.fetchall()
    cursor.close()
    return jsonify(drive_score)


@app.route('/drive_date/hover', methods=['POST'])
def hoverdb():
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()
    user_id = request.form.get("patient")
    rec_date = request.form.get("date")

    get_distance = "select distance,emergency_stops,u_turns  from driveanalytics join driverecordings on driveanalytics.id = driverecordings.id where driverecordings.user_id = 20 driveanalytics.score=9 limit 1".format(
        result1)
    cursor.execute(get_distance)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    return jsonify(result)


@app.route('/drive_hour', methods=['POST'])
def hourdb():
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()
    user_id = request.form.get("patient")
    get_drive_score = "select rec_date,score from driveanalytics join driverecordings on driveanalytics.id = driverecordings.id where driverecordings.user_id = {} order by rec_date".format(
        user_id)
    cursor.execute(get_drive_score)
    drive_score = cursor.fetchall()
    cursor.close()
    return jsonify(drive_score)


@app.route('/drive_hour/hover', methods=['POST'])
def timedb():
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()
    user_id = request.form.get("patient")
    rec_date = request.form.get("date")
    print(rec_date)
    get_distance = "select distance,emergency_stops,u_turns  from driveanalytics join driverecordings on driveanalytics.id = driverecordings.id where driverecordings.user_id = 20 limit 1"
    cursor.execute(get_distance)
    result = cursor.fetchall()
    cursor.close()
    return jsonify(result)


@app.route('/drive_map', methods=['POST'])
def mapdb():
    connection = sqlite3.connect(sqlite_file)
    cursor = connection.cursor()
    user_id = 20
    get_drive_score = "select rec_date,score from driveanalytics join driverecordings on driveanalytics.id = driverecordings.id where driverecordings.user_id = {} order by rec_date".format(
        user_id)
    cursor.execute(get_drive_score)
    drive_score = cursor.fetchall()
    cursor.close()
    return jsonify(drive_score)


@app.route('/query/drive/time-of-day', methods=['POST'])
def queryTimeOfDayDrive():
    conn = sqlite3.connect(sqlite_file)
    c = conn.cursor()
    user_id = request.form.get("patient_id")
    sql = "select rec_date,score from driveanalytics join driverecordings on driveanalytics.id = driverecordings.id where driverecordings.user_id = {} order by rec_date".format(
        user_id)
    c.execute(sql)
    result = c.fetchall()
    c.close()
    parsedresult = []
    timeofdayArr = [[], [], []]
    avgPerTimeOfDay = []
    # dates = [each[0] for each in result]
    for each in result:
        date = parser.parse(each[0])
        if date.hour <= 12 and date.hour >= 6:  ##morning
            timeofdayArr[0].append(each[1])

        elif date.hour <= 18:  ##after-noon
            timeofdayArr[1].append(each[1])

        else:  ##night
            timeofdayArr[2].append(each[1])
    print(timeofdayArr);
    for timeofday in timeofdayArr:
        if len(timeofday) is not 0:
            avg = sum(timeofday) / float(len(timeofday))
            avgPerTimeOfDay.append(avg)
        else:
            avgPerTimeOfDay.append(0)
    return jsonify(avgPerTimeOfDay)

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(debug=True)

# @app.route('/route', methods = ['POST'])
# def routedb():
# 	connection = sqlite3.connect(sqlite_file)
# 	cursor = connection.cursor ()
# 	user_id = 20
# 	sql = "select * from driveanalytics join driverecordings on driveanalytics.id = driverecordings.id where driverecordings.user_id = {}".format(user_id)
# 	cursor.execute(sql)
# 	result = cursor.fetchall()
# 	cursor.close()
# 	return jsonify(result)









