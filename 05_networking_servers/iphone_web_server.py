#!/usr/bin/env python3
"""
🌐 iPhone Hosted Web Server & Remote Control Dashboard
Turns your iPhone into a local HTTP web server accessible from any Mac, PC, or phone on the same Wi-Fi network!
"""

import http.server
import socketserver
import socket
import json
import platform
import os
import sys

def get_local_ip():
    """Retrieves local Wi-Fi IP address of the iPhone"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

HTML_PAGE = """<!DOCTYPE html>
<html lang="en">
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
        .btn { background: #3b82f6; color: white; border: none; padding: 12px 20px; border-radius: 8px; cursor: pointer; font-weight: bold; width: 100%; margin-top: 10px; }
        .btn:hover { background: #2563eb; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <span class="badge">📡 Live Python Server on iPhone</span>
            <h1>iPhone 17 Pro Max Control Center</h1>
            <p style="color: #94a3b8; font-size: 14px;">This website is hosted and served directly from your iPhone via Pyto!</p>
        </div>

        <div class="card">
            <h2>📱 Device & Environment Telemetry</h2>
            <div class="stat-grid">
                <div class="stat-item"><div class="stat-label">Operating System</div><div class="stat-value">__SYSTEM__</div></div>
                <div class="stat-item"><div class="stat-label">CPU Cores</div><div class="stat-value">__CORES__ Cores</div></div>
                <div class="stat-item"><div class="stat-label">Python Version</div><div class="stat-value">__PY_VER__</div></div>
                <div class="stat-item"><div class="stat-label">Architecture</div><div class="stat-value">__ARCH__</div></div>
            </div>
        </div>

        <div class="card">
            <h2>⚡ Connection Status</h2>
            <div class="stat-grid">
                <div class="stat-item"><div class="stat-label">Local IP Address</div><div class="stat-value">__IP__</div></div>
                <div class="stat-item"><div class="stat-label">Port</div><div class="stat-value">8080</div></div>
            </div>
            <button class="btn" onclick="alert('Connection to your iPhone is active and lightning fast!')">🔔 Send Ping Request</button>
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
    print(f"  🌐 iPhone Embedded Web Server")
    print("=" * 60)
    print(f"🚀 Server is now listening on port {port}")
    print(f"\n📲 From this iPhone:")
    print(f"   👉 http://localhost:{port}")
    print(f"\n💻 From Mac, PC, or another device on the same Wi-Fi:")
    print(f"   👉 http://{ip}:{port}")
    print(f"\n📡 JSON API Status Endpoint:")
    print(f"   👉 http://{ip}:{port}/api/status")
    print("-" * 60)
    print("⏳ Press stop or Ctrl+C to terminate server.\n")

    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), CustomHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n⏹️ Server stopped successfully.")

if __name__ == "__main__":
    start_server()
