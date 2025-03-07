from flask import Flask
import os
import subprocess
import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Your full name
    name = "Vishal Prakash"

    # Get the system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "codespace"

    # Get current IST time
    ist_time = datetime.datetime.utcnow() + datetime.timedelta(hours=5, minutes=30)
    formatted_time = ist_time.strftime("%Y-%m-%d %H:%M:%S.%f")

    # Use the correct `top` command for Linux
    top_output = subprocess.getoutput("top -b -n 1")

    # Format the response as HTML
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
