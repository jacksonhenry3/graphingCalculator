#graphing calculator
import wx
from sympy import Symbol,diff,integrate,sin,cos,tan
#from pylab import *



def scale_bitmap(bitmap, width, height):
    image = wx.ImageFromBitmap(bitmap)
    image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
    result = wx.BitmapFromImage(image)
    return result


#creates a class that inherits from wx.Frame
class MyFrame(wx.Frame):
    #the constructor
    def __init__(self,parent,id,title):
        #creates a wx Frame based on parameters given in argument
        wx.Frame.__init__(self,parent,id,title,wx.DefaultPosition,wx.Size(1180,639))
        
        #creates a panel widget in  which to place children
        panel = wx.Panel(self,-1)


        wx.Button(panel, 1, 'plot', (1085,4+25))
        wx.Button(panel, 2, 'Integrate     ',(805,35+25))
        wx.Button(panel, 3, 'Differentiate',(805,65+25))


        # another child, the input box
        self.eq = wx.TextCtrl(panel, -1, 'equation goes here', (805,5+25), (275, -1))
        self.DiffOut = wx.TextCtrl(panel, -1, '', (890,66+25), (270, -1), style = wx.TE_READONLY)
        self.IntOut = wx.TextCtrl(panel, -1, '', (890,36+25), (270, -1), style = wx.TE_READONLY)


        #binds the buttons to the proper commands
        self.Bind(wx.EVT_BUTTON,self.OnPlot,id = 1)
        self.Bind(wx.EVT_BUTTON,self.OnDiff,id = 3)
        self.Bind(wx.EVT_BUTTON,self.OnInt,id = 2)

        #wx.StaticLine(panel,-1,(805,30),(355,1))
        wx.StaticText(panel, -1, "x min", (1130, 130))
        self.Xmin = wx.Slider(panel, 100, -10, -100, 100, pos=(805, 115),size=(320, -1),style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
        self.Xmin.SetTickFreq(5, 1)
        
        wx.StaticText(panel, -1, "x max", (1130, 180))
        self.Xmax = wx.Slider(panel, 100, 10, -100, 100, pos=(805, 165),size=(320, -1),style=wx.SL_HORIZONTAL | wx.SL_AUTOTICKS | wx.SL_LABELS )
        self.Xmax.SetTickFreq(5, 1)

        
    
        
    
    def OnDiff(self,event):
        equation = self.eq.GetValue()
        x = Symbol("x")
        equation = (diff(equation,x))
        self.DiffOut.Clear()
        self.DiffOut.AppendText(str(equation))
    def OnInt(self,event):
        equation = self.eq.GetValue()
        x = Symbol("x")
        equation = (integrate(equation,x))
        self.IntOut.Clear()
        self.IntOut.AppendText(str(equation))
    def OnPlot(self,event):
        from pylab import sin,cos,tan,log,close,grid,savefig,arange,plot
        close()
        equation = self.eq.GetValue()
        xmin = self.Xmin.GetValue()
        xmax = self.Xmax.GetValue()
        x = arange(xmin,xmax,(xmax-xmin)/(1000.))
        y = eval(equation)
        plot(x,y)
        grid(True)
        savefig("test.png",facecolor = (.6,.6,.6))
        image = wx.Bitmap("test.png")
        #image = scale_bitmap(image, 500, 500)
        wx.StaticBitmap(self, 0, image)
        self.Refresh()
    #def OnClear(self,event):
        

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None, -1, 'Graphing calculator')
        frame.Show(True)
        #self.SetTopWindow(frame)
        return True


app = MyApp(0)
app.MainLoop()

"""
Implicit differentiation
Stationary point
Maxima and minima
Differential equation
Taylor polynomials
L'Hopital's rule
Mean value theorem
Related rates
"""

"""
Indefinite integral
Trapezium rule
Integral of the secant function
Arclength
"""
