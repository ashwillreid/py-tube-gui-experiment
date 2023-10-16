import tkinter
import customtkinter
import pytube

# FUNCTIONS
def startDownload( url ):
	try:
		ytObject = pytube.YouTube(url)
		video = ytObject.streams.get_highest_resolution()
		print(video)
		video.download()
	except Exception as error:
		print("Error:", error)
	print("Download Complete")

def searchVideo():
	try:
		inputString = searchVal.get()
		print(inputString)
		ytObject = pytube.Search(inputString)
		topResult = ytObject.results[0]
		print('TOP RESULT', topResult)
		startDownload(topResult.watch_url)
	except Exception as error:
		print("Error:", error)

# SYSTEM SETTINGS
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# APP FRAME
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# APP CONTENT

title = customtkinter.CTkLabel(app, text="YouTube Downloader", font=("Arial", 20))
title.pack(padx = 10, pady = 10)

inputString = tkinter.StringVar()
searchVal = customtkinter.CTkEntry(app, width=350, height=40, textvariable=inputString)
searchVal.pack()

searchButton = customtkinter.CTkButton(app, text="Search", command=searchVideo)
searchButton.pack(padx = 10, pady = 10)

# APP RUNNER
app.mainloop()