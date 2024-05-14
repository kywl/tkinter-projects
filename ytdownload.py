# download yt videos using tkinter and pytube
# added a gui icon by converting pic to base64, went further with styling, and added a light-dark mode functionality

from tkinter import *
import tkinter as tk
from tkinter import messagebox
from moviepy.editor import *
import pytube

# root window
root = tk.Tk()
theme_night = False
root.option_add('*background', '#fff8f1')  # Set default background color for all widgets
root.option_add('*foreground', '#241c19')  # Set default foreground color for all widgets (font color)
root.title("Youtube Video Downloader")
root.geometry('400x230')
root.configure(bg="#fff8f1")
root.resizable(width=False, height=False)
icon_data = (
    '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'
    'rkJggg=='
)
image = PhotoImage(data=icon_data)
root.iconphoto(False, image)

# theme mode button
theme = Button(root, text="night", font=("Consolas", 8), bg="#EBE8E4", command=lambda: change_theme())
theme.pack(side=TOP, anchor='ne', pady=5, padx=5)

title = Label(root, text="Download yt videos", font=("Consolas", 20), fg="#3D312B")
title.pack(side=TOP, pady=5)


def change_theme():
    global theme_night
    if theme_night:
        # Switch to light theme
        root.configure(bg='#fff8f1')  # Light background color
        title.config(bg='#fff8f1', fg='#3D312B')  # Dark text color
        link_label.config(bg='#fff8f1', fg='#241c19')
        enter_link.config(bg='#fff8f1', fg='#241c19')
        link_frame.config(bg='#fff8f1')
        res_frame.config(bg='#fff8f1')
        res.config(bg='#fff8f1', fg='#241c19')
        res_480p.config(bg='#fff8f1', fg='#241c19')
        res_720p.config(bg='#fff8f1', fg='#241c19')
        res_1080p.config(bg='#fff8f1', fg='#241c19')
        name.config(bg='#fff8f1', fg='#241c19')
        enter_name.config(bg='#fff8f1', fg='#241c19')
        name_frame.config(bg='#fff8f1')
        theme.config(bg='#EBE8E4', fg="#241c19", text='dark')
        submit.config(bg="#ff6e6e")
        theme_night = False
    else:
        # Switch to dark theme
        root.configure(bg='#0c0908')  # Dark background color
        title.config(bg='#0c0908', fg='#32E500')  # Light text color
        link_label.config(bg='#0c0908', fg='#32E500')
        enter_link.config(bg='#0c0908', fg='#32E500')
        link_frame.config(bg='#0c0908')
        res.config(bg='#0c0908', fg='#32E500')
        res_frame.config(bg='#0c0908')
        res_480p.config(bg='#0c0908', fg='#32E500')
        res_720p.config(bg='#0c0908', fg='#32E500')
        res_1080p.config(bg='#0c0908', fg='#32E500')
        name.config(bg='#0c0908', fg='#32E500')
        enter_name.config(bg='#0c0908', fg='#32E500')
        name_frame.config(bg='#0c0908')
        theme.config(bg='#444444', text='light', fg="#32E500")
        submit.config(bg="#FF1313")
        theme_night = True


# get link for yt vid to be downloaded
def download_video():
    # get info
    link = enter_link.get()
    print(link)
    file_name = enter_name.get()
    print(file_name)
    resolution = selected_resolution.get()
    print(resolution)

    # input checks
    if not link.strip():
        messagebox.showwarning("Error", "Please enter a valid youtube link")
        return
    if not file_name.strip():
        messagebox.showwarning("Error", "Please enter a name for the video")
        return
    if not resolution.strip():
        messagebox.showwarning("Error", "Please Select a resolution")
        return

    # download in downloads folder
    download_path = os.path.expanduser("~\\Downloads")
    print(f"Downloading video to {download_path}")

    # download the videos
    try:
        yt = pytube.YouTube(link)
        # filter for video and audio with intended resolution and mp4 format
        video_stream = yt.streams.filter(res=resolution, file_extension='mp4', progressive=False,
                                         only_video=True).first()
        audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()

        if not video_stream:
            messagebox.showwarning("Unavailable", f"Video stream at {resolution} is unavailable.")
            return
        if not audio_stream:
            messagebox.showwarning("Unavailable", "Audio stream is unavailable.")
            return

        download_path = os.path.expanduser("~/Downloads")

        video_path = video_stream.download(output_path=download_path, filename=f"{file_name}_video.mp4")
        audio_path = audio_stream.download(output_path=download_path, filename=f"{file_name}_audio.mp4")

        video_clip = VideoFileClip(video_path)
        audio_clip = AudioFileClip(audio_path)
        final_clip = video_clip.set_audio(audio_clip)
        # combine video and audio then write to downloads folder
        final_clip.write_videofile(os.path.join(download_path, f"{file_name}.mp4"), codec="libx264")

        # delete separate video and audio files
        os.remove(video_path)
        os.remove(audio_path)

        messagebox.showinfo("Success", f"Video + Audio downloaded successfully at {download_path}/{file_name}.mp4")
    except Exception as e:
        messagebox.showerror("Download Failed", str(e))


# frame for link label and entry
link_frame = Frame(root)
link_frame.pack(side=TOP, fill='x', padx=10, pady=5)

# link label
link_label = Label(link_frame, text="Enter link:", font=("Consolas", 10))
link_label.pack(side=LEFT)

# user input the link
enter_link = Entry(link_frame, width=40, font=("Consolas", 10))
enter_link.pack(side=LEFT)

# get user's choice of resolution
# frame for res label and buttons
res_frame = Frame(root)
res_frame.pack(side=TOP, fill='x', padx=10, pady=5)

res = Label(res_frame, text="Resolution", font=("Consolas", 10))
res.pack(side=LEFT)

# frame for buttons
res_buttons = Frame(res_frame)
res_buttons.pack(side=LEFT, padx=10, pady=5)

# Function to update the selected resolution variable
selected_resolution = StringVar()


def set_resolution(video_resolution, btn):
    # raise all the button in case user changes mind and makes a different selection
    res_480p.configure(relief=RAISED)
    res_720p.configure(relief=RAISED)
    res_1080p.configure(relief=RAISED)
    selected_resolution.set(video_resolution)
    # recess button to indicate user selection
    btn.configure(relief=SUNKEN)


# Buttons for different resolutions
res_480p = Button(res_buttons, text="480", font=("Consolas", 10), bg="#EBE8E4",
                  command=lambda: set_resolution("480p", res_480p))
res_480p.pack(side=LEFT)

res_720p = Button(res_buttons, text="720", font=("Consolas", 10), bg="#EBE8E4",
                  command=lambda: set_resolution("720p", res_720p))
res_720p.pack(side=LEFT)  # no padding to keep them together

res_1080p = Button(res_buttons, text="1080", font=("Consolas", 10), bg="#EBE8E4",
                   command=lambda: set_resolution("1080p", res_1080p))
res_1080p.pack(side=LEFT)

# name the file
# frame for name label and entry field to name the file
name_frame = Frame(root)
name_frame.pack(side=TOP, fill='x', padx=10, pady=5)
name = Label(name_frame, text="Name file: ", font=("Consolas", 10))
name.pack(side=LEFT)

enter_name = Entry(name_frame, width=40, font=("Consolas", 10))
enter_name.pack(side=LEFT)

# submit button
submit = Button(root, text="GO", font=("Consolas", 10), bg="#ff6e6e", width=8, command=lambda: download_video())
submit.pack(side=TOP)

root.mainloop()

