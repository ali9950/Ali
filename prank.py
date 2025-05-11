# اسم الملف: prank.py
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler

# كود HTML للمقلب
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>⚠️ تحذير: تم اختراق الجهاز! ⚠️</title>
    <style>
        body {
            background-color: black;
            color: red;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 50px;
        }
        #countdown {
            font-size: 30px;
            margin: 20px;
        }
        #meme {
            display: none;
            margin: 20px auto;
            max-width: 300px;
        }
    </style>
</head>
<body>
    <h1>⚠️ تم اختراق جهازك! ⚠️</h1>
    <p>جاري سرقة جميع بياناتك...</p>
    <div id="countdown"></div>
    <img id="meme" src="https://media.giphy.com/media/LlYzz6zWXODfK/giphy.gif">
    <audio id="scarySound" src="https://www.soundjay.com/misc/sounds/magic-chime-01.mp3" preload="auto"></audio>

    <script>
        // تأثير العد التنازلي المخيف
        let count = 5;
        const countdownEl = document.getElementById("countdown");
        const interval = setInterval(() => {
            countdownEl.textContent = `التدمير الذاتي خلال: ${count} ثانية...`;
            count--;
            if (count < 0) {
                clearInterval(interval);
                document.getElementById("scarySound").play();
                document.getElementById("countdown").style.display = "none";
                document.querySelector("h1").textContent = "هاها! مزحة! 😈";
                document.querySelector("p").textContent = "كنت أختبرك! لا تقلق 😂";
                document.getElementById("meme").style.display = "block";
            }
        }, 1000);
    </script>
</body>
</html>
"""

# حفظ HTML في ملف
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("✅ تم إنشاء صفحة المقلب بنجاح!")
print("🚀 جاري تشغيل الخادم المحلي...")

# تشغيل خادم ويب لعرض الصفحة
os.system("python -m http.server 8080 &")
print("🌐 يمكنك الآن إرسال الرابط التالي لصديقك:")
print("http://<YOUR_IP>:8080")

