// To set this as default, you need a .rootrc file in your home directory,
// containing the following line:
// Rint.Logon: /full/path/to/style.C

#ifndef STYLE_C
#define STYLE_C

#include "TColor.h"
#include "TH1.h"
#include "TLatex.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TH2F.h"
#include "TLegend.h"
#include "TCanvas.h"
#include "THStack.h"

void style()
{
    TStyle* style = new TStyle("style", "style");

    // Centre title
    style->SetTitleAlign(22);
    style->SetTitleX(.5);
    style->SetTitleY(.95);
    style->SetTitleBorderSize(0);

    // No info box
    style->SetOptStat(0);

    //set the background color to white
    style->SetFillColor(10);
    style->SetFrameFillColor(10);
    style->SetCanvasColor(10);
    style->SetPadColor(10);
    style->SetTitleFillColor(0);
    style->SetStatColor(10);

    // Don't put a colored frame around the plots
    style->SetFrameBorderMode(0);
    style->SetCanvasBorderMode(0);
    style->SetPadBorderMode(0);

    // Set the default line color for a fit function to be red
    style->SetFuncColor(kRed);

    // Marker settings
    style->SetMarkerStyle(kFullCircle);

    // No border on legends
    style->SetLegendBorderSize(0);

    // Disabled for violating CHIPS style guidelines
    // Scientific notation on axes
    //TGaxis::SetMaxDigits(3);

    // Axis titles
    style->SetTitleSize(.055, "xyz");
    style->SetTitleOffset(.8, "xyz");
    // More space for y-axis to avoid clashing with big numbers
    style->SetTitleOffset(.9, "y");
    // This applies the same settings to the overall plot title
    style->SetTitleSize(.055, "");
    style->SetTitleOffset(.8, "");
    // Axis labels (numbering)
    style->SetLabelSize(.04, "xyz");
    style->SetLabelOffset(.005, "xyz");

    // Prevent ROOT from occasionally automatically zero-suppressing
    style->SetHistMinimumZero();

    // Thicker lines
    style->SetHistLineWidth(3);
    style->SetFrameLineWidth(3);
    style->SetFuncWidth(3);

    // Set the number of tick marks to show
    style->SetNdivisions(506, "xyz");

    // Set the tick mark style
    style->SetPadTickX(1);
    style->SetPadTickY(1);

    // Fonts
    const int kCHIPSFont = 42;
    style->SetStatFont(kCHIPSFont);
    style->SetLabelFont(kCHIPSFont, "xyz");
    style->SetTitleFont(kCHIPSFont, "xyz");
    style->SetTitleFont(kCHIPSFont, ""); // Apply same setting to plot titles
    style->SetTextFont(kCHIPSFont);
    style->SetLegendFont(kCHIPSFont);

    // Get moodier colours for colz
    const Int_t NRGBs = 5;
    const Int_t NCont = 255;
    Double_t stops[NRGBs] = { 0.00, 0.34, 0.61, 0.84, 1.00 };
    Double_t red[NRGBs]   = { 0.00, 0.00, 0.87, 1.00, 0.51 };
    Double_t green[NRGBs] = { 0.00, 0.81, 1.00, 0.20, 0.00 };
    Double_t blue[NRGBs]  = { 0.51, 1.00, 0.12, 0.00, 0.00 };
    TColor::CreateGradientColorTable(NRGBs, stops, red, green, blue, NCont);
    style->SetNumberContours(NCont);

    gROOT->SetStyle("style");

    // Uncomment this line if you want to force all plots loaded from files
    // to use this same style
    gROOT->ForceStyle();
}

// Put a "CHIPS Preliminary" tag in the corner
void Preliminary()
{
    TLatex* prelim = new TLatex(.9, .95, "CHIPS Preliminary");
    prelim->SetTextColor(kBlue);
    prelim->SetNDC();
    prelim->SetTextSize(2/30.);
    prelim->SetTextAlign(32);
    prelim->Draw();
}

// Put a "CHIPS Preliminary" tag on the right
void PreliminarySide()
{
    TLatex* prelim = new TLatex(.93, .9, "CHIPS Preliminary");
    prelim->SetTextColor(kBlue);
    prelim->SetNDC();
    prelim->SetTextSize(2/30.);
    prelim->SetTextAngle(270);
    prelim->SetTextAlign(12);
    prelim->Draw();
}

// Put a "CHIPS Simulation" tag in the corner
void Simulation()
{
    TLatex* prelim = new TLatex(.9, .95, "CHIPS Simulation");
    prelim->SetTextColor(kGray+1);
    prelim->SetNDC();
    prelim->SetTextSize(2/30.);
    prelim->SetTextAlign(32);
    prelim->Draw();
}

// Put a "CHIPS Simulation" tag on the right
void SimulationSide()
{
    TLatex* prelim = new TLatex(.93, .9, "CHIPS Simulation");
    prelim->SetTextColor(kGray+1);
    prelim->SetNDC();
    prelim->SetTextSize(2/30.);
    prelim->SetTextAngle(270);
    prelim->SetTextAlign(12);
    prelim->Draw();
}

// Put a "CHIPS Fake Data" tag in the corner
void FakeData()
{
    TLatex* prelim = new TLatex(.9, .95, "CHIPS Fake Data");
    prelim->SetTextColor(kBlue);
    prelim->SetNDC();
    prelim->SetTextSize(2/30.);
    prelim->SetTextAlign(32);
    prelim->Draw();
}

// Add a label in top left corner
// Especially useful for "Neutrino Beam" and "Antineutrino Beam" labels
void CornerLabel(std::string Str) {
    TLatex* CornLab = new TLatex(.1, .93, Str.c_str());
    CornLab->SetTextColor(kGray+1);
    CornLab->SetNDC();
    CornLab->SetTextSize (2/30.);
    CornLab->SetTextAlign(11);
    CornLab->Draw();
}

void CenterTitles(TH1* histo)
{
    histo->GetXaxis()->CenterTitle();
    histo->GetYaxis()->CenterTitle();
    histo->GetZaxis()->CenterTitle();  
}

// Create a 3d plot
void create_plot_2d(TString name, TH2F *hist, TString title_string,
                    double x_low, double x_high, double y_low, double y_high, double z_low, double z_high,
                    TString draw_opt, bool log_y, bool log_z)
{
    // Define an empty histogram to set global variables
    TH2F *hempty = new TH2F("hempty", title_string, 1, x_low, x_high, 1, y_low, y_high);
    CenterTitles(hempty);

    hempty->GetZaxis()->SetRangeUser(z_low, z_high);
    hempty->GetYaxis()->SetTitleOffset(0.65);

    // Create the canvas and draw all histograms
    TCanvas *canvas = new TCanvas("canvas", "canvas", 1000, 800);
    if(log_y) canvas->SetLogy();
    if(log_z) canvas->SetLogz();
    canvas->cd();
    hempty->Draw();
    hist->Draw(draw_opt);
    canvas->Draw();

    // Save canvas as png and root macro
    canvas->SaveAs(name);

    delete hempty;
    delete canvas;
}

// Create a 2d plot
void create_plot(TString name, int num, TH1F **hists, TString title_string,
                 double x_low, double x_high, double y_low, double y_high,
                 TString leg_draw_opt, TString draw_opt, bool log_y, bool stacked,
                 double with_z=false, double z_low=0, double z_high=0, double log_z=false, TString z_title="")
{
    // Define an empty histogram to set global variables
    TH2F *hempty = new TH2F("hempty", title_string, 1, x_low, x_high, 1, y_low, y_high);
    CenterTitles(hempty);

    if(with_z)
    {
        hempty->GetZaxis()->SetTitle(z_title);
        hempty->GetZaxis()->SetRangeUser(z_low, z_high);
        hempty->GetYaxis()->SetTitleOffset(0.65);
    }

    // Create the legend
    TLegend *legend = new TLegend(0.7, 0.65, 0.85, 0.85);
    legend->SetFillStyle(0);
    for(int i=0; i<num; i++) legend->AddEntry(hists[i], hists[i]->GetTitle(), leg_draw_opt);

    // Create stacked histogram if need be
    THStack *stack = new THStack("stack","");
    for(int i=0; i<num; i++) stack->Add(hists[i]);

    // Create the canvas and draw all histograms
    TCanvas *canvas = new TCanvas("canvas", "canvas", 1000, 800);
    if(log_y) canvas->SetLogy();
    canvas->cd();
    hempty->Draw();
    if(stacked) stack->Draw(draw_opt);
    else for(int i=0; i<num; i++) hists[i]->Draw(draw_opt);
    legend->Draw("same");
    canvas->Draw();

    // Save canvas as png and root macro
    canvas->SaveAs(name);

    delete hempty;
    delete legend;
    delete stack;
    delete canvas;
}

#endif
