import sys
import enum
import array
import ROOT

import matplotlib as plt
plt.use("pgf")
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

import mplhep as hep
plt.style.use(hep.style.ROOT)


class CHIPSStyle(ROOT.TStyle):
    """The CHerenkov detectors In mine PitS project ROOT plotting style
    """

    def __init__(self, font=42, cont=255):
        """Initialise the CHIPSStyle class.
        Args:
            font (int): ROOT font code to use
            cont (int): Number of contours to use for colour pallette
        """
        super(CHIPSStyle, self).__init__('CHIPSStyle', 'CHIPS ROOT Style')
        self.SetTextFont(font)
        # Canvas
        self.SetCanvasBorderMode(0)
        self.SetCanvasColor(0)
        self.SetCanvasDefH(600)  # Height
        self.SetCanvasDefW(600)  # Width
        self.SetCanvasDefX(0)  # On-Screen Position
        self.SetCanvasDefY(0)
        # Pad
        self.SetPadBorderMode(0)
        self.SetPadColor(0)
        self.SetPadGridX(False)
        self.SetPadGridY(False)
        self.SetGridColor(0)
        self.SetGridStyle(3)
        self.SetGridWidth(1)
        # Frame
        self.SetFrameBorderMode(0)
        self.SetFrameBorderSize(1)
        self.SetFrameFillColor(0)
        self.SetFrameFillStyle(0)
        self.SetFrameLineColor(1)
        self.SetFrameLineStyle(1)
        self.SetFrameLineWidth(3)
        # Histogram
        self.SetHistLineColor(1)
        self.SetHistLineStyle(0)
        self.SetHistLineWidth(2)
        self.SetEndErrorSize(2)
        self.SetMarkerStyle(20)
        self.SetHistMinimumZero()
        # Fit/Function
        self.SetOptFit(1)
        self.SetFitFormat('5.4g')
        self.SetFuncColor(2)
        self.SetFuncStyle(1)
        self.SetFuncWidth(2)
        # Date
        self.SetOptDate(0)
        # Statistics Box
        self.SetOptFile(0)
        self.SetOptStat(0)  # Pass 'mr' to display the mean and RMS.
        self.SetStatColor(0)
        self.SetStatFont(font)
        self.SetStatFontSize(0.025)
        self.SetStatTextColor(1)
        self.SetStatFormat('6.4g')
        self.SetStatBorderSize(1)
        self.SetStatH(0.1)
        self.SetStatW(0.15)
        # Margins
        self.SetPadTopMargin(0.05)
        self.SetPadBottomMargin(0.13)
        self.SetPadLeftMargin(0.16)
        self.SetPadRightMargin(0.02)
        # Global Title
        self.SetOptTitle(0)  # 0 = No Title
        self.SetTitleFont(font)
        self.SetTitleColor(1)
        self.SetTitleTextColor(1)
        self.SetTitleFillColor(10)
        self.SetTitleFontSize(0.05)
        # Axis Titles
        self.SetTitleColor(1, 'XYZ')
        self.SetTitleFont(font, 'XYZ')
        self.SetTitleSize(0.05, 'XYZ')
        self.SetTitleXOffset(0.9)
        self.SetTitleYOffset(1.25)
        # Axis Labels
        self.SetLabelColor(1, 'XYZ')
        self.SetLabelFont(font, 'XYZ')
        self.SetLabelOffset(0.007, 'XYZ')
        self.SetLabelSize(0.05, 'XYZ')
        # Axes
        self.SetAxisColor(1, 'XYZ')
        self.SetStripDecimals(True)
        self.SetTickLength(0.03, 'XYZ')
        self.SetNdivisions(510, 'XYZ')
        # 0 = Text labels (and ticks) only on bottom, 1 = Text labels on top and bottom
        self.SetPadTickX(1)
        self.SetPadTickY(1)
        # Log Scale Axes
        self.SetOptLogx(0)
        self.SetOptLogy(0)
        self.SetOptLogz(0)
        # Postscript Options
        self.SetPaperSize(20, 20)
        # Hatches
        self.SetHatchesLineWidth(5)
        self.SetHatchesSpacing(0.05)
        # Legend
        self.SetLegendBorderSize(0)
        self.SetLegendFont(font)
        # Get modified colors for colz
        stops = [0.00, 0.34, 0.61, 0.84, 1.00]
        red = [0.00, 0.00, 0.87, 1.00, 0.51]
        green = [0.00, 0.81, 1.00, 0.20, 0.00]
        blue = [0.51, 1.00, 0.12, 0.00, 0.00]
        s = array.array('d', stops)
        r = array.array('d', red)
        g = array.array('d', green)
        b = array.array('d', blue)
        ROOT.TColor.CreateGradientColorTable(len(s), s, r, g, b, cont)
        self.SetNumberContours(cont)

    def __enter__(self):
        """Set the gStyle to ChipsStyle while remembering the previous gStyle."""
        self.previous_gStyle = ROOT.gROOT.GetStyle(ROOT.gStyle.GetName())
        self.cd()
        ROOT.gROOT.ForceStyle()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        """Reset to the previous gStyle.
        """
        self.previous_gStyle.cd()


class POS(enum.Enum):
    """Plot position enumeration.
    """
    TR = 1  # Top right
    RS = 2  # Right side
    TL = 3  # Top left


def label(label_text, position):
    """Generates a label in for the specified position.
    Args:
        label_text (str): Text for the label
        position (Enum.POS): Position enum code
    Returns:
        ROOT.TLatex: The label
    """
    x, y, angle, align = None, None, None, None
    if position is POS.TR:
        x = 0.90
        y = 0.95
        angle = 0
        align = 32
    elif position is POS.RS:
        x = 0.93
        y = 0.90
        angle = 270
        align = 12
    elif position is POS.TL:
        x = 0.10
        y = 0.95
        angle = 0
        align = 11
    else:
        raise NotImplementedError
    
    label = ROOT.TLatex(x, y, label_text)
    label.SetTextColor(4)
    label.SetNDC()
    label.SetTextSize(2/30.0)
    label.SetTextAngle(angle)
    label.SetTextAlign(align)
    return label


def format_hist(hist):
    """Generates a label on the side of the plot.
    Args:
        hist (ROOT.Hist): ROOT histogram to format
    Returns:
        ROOT.Hist: Formatted histogram
    """
    hist.GetXaxis().CenterTitle()
    hist.GetYaxis().CenterTitle()
    hist.GetZaxis().CenterTitle()


def plot(plots, title, path, x_low, x_high, y_low, y_high,
         z_low=None, z_high=None, log_x=False, log_y=False, log_z=False,
         opt='LP', leg_opt=None, leg_x=0.75, leg_y=0.70, stack=False,
         cuts=None, texts=None, grid_x=False, grid_y=False):
    """Plots the list of histograms to file as a png.
    Args:
        plots (list[ROOT.Hist]): List of histograms to plot
        title (str): Title for the plot (contains axis titles)
        path (str): Path to save plot
        x_low (float): Low x-axis value
        x_high (float): High x-axis value
        y_low (float): Low y-axis value
        y_high (float): High y-axis value
        z_low (float): Low z-axis value
        z_high (float): High z-axis value
        log_x (bool): Log the x-axis?
        log_y (bool): Log the y-axis?
        log_z (bool): Log the z-axis?
        opt (str): Histogram plotting option
        leg_opt (str): Legend plotting option
        leg_x (float): Legend x-position
        leg_y (float)L Legend y-position
        stack (bool): Should we stack the histograms?
        cuts (list[[low,high]]): List of cuts to show on plot
        texts (list[[text, x, y]]): List of text to show on plot
        grid_x (bool): Should we show the x-grid lines?
        grid_y (bool): Should we show the y-grid lines?
    """
    # Define an empty histogram to set global variables
    global_h = ROOT.TH2F('global_h', title, 1, x_low, x_high, 1, y_low, y_high)
    format_hist(global_h)

    # Set z-axis options if in use
    if z_low is not None and z_high is not None:
        global_h.GetZaxis().SetRangeUser(z_low, z_high)
        global_h.GetYaxis().SetTitleOffset(0.65)

    # Create the canvas and draw the global options histogram
    canvas = ROOT.TCanvas(path, "canvas", 1000, 800)
    canvas.cd()
    if log_x: 
        canvas.SetLogx()
    if log_y: 
        canvas.SetLogy()
    if log_z: 
        canvas.SetLogz()
    if grid_x:
        canvas.SetGridx()
    if grid_y:
        canvas.SetGridy() 
    global_h.Draw()

    # Create and draw the legend
    legend = None
    if leg_opt is not None:
        legend = ROOT.TLegend(leg_x, leg_y, leg_x+0.15, leg_y+0.20)
        legend.SetFillStyle(0)
        for i in range(len(plots)):    
            legend.AddEntry(plots[i], plots[i].GetTitle(), leg_opt)
        legend.Draw("same")

    # Create and draw the cuts lines/greyed out box
    if cuts is not None:
        for cut in cuts:
            low = ROOT.TLine(cut[0], y_low, cut[0], y_high)
            low.SetLineWidth(3)
            low.SetLineColor(1)
            box = ROOT.TBox(cut[0], y_low, cut[1], y_high)
            box.SetFillColor(17)
            # box.SetFillStyle(3144)
            high = ROOT.TLine(cut[1], y_low, cut[1], y_high)
            high.SetLineWidth(3)
            high.SetLineColor(14)
            if cut[0] == x_low:
                box.Draw()
                high.Draw()
            elif cut[1] == x_high:
                low.Draw()
                box.Draw()
            else:
                #low.Draw()
                box.Draw()
                #high.Draw()

    # Create any text needed
    if texts is not None:
        for text in texts:
            plot_text = ROOT.TLatex(text[1], text[2], '')
            plot_text.SetTextSize(text[3])
            plot_text.SetTextColor(text[4])
            plot_text.DrawText(text[1], text[2], text[0])

    # Draw the histograms
    if stack:
        stack = ROOT.THStack("stack","")
        for i in range(len(plots)):
            stack.Add(plots[i])
        stack.Draw(opt)
    else:
        for i in range(len(plots)):
            plots[i].Draw(opt)

    l = ROOT.TLine()
    l.SetLineWidth(3)
    l.DrawLine(x_low, y_low, x_high, y_low)
    l.DrawLine(x_low, y_low, x_low, y_high)
    l.DrawLine(x_high, y_low, x_high, y_high)
    l.DrawLine(x_low, y_high, x_high, y_high)

    #canvas.Draw()
    canvas.SaveAs(path)


def plot_tree(path, tree, var, title, x_bins, x_low, x_high):
    """Plot a variable from a TTree.
    Args:
        path (str): Path to save plot
        tree (ROOT.TTree): ROOT TTree to plot from
        var (str): Variable to plot from the TTree
        title (str): Title for the plot (contains axis titles)
        x_bins (int): Number of x-bins
        x_low (float): Low x-axis value
        x_high (float): High x-axis value
    """
    hist = ROOT.TH1F(var + "_h", title, x_bins, x_low, x_high)
    format_hist(hist)

    # Fill the histogram from the tree
    varexp = var + ">>" + var + "_h"
    selection = var + ">" + x_low + " && " + var + "<" + x_high

    # Draw the histogram to a canvas and save to file
    canvas = ROOT.TCanvas("canvas", "canvas", 1000, 800)
    tree.Draw(varexp, selection)
    hist.Scale(1/hist.GetEntries())
    hist.Draw("HIST")
    canvas.Draw()
    canvas.SaveAs(path)