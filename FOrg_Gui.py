import wx


class Window(wx.Frame):
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(1920,1080), pos=(0,1))
		
		
		
app = wx.App(False)
window = Window(None, 'Financial Organizer')
window.Show()
app.MainLoop()
