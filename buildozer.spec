[app]

# (اسم التطبيق وحزمته)
title = Hisab Al Himayat
package.name = hisabalhimayat
package.domain = org.odey

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0

# المكتبات المطلوبة لتشغيل النصوص العربية وتطبيق كيفي
requirements = python3,kivy,arabic_reshaper,python-bidi

# مسارات الأيقونات وشاشة البدء
icon.filename = %(source.dir)s/icon.png
presplash.filename = %(source.dir)s/presplash.png

orientation = portrait
fullscreen = 0

# إعدادات الأندرويد
android.api = 33
android.minapi = 21

# الموافقة التلقائية على ترخيص Android SDK (لمنع توقف البناء)
android.accept_sdk_license = True

log_level = 2

[buildozer]
warn_on_root = 1
