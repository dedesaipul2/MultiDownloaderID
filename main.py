import os
import threading
import yt_dlp
import requests
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.popup import Popup
from kivy.uix.label import Label

# ------------------------------------------------------------
# Folder Penyimpanan (Download Folder Android)
# ------------------------------------------------------------

DOWNLOAD_DIR = "/storage/emulated/0/Download/"

if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# ------------------------------------------------------------
# Popup Notifikasi Sederhana
# ------------------------------------------------------------
def show_popup(message):
    popup = Popup(
        title="Multi Downloader ID",
        content=Label(text=message),
        size_hint=(0.7, 0.3)
    )
    popup.open()

# ------------------------------------------------------------
# Halaman Utama
# ------------------------------------------------------------
class HomePage(Screen):
    pass

# ------------------------------------------------------------
# Downloader Page
# ------------------------------------------------------------
class DownloaderPage(Screen):

    def start_download(self):
        url = self.ids.url_input.text.strip()

        if url == "":
            show_popup("Masukkan URL terlebih dahulu!")
            return

        # Deteksi platform otomatis
        if "youtube.com" in url or "youtu.be" in url:
            threading.Thread(target=self.youtube_download, args=(url,)).start()

        elif "tiktok.com" in url:
            threading.Thread(target=self.tiktok_download, args=(url,)).start()

        elif "instagram.com" in url:
            threading.Thread(target=self.instagram_download, args=(url,)).start()

        elif "facebook.com" in url:
            threading.Thread(target=self.facebook_download, args=(url,)).start()

        else:
            show_popup("Platform tidak dikenali!")
            return

    # --------------------------------------------------------
    # YouTube Downloader
    # --------------------------------------------------------
    def youtube_download(self, url):
        try:
            ydl_opts = {
                'outtmpl': DOWNLOAD_DIR + '%(title)s.%(ext)s',
                'format': 'best'
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            Clock.schedule_once(lambda dt: show_popup("Download YouTube selesai!"), 0)

        except Exception as e:
            Clock.schedule_once(lambda dt: show_popup(f"Error YouTube: {str(e)}"), 0)

    # --------------------------------------------------------
    # TikTok Downloader
    # --------------------------------------------------------
    def tiktok_download(self, url):
        try:
            api = "https://api.tikmate.app/api/lookup?url=" + url
            r = requests.get(api).json()

            dl_link = "https://tikmate.app/download/" + r["token"] + "/" + r["id"] + ".mp4"
            file_path = DOWNLOAD_DIR + "tiktok_video.mp4"

            open(file_path, "wb").write(requests.get(dl_link).content)

            Clock.schedule_once(lambda dt: show_popup("Download TikTok selesai!"), 0)

        except Exception as e:
            Clock.schedule_once(lambda dt: show_popup(f"Error TikTok: {str(e)}"), 0)

    # --------------------------------------------------------
    # Instagram Downloader
    # --------------------------------------------------------
    def instagram_download(self, url):
        try:
            api = "https://saveig.app/api/ajaxSearch"
            data = {"q": url, "vt": "Instagram"}

            res = requests.post(api, data=data).json()
            dl_link = res["data"]["medias"][0]["url"]

            fname = DOWNLOAD_DIR + "instagram_media.mp4"
            open(fname, "wb").write(requests.get(dl_link).content)

            Clock.schedule_once(lambda dt: show_popup("Download Instagram selesai!"), 0)

        except Exception as e:
            Clock.schedule_once(lambda dt: show_popup(f"Error Instagram: {str(e)}"), 0)

    # --------------------------------------------------------
    # Facebook Downloader
    # --------------------------------------------------------
    def facebook_download(self, url):
        try:
            api = "https://anonfb.com/api/convert"
            data = {"url": url}

            r = requests.post(api, data=data).json()
            dl_link = r["links"][0]["url"]

            fname = DOWNLOAD_DIR + "facebook_video.mp4"
            open(fname, "wb").write(requests.get(dl_link).content)

            Clock.schedule_once(lambda dt: show_popup("Download Facebook selesai!"), 0)

        except Exception as e:
            Clock.schedule_once(lambda dt: show_popup(f"Error Facebook: {str(e)}"), 0)


# ------------------------------------------------------------
# Halaman Tools
# ------------------------------------------------------------
class ToolsPage(Screen):

    def check_ip(self):
        try:
            ipinfo = requests.get("https://api.ipify.org?format=json").json()
            show_popup(f"IP Kamu: {ipinfo['ip']}")
        except:
            show_popup("Gagal mengambil IP!")


# ------------------------------------------------------------
# Settings Page
# ------------------------------------------------------------
class SettingsPage(Screen):
    pass


# ------------------------------------------------------------
# Screen Manager
# ------------------------------------------------------------
class MainApp(ScreenManager):
    pass


# ------------------------------------------------------------
# Main App Loader
# ------------------------------------------------------------
class MultiDownloaderID(App):

    def build(self):
        return Builder.load_file("multi.kv")


# ------------------------------------------------------------
# Start App
# ------------------------------------------------------------
if __name__ == "__main__":
    MultiDownloaderID().run()