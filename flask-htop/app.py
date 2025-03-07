from flask import Flask
import os
import subprocess
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():

    name = "Vishal Prakash"


    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"


    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S.%f")


    if os.uname().sysname == "Darwin":  
        top_output = subprocess.getoutput("top -l 1")
    else:  # Linux
        top_output = subprocess.getoutput("top -b -n 1")


    response = f"""
    <pre>
    Name: {name}
    User: {username}
    Server Time (IST): {formatted_time}
    
    TOP output:
    {top_output}
    </pre>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
