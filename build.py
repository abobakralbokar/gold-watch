#!/usr/bin/env python3
"""يبني index.html (نسخة الموقع المستقل) من page.html (نسخة الأرتيفاكت) بإضافة هيكل الصفحة الكامل."""
import pathlib
root = pathlib.Path(__file__).parent
page = (root / "page.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0E1013">
<meta name="description" content="أسعار جرام الذهب لحظيًا بالريال السعودي وفي صنعاء وعدن، مع التوقعات والمستويات والتنبيهات.">
<style>:root{color-scheme:light dark;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
"""
tail = "\n</body>\n</html>\n"
(root / "index.html").write_text(head + page + tail, encoding="utf-8")
print("index.html built:", len(page), "chars")
