#!/bin/bash

# تثبيت cloudflared
echo "تثبيت cloudflared..."
wget https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm -O cloudflared
chmod +x cloudflared
mv cloudflared /data/data/com.termux/files/usr/bin

# إنشاء المجلد لملفات المقلب
mkdir -p prank && cd prank

# إنشاء صفحة HTML للمقلب
echo "إنشاء صفحة HTML..."
cat <<EOL > index.html
<!DOCTYPE html>
<html lang="ar">
<head>
  <meta charset="UTF-8">
  <title>تم اختراقك!</title>
  <style>
    body {
      background-color: black;
      color: red;
      text-align: center;
      font-family: monospace;
      margin-top: 100px;
    }
    h1 {
      font-size: 48px;
    }
  </style>
  <script>
    setTimeout(function() {
      window.location.href = "https://i.imgur.com/U3vTGjX.jpeg"; // صورة الميمز
    }, 5000);
  </script>
</head>
<body>
  <h1>هاتفك تم اختراقه!</h1>
  <p>يتم الآن نقل ملفاتك إلى السيرفر...</p>
</body>
</html>
EOL

# تشغيل سيرفر Python
echo "تشغيل السيرفر المحلي..."
tmux new-session -d -s prank_session "python3 -m http.server 8080"

# تشغيل Cloudflared
echo "تشغيل النفق عبر cloudflared..."
tmux new-session -d -s tunnel_session "cloudflared tunnel --url http://localhost:8080"

# تأخير بسيط لضمان تشغيل النفق أولاً
sleep 5

# طباعة رابط الوصول
echo "المقلب جاهز! رابط الوصول هو:"
curl -s http://localhost:4040/api/tunnels | jq -r .tunnels[0].public_url
