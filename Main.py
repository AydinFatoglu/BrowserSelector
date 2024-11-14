import wx
import subprocess
import argparse
import sys

class MyApp(wx.App):
    def __init__(self, command1, command2):
        self.command1 = command1
        self.command2 = command2
        super().__init__()

    def OnInit(self):
        frame = MyFrame(None, title="Browser Selector", command1=self.command1, command2=self.command2)
        frame.Centre()  # Center the frame on the screen
        frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, title, command1, command2):
        # Set style to remove minimize and maximize buttons
        super().__init__(parent, title=title, size=(400, 300), style=wx.CLOSE_BOX | wx.CAPTION | wx.SYSTEM_MENU)
        
        # Save commands
        self.command1 = command1
        self.command2 = command2

        # Panel for organizing layout
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.BLACK)  # Set panel background to black

        # Add description text at the top
        description = wx.StaticText(panel, label="Select Browser to Open the Page", style=wx.ALIGN_CENTER)
        description.SetForegroundColour(wx.WHITE)  # Set text color to white for visibility
        description.SetBackgroundColour(wx.BLACK)  # Ensure background is black

        # Set font size for description
        font = description.GetFont()
        font.PointSize += 4  # Increase font size
        description.SetFont(font)

        # Load icons from PNG files and resize to 128x128
        icon1 = wx.Bitmap("icon1.png", wx.BITMAP_TYPE_PNG).ConvertToImage().Scale(128, 128).ConvertToBitmap()
        icon2 = wx.Bitmap("icon2.png", wx.BITMAP_TYPE_PNG).ConvertToImage().Scale(128, 128).ConvertToBitmap()

        # Create buttons with resized icons
        btn1 = wx.BitmapButton(panel, bitmap=icon1, size=(150, 150))
        btn2 = wx.BitmapButton(panel, bitmap=icon2, size=(150, 150))

        # Bind button events to methods that run commands
        btn1.Bind(wx.EVT_BUTTON, self.on_run_command1)
        btn2.Bind(wx.EVT_BUTTON, self.on_run_command2)

        # Horizontal box sizer to align icons side by side
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add(btn1, 0, wx.ALL | wx.CENTER, 10)
        hbox.Add(btn2, 0, wx.ALL | wx.CENTER, 10)

        # Vertical box sizer to center description and buttons within the panel
        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(description, 0, wx.ALL | wx.ALIGN_CENTER, 10)  # Add description at the top center
        vbox.Add(hbox, 0, wx.ALL | wx.CENTER, 10)  # Add buttons below

        # Set sizer for the panel to arrange content
        panel.SetSizer(vbox)

    def on_run_command1(self, event):
        subprocess.run(self.command1, shell=True)
        self.Close()  # Close the main window after the command completes

    def on_run_command2(self, event):
        subprocess.run(self.command2, shell=True)
        self.Close()  # Close the main window after the command completes

def show_message_box(message):
    """Displays a message box with the given message."""
    app = wx.App(False)
    wx.MessageBox(message, "Error", wx.OK | wx.ICON_ERROR)

def main():
    # Argument parsing with error handling
    parser = argparse.ArgumentParser(description="Browser Selector")
    parser.add_argument("--c1", type=str, help="Command to run for button 1")
    parser.add_argument("--c2", type=str, help="Command to run for button 2")

    # Parse arguments with custom error handling
    try:
        args = parser.parse_args()
    except SystemExit as e:
        # Handle argparse errors by showing a message box
        show_message_box(
            "Please provide both --c1 and --c2 commands.\n\n"
            "Usage:\n"
            "browserselector.exe --c1='start chrome https://yoursite.com' --c2='start msedge https://yoursite.com'\n\n"
            "Explanation:\n"
            "You can specify any browser to open the desired website as long as the correct command is provided."
        )
        sys.exit(1)  # Exit after showing message box

    # Check if both arguments are provided
    if not args.c1 or not args.c2:
        show_message_box(
            "Please provide both --c1 and --c2 commands.\n\n"
            "Usage:\n"
            "browserselector.exe --c1='start chrome https://yoursite.com' --c2='start msedge https://yoursite.com'\n\n"
            "Explanation:\n"
            "You can specify any browser to open the desired website as long as the correct command is provided."
        )
        return  # Exit without starting the main app

    # Start the app with the provided commands
    app = MyApp(command1=args.c1, command2=args.c2)
    app.MainLoop()

if __name__ == "__main__":
    main()

