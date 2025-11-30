[app]

title = Multi Downloader ID
package.name = multidownloaderid
package.domain = org.multidownloader

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,mp3,ttf,txt,md,xml,json

version = 1.0.0

# --- FIXED requirements ---
# python3 tidak perlu ditulis
# pillow harus versi stabil
# yt-dlp harus ditambah manual via requirements + source.include_exts
requirements = kivy==2.2.1, pillow==9.5.0, requests, yt-dlp

# agar yt-dlp bisa dibundle buildozer
android.whitelist = yt_dlp/*.py

orientation = portrait
fullscreen = 0

# --- Android permissions modern ---
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# --- Android Target ---
android.api = 33
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a

android.enable_androidx = True
android.allow_backup = True

# aktifkan SDL2 bootstrap wajib untuk Kivy
android.bootstrap = sdl2

# adaptive icon
android.adaptive_icon_foreground = icon.png
android.adaptive_icon_background = #000000
icon.filename = icon.png

log_level = 2


[buildozer]
log_level = 2
warn_on_root = 1