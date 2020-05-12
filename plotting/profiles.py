import ROOT
import utils

def Partition(C, Nx, Ny, lMargin, rMargin, bMargin, tMargin):
    if C == None:
        return
    # Setup Pad layout:
    vSpacing = 0.01
    vStep = (1. - bMargin - tMargin - (Ny - 1) * vSpacing) / Ny
    hSpacing = 0.01
    hStep = ((1. - lMargin - rMargin - (Nx - 1) * hSpacing) / Nx) * 0.88
    vposd, vposu, vmard, vmaru, vfactor = 0.0, 0.0, 0.0, 0.0, 0.0
    hposl, hposr, hmarl, hmarr, hfactor = 0.0, 0.0, 0.0, 0.0, 0.0
    for i in range(Nx):
        if i==0:
            hposl = 0.0
            hposr = lMargin + hStep
            hfactor = hposr - hposl
            hmarl = lMargin / hfactor
            hmarr = 0.0
        elif i==Nx-1:
            hposl = hposr + hSpacing
            hposr = hposl + hStep + rMargin
            hfactor = hposr - hposl
            hmarl = 0.0
            hmarr = rMargin / (hposr - hposl)
        else:
            hposl = hposr + hSpacing
            hposr = hposl + hStep
            hfactor = hposr - hposl
            hmarl = 0.0
            hmarr = 0.0

        for j in range(Ny):
            if j==0:
                vposd = 0.0
                vposu = bMargin + vStep
                vfactor = vposu - vposd
                vmard = bMargin / vfactor
                vmaru = 0.0
            elif j==Ny-1:
                vposd = vposu + vSpacing
                vposu = vposd + vStep + tMargin
                vfactor = vposu - vposd
                vmard = 0.0
                vmaru = tMargin / (vposu - vposd)
            else:
                vposd = vposu + vSpacing
                vposu = vposd + vStep
                vfactor = vposu - vposd
                vmard = 0.0
                vmaru = 0.0
            C.cd(0)
            pad = ROOT.TPad("pad_{}_{}".format(i, j), "", hposl, vposd, hposr, vposu)
            pad.SetLeftMargin(hmarl)
            pad.SetRightMargin(hmarr)
            pad.SetBottomMargin(vmard)
            pad.SetTopMargin(vmaru)
            pad.SetFrameBorderMode(0)
            pad.SetBorderMode(0)
            pad.SetBorderSize(0)
            pad.SetLogz()
            pad.Draw()


def profiles():

    el_file = ROOT.TFile("data/profile_electrons.root")
    mu_file = ROOT.TFile("data/profile_muons.root")
    pi_file = ROOT.TFile("data/profile_pions.root")
    pr_file = ROOT.TFile("data/profile_protons.root")

    el_d = el_file.Get("fRho")
    mu_d = mu_file.Get("fRho")
    pi_d = pi_file.Get("fRho")
    pr_d = pr_file.Get("fRho")

    el_d.SetLineColor(ROOT.kGreen + 1)
    el_d.SetTitle("e")
    mu_d.SetLineColor(ROOT.kRed + 1)
    mu_d.SetTitle("#mu")
    pi_d.SetLineColor(ROOT.kBlue + 1)
    pi_d.SetTitle("#pi^{#pm}")
    pr_d.SetLineColor(ROOT.kBlack)
    pr_d.SetTitle("P")

    hists = [el_d, mu_d, pi_d, pr_d]
    utils.create_plot("../diagrams/cvn/emission_distance.png", hists, "Distance (cm) Fraction of emitted photons",
                      0, 1400, 0, 0.006, "L", "same", False, False)

    ROOT.gStyle.SetOptLogz(1)

    # Get the normalised emission profiles
    el_g = el_file.Get("fGFine")
    el_g.GetXaxis().SetTitle("Cosine emission angle")
    el_g.GetYaxis().SetTitle("Distance (cm)")
    mu_g = mu_file.Get("fGFine")
    mu_g.GetXaxis().SetTitle("Cosine emission angle")
    mu_g.GetYaxis().SetTitle("Distance (cm)")
    pi_g = pi_file.Get("fGFine")
    pi_g.GetXaxis().SetTitle("Cosine emission angle")
    pi_g.GetYaxis().SetTitle("Distance (cm)")
    pr_g = pr_file.Get("fGFine")
    pr_g.GetXaxis().SetTitle("Cosine emission angle")
    pr_g.GetYaxis().SetTitle("Distance (cm)")

    profile_c = ROOT.TCanvas("profile_c", "profile_c", 1000, 800)
    profile_c.SetFillStyle(4000)
    # Number of PADS
    Nx = 2
    Ny = 2
    # Margins
    lMargin = 0.1
    rMargin = 0.02
    bMargin = 0.1
    tMargin = 0.05
    # Canvas setup
    Partition(profile_c, Nx, Ny, lMargin, rMargin, bMargin, tMargin)

    TPaletteAxis *palette
    ROOT.TPad *pad[Nx][Ny]

    pad = [[]]

    for i in range(Nx):
        for j in range(Ny):
            profile_c.cd(0)
            # Get the pads previously created.
            pad[i][j] = ROOT.gROOT.FindObject("pad_{}_{}".format(i, j))
            ROOT.gPad.SetLogz()
            pad[i][j].Draw()
            pad[i][j].SetFillStyle(4000)
            pad[i][j].SetFrameFillStyle(4000)
            pad[i][j].cd()
            # Size factors
            xFactor = pad[0][0].GetAbsWNDC() / pad[i][j].GetAbsWNDC()
            yFactor = pad[0][0].GetAbsHNDC() / pad[i][j].GetAbsHNDC()
            hFrame = el_g.Clone("h_{}_{}".format(i, j))
            hFrame.Reset()
            # Format for y axis
            hFrame.GetYaxis().SetRangeUser(10, 1400)
            hFrame.GetYaxis().SetLabelFont(43)
            hFrame.GetYaxis().SetLabelSize(16)
            hFrame.GetYaxis().SetLabelOffset(0.02)
            hFrame.GetYaxis().SetTitleFont(43)
            hFrame.GetYaxis().SetTitleSize(30)
            hFrame.GetYaxis().SetTitleOffset(2.5)
            hFrame.GetYaxis().CenterTitle()
            hFrame.GetYaxis().SetNdivisions(505)
            hFrame.GetYaxis().SetTickLength(xFactor * 0.04 / yFactor)
            # Format for x axis
            hFrame.GetXaxis().SetRangeUser(0.3, 1.1)
            hFrame.GetXaxis().SetLabelFont(43)
            hFrame.GetXaxis().SetLabelSize(16)
            hFrame.GetXaxis().SetLabelOffset(0.02)
            hFrame.GetXaxis().SetTitleFont(43)
            hFrame.GetXaxis().SetTitleSize(30)
            hFrame.GetXaxis().SetTitleOffset(2.5)
            hFrame.GetXaxis().CenterTitle()
            hFrame.GetXaxis().SetNdivisions(505)
            hFrame.GetXaxis().SetTickLength(yFactor * 0.06 / xFactor)
            # Format for the z axis
            hFrame.GetZaxis().SetRangeUser(0, 0.01)

            # Draw the frame and the plot
            hFrame.Draw()
            text = ROOT.TLatex(.1, .93, "hello")

            if i==0 and j==0:
                text.SetTextSize(2.6 / 30.)
                text.DrawText(0.375, 1200, "charged pion")
                pi_g.Draw("sameCOL")
            if i==0 and j==1:
                text.SetTextSize(3 / 30.)
                text.DrawText(0.375, 1200, "electron")
                el_g.Draw("sameCOL")
            if i==1 and j==0:
                text.SetTextSize(2.6 / 30.)
                text.DrawText(0.375, 1200, "proton")
                pr_g.Draw("sameCOL")
            if i==1 and j==1:
                text.SetTextSize(3 / 30.)
                text.DrawText(0.375, 1200, "muon")
                mu_g.Draw("sameCOL")
                palette = ROOT.TPaletteAxis(0.90, 0.1, 0.93, 0.95, mu_g)

            ROOT.gPad.Update()
            ROOT.gPad.RedrawAxis()
            l = ROOT.TLine()
            l.SetLineWidth(3)
            l.DrawLine(ROOT.gPad.GetUxmin(), ROOT.gPad.GetUymin(), ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymin())
            l.DrawLine(ROOT.gPad.GetUxmin(), ROOT.gPad.GetUymin(), ROOT.gPad.GetUxmin(), ROOT.gPad.GetUymax())
            l.DrawLine(ROOT.gPad.GetUxmin(), ROOT.gPad.GetUymax(), ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax())
            l.DrawLine(ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymin(), ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax())

    profile_c.cd()
    palette.Draw("same")
    profile_c.SetLogz()
    profile_c.Draw()

    # Save canvas as png and root macro
    profile_c.SaveAs("../diagrams/cvn/emission_profile.png")

    el_file.Close()
    mu_file.Close()
    pi_file.Close()
    pr_file.Close()


if __name__ == "__main__":
    profiles()