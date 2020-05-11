#include <iostream>
#include <fstream>
#include "TFile.h"
#include "TH1F.h"

R__ADD_INCLUDE_PATH($PLOTTING)
#include "style.C"

using namespace std;

void event_numbers()
{
    // Open the file and get all the histograms we need
    TFile *file = new TFile("./data/flux_chips.root");
    TH1F *nuel_cc_h = (TH1F*)file->Get("enufullfine_nue_allpar_tot_cc_CHIPSoffAXIS");
    TH1F *anuel_cc_h = (TH1F*)file->Get("enufullfine_anue_allpar_tot_cc_CHIPSoffAXIS");
    TH1F *numu_cc_h = (TH1F*)file->Get("enufullfine_numu_allpar_tot_cc_CHIPSoffAXIS");
    TH1F *anumu_cc_h = (TH1F*)file->Get("enufullfine_anumu_allpar_tot_cc_CHIPSoffAXIS");
    TH1F *nuel_nc_h = (TH1F*)file->Get("enufullfine_nue_allpar_tot_nc_CHIPSoffAXIS");
    TH1F *anuel_nc_h = (TH1F*)file->Get("enufullfine_anue_allpar_tot_nc_CHIPSoffAXIS");
    TH1F *numu_nc_h = (TH1F*)file->Get("enufullfine_numu_allpar_tot_nc_CHIPSoffAXIS");
    TH1F *anumu_nc_h = (TH1F*)file->Get("enufullfine_anumu_allpar_tot_nc_CHIPSoffAXIS");

    double min = 0.0;
    double max = 15.0;
    double nuel_cc = nuel_cc_h->Integral(nuel_cc_h->FindFixBin(min), nuel_cc_h->FindFixBin(max), "");
    double anuel_cc = anuel_cc_h->Integral(anuel_cc_h->FindFixBin(min), anuel_cc_h->FindFixBin(max), "");
    double numu_cc = numu_cc_h->Integral(numu_cc_h->FindFixBin(min), numu_cc_h->FindFixBin(max), "");
    double anumu_cc = anumu_cc_h->Integral(anumu_cc_h->FindFixBin(min), anumu_cc_h->FindFixBin(max), "");
    double nuel_nc = nuel_nc_h->Integral(nuel_nc_h->FindFixBin(min), nuel_nc_h->FindFixBin(max), "");
    double anuel_nc = anuel_nc_h->Integral(anuel_nc_h->FindFixBin(min), anuel_nc_h->FindFixBin(max), "");
    double numu_nc = numu_nc_h->Integral(numu_nc_h->FindFixBin(min), numu_nc_h->FindFixBin(max), "");
    double anumu_nc = anumu_nc_h->Integral(anumu_nc_h->FindFixBin(min), anumu_nc_h->FindFixBin(max), "");

    double scale = (6*pow(10,20))/(50*pow(10,6));
    nuel_cc = nuel_cc * scale;
    anuel_cc = anuel_cc * scale;
    numu_cc = numu_cc * scale;
    anumu_cc = anumu_cc * scale;
    nuel_nc = nuel_nc * scale;
    anuel_nc = anuel_nc * scale;
    numu_nc = numu_nc * scale;
    anumu_nc = anumu_nc * scale;
    double total = nuel_cc + anuel_cc + numu_cc + anumu_cc + nuel_nc + anuel_nc + numu_nc + anumu_nc;

    double nuel_tot = nuel_cc + nuel_nc;
    double anuel_tot = anuel_cc + anuel_nc;
    double numu_tot = numu_cc + numu_nc;
    double anumu_tot = anumu_cc + anumu_nc;

    cout << "###########################################################" << endl;
    cout << "Events/6*10^20 POT/kt in the range [0," << max << "]...\n" << endl;
    cout << "nuel_cc: " << nuel_cc << ", frac: " << (nuel_cc/total) << endl;
    cout << "anuel_cc: " << anuel_cc << ", frac: " << (anuel_cc/total) << endl;
    cout << "numu_cc: " << numu_cc << ", frac: " << (numu_cc/total) << endl;
    cout << "anumu_cc: " << anumu_cc << ", frac: " << (anumu_cc/total) << endl;
    cout << "nuel_nc: " << nuel_nc << ", frac: " << (nuel_nc/total) << endl;
    cout << "anuel_nc: " << anuel_nc << ", frac: " << (anuel_nc/total) << endl;
    cout << "numu_nc: " << numu_nc << ", frac: " << (numu_nc/total) << endl;
    cout << "anumu_nc: " << anumu_nc << ", frac: " << (anumu_nc/total) << endl;
    cout << "Total:" << total << endl;

    cout << "\nnuel_tot: " << nuel_tot << ", frac: " << (nuel_tot/total) << endl;
    cout << "anuel_tot: " << anuel_tot << ", frac: " << (anuel_tot/total) << endl;
    cout << "numu_tot: " << numu_tot << ", frac: " << (numu_tot/total) << endl;
    cout << "anumu_tot: " << anumu_tot << ", frac: " << (anumu_tot/total) << endl;
    cout << "###########################################################" << endl;

    ofstream myfile;
    myfile.open("output/weights.txt");
    myfile << (nuel_tot/total) << "\n";
    myfile << (anuel_tot/total) << "\n";
    myfile << (numu_tot/total) << "\n";
    myfile << (anumu_tot/total) << "\n";
    myfile << total << "\n";
    myfile.close();

    file->Close();
}

void flux_plot()
{
    // Open the file and get all the histograms we need
    TFile *file = new TFile("./data/flux_chips.root");
    TH1F *nuel_flux_h = (TH1F*)file->Get("enufullfine_nue_allpar_NoXSec_CHIPSoffAXIS");
    TH1F *anuel_flux_h = (TH1F*)file->Get("enufullfine_anue_allpar_NoXSec_CHIPSoffAXIS");
    TH1F *numu_flux_h = (TH1F*)file->Get("enufullfine_numu_allpar_NoXSec_CHIPSoffAXIS");
    TH1F *anumu_flux_h = (TH1F*)file->Get("enufullfine_anumu_allpar_NoXSec_CHIPSoffAXIS");

    // Apply manipulation to the histograms
    double scale = (6*pow(10,20))/(50*pow(10,6));
    nuel_flux_h->Scale(scale); nuel_flux_h->SetTitle("#nu_{#mu}"); nuel_flux_h->SetLineColor(kGreen+1);
    anuel_flux_h->Scale(scale); anuel_flux_h->SetTitle("#bar{#nu}_{#mu}"); anuel_flux_h->SetLineColor(kGreen+2);
    numu_flux_h->Scale(scale); numu_flux_h->SetTitle("#nu_{e}"); numu_flux_h->SetLineColor(kBlue+1);
    anumu_flux_h->Scale(scale); anumu_flux_h->SetTitle("#bar{#nu}_{e}"); anumu_flux_h->SetLineColor(kBlue+2);
 
    const int num = 4;
    TH1F *hists[num] = {nuel_flux_h, anuel_flux_h, numu_flux_h, anumu_flux_h};
    create_plot("../diagrams/cvn/flux.png", num, hists, ";Neutrino Energy (GeV); #nu/6#times10^{20}POT/kt",
                0, 15, 1e2, 1.5e6, "L", "samehist", true, false);

    file->Close();
}

void flux()
{
    event_numbers();
    flux_plot();
}