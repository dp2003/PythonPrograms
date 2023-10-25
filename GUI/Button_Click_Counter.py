from tkinter import *;
class MyApp(Frame):
    def __init__(self, master):
        Frame.__init__(self, master);
        self.grid();
        # below is the number of button clicks
        self.button_clicks = 0;
        self.create_widget();
    def create_widget(self):
        self.buttn = Button(self, text = "Total Clicks = 0");
        self.buttn["command"] = self.update_click_count;
        self.buttn.grid();
    def update_click_count(self):
        self.button_clicks += 1;
        self.buttn["text"] = "Total Clicks = " + str(self.button_clicks);
mainWindow = Tk();
mainWindow.title("GUI Event Handler");
mainWindow.geometry("300x200");
app = MyApp(mainWindow);
mainWindow.mainloop();