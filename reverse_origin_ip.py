from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def reverse_ip():
    # Get the origin IP address
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    
    # Reverse the IP
    reversed_ip = ".".join(client_ip.split(".")[::-1])
    
    return f"Your reversed IP is: {reversed_ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

