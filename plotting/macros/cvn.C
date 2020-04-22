#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"

R__ADD_INCLUDE_PATH($PLOTTING)
#include "style.C"

using namespace std;

void cvn()
{
    TFile *file = new TFile("data/cvn_output.root");
    TTree *tree = (TTree*)file->Get("events");

    tree_hist("../diagrams/cvn/nuEnergy.png", tree, "t_nuEnergy", 
              ";Neutrino Energy (MeV); Fraction of Events", 30, 0, 15000);

    file->Close();
}