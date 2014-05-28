'''
Created on 05/04/2012

@author: lucask
'''
import wx

labels = "one two three four".split()

class TestFrame(wx.Frame):
    title = "none"
    def __init__(self):
        wx.Frame.__init__(self, None, -1, self.title)
        sizer = self.CreateSizerAndWindows()
        self.SetSizer(sizer)
        self.Fit()
        
class VBoxSizerFrame(TestFrame):
    title = "Vertical BoxSizer"
    
    def CreateSizerAndWindows(self):
        sizer = wx.BoxSizer(wx.VERTICAL)
        for label in labels:
            bw = wx.Button(self, label='Open', size=(80, 25))

            # bw = BlockWindow(self, label=label, size=(200,30))
            sizer.Add(bw, flag=wx.EXPAND)
        return sizer
    
app = wx.PySimpleApp()
frame = VBoxSizerFrame()
frame.Show()
app.MainLoop()