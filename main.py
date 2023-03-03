import tkinter
import customtkinter
from pytube import YouTube
import os
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("minimal example app")
        self.minsize(400, 300)
        #app frame
        self.geometry("720x480")
        self.title("Youtube Downloader")
        #### FRAME1 
        ##############
        self.frame1 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.frame1.grid(row=0, column=0, padx=10,pady=10, sticky="ns")
        #title element 
        self.title = customtkinter.CTkLabel(self.frame1,text="Insert a youtube link")
        self.title.grid(row=0, column=1,columnspan=2,padx=10,pady=10)

        # link input
        self.url_var =tkinter.StringVar()
        self.link_input = customtkinter.CTkEntry(self.frame1, width=350,height=40,textvariable=self.url_var)
        self.link_input.grid(row=1, column=0,columnspan=5,padx=10,pady=10)

        # folder path entry:
        self.folderPath = tkinter.StringVar()
        # set default path
        self.folderPath.set(os.path.expanduser("~/Downloads"))
        self.Path_entry = customtkinter.CTkLabel(self.frame1,textvariable=self.folderPath)
        self.Path_entry.grid(row=2, column=0,padx=10,pady=10)

        # folder path button:
        self.pathButton = customtkinter.CTkButton(self.frame1, text="Save to Directory", command=self.getFolderPath)
        self.pathButton.grid(row=2, column=4,padx=10,pady=10)

        #### FRAME2 
        ##############
        self.frame2 = customtkinter.CTkFrame(self, width=140, corner_radius=0, fg_color="transparent")
        self.frame2.grid(row=0, column=1,padx=10,pady=10, sticky="nsew")
        # #download button 
        self.downloadbutton = customtkinter.CTkButton(self.frame2,height=40,fg_color="green", text="Download", command=self.download)
        self.downloadbutton.grid(row=1, column=1,padx=20,pady=10)


        # # progress bar/FRAME3
        self.frame3 = customtkinter.CTkFrame(self, width=200, corner_radius=0)
        
        self.videodownloading = customtkinter.CTkLabel(self.frame3,text="")
        
        self.progressText = customtkinter.CTkLabel(self.frame3,text="dsdfd")
        
        self.progressBar = customtkinter.CTkProgressBar(self.frame3,width = 400)


        #### FRAME4
        ##############
        self.frame4 = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.frame4.grid(row=3, column=0,columnspan=2, padx=10,pady=10, sticky="ns")
        # # #Status
        self.StatusLabel = customtkinter.CTkLabel(self.frame4,text="")
        self.StatusLabel.grid(row=0, column=0,padx=10,pady=10, sticky="nsew")

    def download(self):
        try:
            # find link and video
            ytlink= self.link_input.get()
            ytObject = YouTube(ytlink, on_progress_callback=self.on_progress)
            self.videodownloading.configure(text=ytObject.title)
            video= ytObject.streams.get_highest_resolution()
            # show progress and download
            self.progressBar.set(0)
            self.frame3.grid(row=2, column=0,columnspan =2, padx=10,pady=10, sticky="nsew")
            self.videodownloading.grid(row=0, column=0,padx=10,pady=10, sticky="nsew")
            self.progressText.grid(row=1, column=0,padx=10,pady=10, sticky="nsew")
            self.progressBar.grid(row=1, column=1,padx=10,pady=10, sticky="nsew")

            video.download(self.folderPath.get())
            self.StatusLabel.configure(text="Video Downladed",text_color="green")
        except:
            self.StatusLabel.configure(text="Download error",text_color="red")
        self.resetUI()

    def on_progress(self,stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size- bytes_remaining
        Complete_Perct= bytes_downloaded/total_size *100
        progressTextvalue = str(int(Complete_Perct))+"%"
        self.progressText.configure(text=progressTextvalue)
        self.progressText.update()
        self.progressBar.set(float(Complete_Perct/100))

    def resetUI(self):
        self.title.configure("Insert a youtube link")
        self.frame3.grid_forget()
        self.videodownloading.grid_forget()
        self.progressText.grid_forget()
        self.progressBar.grid_forget()
        
    def getFolderPath(self):
        folder_selected = tkinter.filedialog.askdirectory()
        if folder_selected !="":
            self.folderPath.set(folder_selected)
    # run app
if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    app = App()
    app.mainloop()