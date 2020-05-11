#include "TFile.h"
#include "TH2F.h"

R__ADD_INCLUDE_PATH($PLOTTING)
#include "style.C"

using namespace std;

void digi()
{
    TFile *file = new TFile("data/digi_sk1pe.root");
    TH2F *raw = (TH2F*)file->Get("rawDigiPDF");
    TH2F *pois = (TH2F*)file->Get("poissonDigiPDF_digiNorm_ln");

    raw->GetZaxis()->SetLabelSize(0.3);
    raw->GetZaxis()->SetLabelSize(0.03);
    raw->GetZaxis()->SetLabelOffset(0);

    create_plot_2d("../diagrams/cvn/digi_method.png", raw, ";Incident Photons; Digitised charge in p.e; ",
                   0, 10, 0, 10, 1e-5, 1e-2 ,"same COLZ", false, true);

    create_plot_2d("../diagrams/cvn/digi_likelihood.png", pois, ";Predicted mean number of photons; Digitised charge in p.e; ",
                   0, 10, 0, 10,  5, 25, "same COLZ", false, false);

    file->Close();
}