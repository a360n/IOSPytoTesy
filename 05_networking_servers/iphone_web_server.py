#!/usr/bin/env python3
"""
🌐 تشغيل خادم ويب تفاعلي على الآيفون (iPhone Web Server & Remote Control)
يقوم هذا السكربت بتحويل جهاز الآيفون إلى سيرفر ويب مصغر (HTTP Server) متصل بشبكة الـ Wi-Fi المحلية!
يمكنك فتح المتصفح من جهاز الماك أو الكمبيوتر على نفس الشبكة والدخول لصفحة تحكم الآيفون.
"""

import http.server
import socketserver
import socket
import json
import platform
import os
import sys

def get_local_ip():
    """الحصول على عنوان IP المحلي للآيفون على شبكة الواي فاي"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # لا يتم إرسال بيانات فعلية
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

HTML_PAGE = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iPhone Pyto Control Center</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background: #0b0f19; color: #f3f4f6; min-height: 100vh; padding: 20px; display: flex; justify-content: center; }
        .container { width: 100%; max-width: 700px; }
        .header { text-align: center; margin-bottom: 25px; padding: 20px; background: rgba(255,255,255,0.05); border-radius: 16px; backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }
        .header h1 { font-size: 24px; color: #38bdf8; margin-bottom: 8px; }
        .badge { display: inline-block; padding: 4px 12px; background: #0284c7; color: white; border-radius: 20px; font-size: 13px; font-weight: bold; }
        .card { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 20px; margin-bottom: 20px; }
        .card h2 { font-size: 18px; color: #f472b6; margin-bottom: 15px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 8px; }
        .stat-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; }
        .stat-item { background: rgba(0,0,0,0.3); padding: 12px; border-radius: 10px; }
        .stat-label { font-size: 12px; color: #9ca3af; }
        .stat-value { font-size: 16px; font-weight: bold; color: #34d399; margin-top: 4px; }
        .terminal { background: #000; border-radius: 10px; padding: 15px; font-family: monospace; font-size: 14px; color: #10b981; border: 1px solid #1f2937; height: 120px; overflow-y: auto; margin-top: 10px; }
        .btn { background: #3b82f6; color: white; border: none; padding: 10px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; margin-top: 10px; }
        .btn:hover { background: #2563eb; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <span class="badge">📡 خادم بايثون نشط على الآيفون</span>
            <h1>لوحة تحكم iPhone 17 Pro Max</h1>
            <p style="color: #94a3b8; font-size: 14px;">تم تشغيل هذا الموقع مباشرة من جهاز الآيفون الخاص بك عبر Pyto!</p>
        </div>

        <div class="card">
            <h2>📱 معلومات الجهاز والبيئة</h2>
            <div class="stat-grid">
                <div class="stat-item"><div class="stat-label">النظام</div><div class="stat-value">__SYSTEM__</div></div>
                <div class="stat-item"><div class="stat-label">أنوية المعالج</div><div class="stat-value">__CORES__ Cores</div></div>
                <div class="stat-item"><div class="stat-label">إصدار بايثون</div><div class="stat-value">__PY_VER__</div></div>
                <div class="stat-item"><div class="stat-label">المعمارية</div><div class="stat-value">__ARCH__</div></div>
            </div>
        </div>

        <div class="card">
            <h2>⚡ حالة الاتصال المباشر</h2>
            <div class="stat-grid">
                <div class="stat-item"><div class="stat-label">عنوان الآي بي المحلي</div><div class="stat-value">__IP__</div></div>
                <div class="stat-item"><div class="stat-label">المنفذ (Port)</div><div class="stat-value">8080</div></div>
            </div>
            <button class="btn" onclick="alert('اتصالك بالآيفون يعمل بسرعة البرق!')">🔔 إرسال اختبار استجابة Ping</button>
        </div>
    </div>
</body>
</html>"""

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.end_headers()
            
            content = HTML_PAGE
            content = content.replace("__SYSTEM__", f"{platform.system()} {platform.release()}")
            content = content.replace("__CORES__", str(os.cpu_count() or 4))
            content = content.replace("__PY_VER__", sys.version.split()[0])
            content = content.replace("__ARCH__", platform.machine())
            content = content.replace("__IP__", get_local_ip())
            
            self.wfile.write(content.encode("utf-8"))
        elif self.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status_data = {
                "status": "online",
                "device": "iPhone",
                "cores": os.cpu_count(),
                "python": sys.version
            }
            self.wfile.write(json.dumps(status_data).encode("utf-8"))
        else:
            super().do_GET()

def start_server(port=8080):
    ip = get_local_ip()
    print("=" * 60)
    print(f"  🌐 خادم ويب محلي يعمل على الآيفون (iPhone Web Server)")
    print("=" * 60)
    print(f"🚀 السيرفر يعمل الآن على المنفذ {port}")
    print(f"\n📲 للدخول من نفس جهاز الآيفون:")
    print(f"   👉 http://localhost:{port}")
    print(f"\n💻 للدخول من جهاز الماك أو الكمبيوتر أو أي هاتف على نفس الواي فاي:")
    print(f"   👉 http://{ip}:{port}")
    print(f"\n📡 للاستعلام عبر الـ API:")
    print(f"   👉 http://{ip}:{port}/api/status")
    print("-" * 60)
    print("⏳ اضغط (Stop / Ctrl+C) لإيقاف السيرفر.\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n⏹️ تم إيقاف السيرفر بنجاح.")

if __name__ == "__main__":
    start_server()
