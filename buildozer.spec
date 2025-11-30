[app]

title = Multi Downloader ID
package.name = multidownloaderid
package.domain = org.multidownloader

source.dir = .
source.include_exts = py,kv,png,jpg,jpeg,mp3,ttf,txt,md,xml,json

version = 1.0.0

# -----------------------------------------
# Requirements
# -----------------------------------------
# python3 tidak perlu ditulis
requirements = \
    kivy==2.2.1, \
    pillow==9.5.0, \
    requests, \
    yt-dlp

# Agar yt-dlp ikut dibundle
android.whitelist = yt_dlp/*.py

orientation = portrait
fullscreen = 0

# -----------------------------------------
# Android Permissions
# -----------------------------------------
android.permissions = \
    INTERNET, \
    READ_EXTERNAL_STORAGE, \
    WRITE_EXTERNAL_STORAGE, \
    MANAGE_EXTERNAL_STORAGE

# -----------------------------------------
# Android Target
# -----------------------------------------
android.api = 33
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a, armeabi-v7a

android.enable_androidx = True
android.allow_backup = True
android.bootstrap = sdl2

icon.filename = icon.png
android.adaptive_icon_foreground = icon.png
android.adaptive_icon_background = #000000

log_level = 2


[buildozer]
log_level = 2
warn_on_root = 1