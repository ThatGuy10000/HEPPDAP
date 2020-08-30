import wx

class MainApp(wx.App):
    #Initialize the app  
    def __init__(self):
        super().__init__(clearSigInt=True)
        print(1)
    #init frame
        frame = Channelnameframe("Channel Designations")
        frame.SetSize(1000,800)
        frame.Show()


class Channelnameframe (wx.Frame):
    """
    Class used for creating frames other than the main one
    """
    
    def __init__(self, title, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        chanpanel = ChannelPanel(self)
        self.Show()
       


class ChannelPanel(wx.Panel):
    
    def __init__(self, parent):
       wx.Panel.__init__(self, parent)
       self.build()

    def build(self):
        channelsizer = wx.BoxSizer(wx.HORIZONTAL)
        board1sizer = wx.BoxSizer(wx.VERTICAL)
        board2sizer = wx.BoxSizer(wx.VERTICAL)
        boards = [board1sizer, board2sizer]
        channelnamematrix = [[],[]]
        for board in boards:
            for chan in range(4):
                channel = wx.BoxSizer(wx.HORIZONTAL)
                label = wx.StaticText(self, label = "Channel %s" % str(chan + 1))
                text = wx.TextCtrl(self, value = "", size = (100, 20))
                channel.Add(label, 0, wx.ALL, 0)
                channel.Add(text, 0, wx.ALL, 0)
                board.Add(channel, 0, wx.ALL, 0)
            channelsizer.Add(board, 0, wx.ALL, 0)

        self.SetSizer(channelsizer)        

def main():
    app = MainApp()
    app.MainLoop()

if __name__ == "__main__":
    main()



