from flask import Flask, request, render_template_string
import requests
import socket
import os

app = Flask(__name__)

@app.route('/')
def index():
    ip = request.remote_addr
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except:
        hostname = "Không xác định"
    
    # Lấy thông tin từ IP
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = r.json()
    except:
        data = {"status": "fail"}
    
    # Ghi log IP
    with open("ip_logs.txt", "a", encoding="utf-8") as f:
        f.write(f"IP: {ip} | Thời gian: {request.headers.get('Date')} | User-Agent: {request.user_agent} | Thông tin: {data}\n")
    
    return f"""
    <h1>✅ IP Logger hoạt động!</h1>
    <p>IP của bạn: <strong>{ip}</strong></p>
    <p>Hostname: {hostname}</p>
    <p>Thành phố: {data.get('city', 'N/A')}</p>
    <p>Quốc gia: {data.get('country', 'N/A')}</p>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
    
