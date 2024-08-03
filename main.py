import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import yt_dlp


def download_video():
    url = entry_url.get()
    if not url:
        messagebox.showerror("Input Error", "Please enter a valid video URL.")
        return

    try:
        # Define download options
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{download_folder}/%(title)s.%(ext)s',
            'ffmpeg_location': '/path/to/ffmpeg/bin',  # Replace with the path to ffmpeg on your system
            'noplaylist': True,  # To download single video only
        }

        # Download video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Success", "Video downloaded successfully!")

    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {e}")


def select_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        global download_folder
        download_folder = folder_selected
        lbl_folder.config(text=f"Download Folder: {download_folder}")


def main():
    global entry_url, lbl_folder, download_folder

    # Initialize download folder
    download_folder = ""

    # Create the main window
    root = tk.Tk()
    root.title("Instagram Video Downloader")

    # URL input frame
    frame_url = tk.Frame(root)
    frame_url.pack(pady=10)

    tk.Label(frame_url, text="Video URL:").grid(row=0, column=0, padx=5, pady=5)
    entry_url = tk.Entry(frame_url, width=50)
    entry_url.grid(row=0, column=1, padx=5, pady=5)

    # Folder selection frame
    frame_folder = tk.Frame(root)
    frame_folder.pack(pady=10)

    lbl_folder = tk.Label(frame_folder, text="Download Folder: Not selected")
    lbl_folder.pack(pady=5)

    btn_select_folder = tk.Button(frame_folder, text="Select Folder", command=select_folder)
    btn_select_folder.pack(pady=5)

    # Download button
    btn_download = tk.Button(root, text="Download Video", command=download_video)
    btn_download.pack(pady=20)

    # Run the application
    root.mainloop()


if __name__ == "__main__":
    main()
