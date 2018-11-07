from flask import Flask, render_template, json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config.from_pyfile('database.cfg')
app.config.from_pyfile('/etc/dbhost.cfg')

mysql.init_app(app)

@app.route('/')
def main():
    version = showVersion()
    return render_template('index.html', version=version)

def showVersion():
    try:
        myfile = '/tmp/app-version.txt'
        with open(myfile) as f:
            message = '{0}'.format(f.read())
    except IOError:
        message = '\n\nFile not found: ' + myfile
    return message


@app.route('/showEntries')
def showEntries():
    version = showVersion()
    try:
        # connect to mysql
        connection = mysql.connect()
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM students''')
        result = cursor.fetchall()
	    
        students = []
        for entry in result:
            record = {
                    'id': entry[0],
                    'name': entry[1],
            }
            students.append(record)		

        return render_template('db.html', version=version, students=students)
    except Exception as e:
        return json.dumps({'error':str(e)})

    except Exception as e:
        return json.dumps({'error':str(e)})
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
