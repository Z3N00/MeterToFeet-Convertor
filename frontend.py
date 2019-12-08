import backend
import wx

def press_button(event):
    meters = float(input_box.GetValue())
    result.SetLabel(str(backend.meters_feet(meters)))



app = wx.App()
frame = wx.Frame(parent = None, title = "Meters to feet")
panel = wx.Panel(frame)
sizer = wx.GridBagSizer(10, 100)

input_label = wx.StaticText(panel, label = "Metres: ")
input_box = wx.TextCtrl(panel)

result_label = wx.StaticText(panel, label = "Feet: ")
result = wx.StaticText(panel, label = "")

button = wx.Button(panel, label = "Convert")
button.Bind(wx.EVT_BUTTON, press_button)


sizer.Add(input_label, (0, 0))
sizer.Add(input_box, (0, 1.5))
sizer.Add(result_label, (1 ,0))
sizer.Add(result, (1, 1.5))
sizer.Add(button, (2, 1))


frame.SetSizerAndFit(sizer)
panel.SetSizerAndFit(sizer)
frame.Show()
app.MainLoop()
