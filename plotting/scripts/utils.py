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
# Now save plots with plt.savefig('histogram.pgf')

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
        self.SetFrameLineWidth(2)
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
        self.SetTitleSize(0.06, 'XYZ')
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


def plot_hists(hists, title, path, x_low, x_high, y_low, y_high,
               z_low=None, z_high=None, log_x=False, log_y=False, log_z=False,
               opt='LP', leg_opt=None, stack=False):
    """Plots the list of histograms to file as a png.
    Args:
        hists (list[ROOT.Hist]): List of histograms to plot
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
        stack (bool): Should we stack the histograms?
    """
    # Define an empty histogram to set global variables
    global_h = ROOT.TH2F('global_h', title, 1, x_low, x_high, 1, y_low, y_high)
    format_hist(global_h)

    # Set z-axis options if in use
    if z_low is not None and z_high is not None:
        global_h.GetZaxis().SetRangeUser(z_low, z_high)
        global_h.GetYaxis().SetTitleOffset(0.65)

    # Create the canvas and draw the global options histogram
    canvas = ROOT.TCanvas("canvas", "canvas", 1000, 800)
    canvas.cd()
    if log_x: 
        canvas.SetLogx()
    if log_y: 
        canvas.SetLogy()
    if log_z: 
        canvas.SetLogz()
    global_h.Draw()

    # Create the legend
    legend = None
    if leg_opt is not None:
        legend = ROOT.TLegend(0.7, 0.65, 0.85, 0.85)
        legend.SetFillStyle(0)
        for i in range(len(hists)):    
            legend.AddEntry(hists[i], hists[i].GetTitle(), leg_opt)
        legend.Draw("same")

    # Draw the histograms
    if stack:
        stack = ROOT.THStack("stack","")
        for i in range(len(hists)):
            stack.Add(hists[i])
        stack.Draw(opt)
    else:
        for i in range(len(hists)):
            hists[i].Draw(opt)

    canvas.Draw()
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