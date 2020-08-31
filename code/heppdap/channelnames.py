import wx

class Channelnameframe (wx.Frame):
    """
    Class used for creating frames other than the main one
    """
    
    def __init__(self, title, matrix, parent=None):
        wx.Frame.__init__(self, parent=parent, title=title)
        self.chanpanel = ChannelPanel(self, matrix)
        self.Show()

    def getchannelnames(self):
        return self.chanpanel.channels

class ChannelPanel(wx.Panel):
    
    def __init__(self, parent, matrix):
       self.parent = parent
       wx.Panel.__init__(self, parent)
       self.build(matrix)

       self.channels = [["Channel 1", "Channel 2", "Channel 3", "Channel 4"], ["Channel 1", "Channel 2", "Channel 3", "Channel 4"]]

    def build(self, channelmatrix):
        channelsizer = wx.BoxSizer(wx.HORIZONTAL)
        board1sizer = wx.BoxSizer(wx.VERTICAL)
        board2sizer = wx.BoxSizer(wx.VERTICAL)
        self.boards = [board1sizer, board2sizer]


        for boardsizer, board  in zip(self.boards, channelmatrix):
            for chan in range(4):
                channel = wx.BoxSizer(wx.HORIZONTAL)
                label = wx.StaticText(self, label = "Channel %s" % str(chan + 1))
                if chan + 1 in board:
                    text = wx.TextCtrl(self, value = "", size = (100, 20))
                else:
                    text = wx.StaticText(self, id=wx.ID_ANY, label = "Channel Unavailable") 

                channel.Add(label, 0, wx.ALL, 0)
                channel.Add(text, 0, wx.ALL, 0)
                boardsizer.Add(channel, 0, wx.ALL, 0)
            channelsizer.Add(boardsizer, 0, wx.ALL, 0)
        ok = wx.Button(self, wx.ID_ANY, "OK")
        self.Bind(wx.EVT_BUTTON, self.closeout, ok)
        channelsizer.Add(ok, 0, wx.ALL, 0)
        self.SetSizer(channelsizer)
         
    
    def closeout(self, event):
        self.channels = [[],[]]
        b = 0
        c = 0
        for board in self.boards:
            for channel in board:
                text = channel.GetSizer().GetChildren()[1].GetWindow()
                if isinstance(text, wx.TextCtrl):
                    if text.GetValue() != "":
                        self.channels[b].append(text.GetValue())
                    else:
                        self.channels[b].append ("Channel %s" % str(c + 1))

                else:
                    self.channels[b].append("Channel Unavailable")
                c += 1
            b += 1


        self.parent.Destroy()
        
