#include "TFile.h"
#include "TTree.h"
#include "TH1F.h"
#include "TH2F.h"

R__ADD_INCLUDE_PATH($PLOTTING)
#include "style.C"

using namespace std;

void cvn()
{
    TFile *file = new TFile("data/cvn_flux_output.root");
    TTree *tree = (TTree*)file->Get("events");

    tree_hist("../diagrams/cvn/nuEnergy.png", tree, "t_nuEnergy", 
              ";Neutrino Energy (MeV); Fraction of Events", 30, 0, 15000);

    int categories = 17;
    for(int i=0; i<categories; i++)
    {
        TH2F *true_cat_pred_e_h = new TH2F("true_cat_pred_e",
            "true_cat_pred_e ;True Energy (MeV); Estimated Energy (MeV)", 40, 0, 10000, 40, 0, 10000);
        TH2F *pred_cat_pred_e_h = new TH2F("pred_cat_pred_e",
            "pred_cat_pred_e ;True Energy (MeV); Estimated Energy (MeV)", 40, 0, 10000, 40, 0, 10000);
        
        TString true_cut = "t_cat==";
        true_cut += i;
        tree->Draw("t_nuEnergy:true_cat_pred_e>>true_cat_pred_e", true_cut);
        TString pred_cut = "classification==";
        pred_cut += i;
        tree->Draw("t_nuEnergy:pred_cat_pred_e>>pred_cat_pred_e", pred_cut);

        TCanvas *canvas_true = new TCanvas(true_cut, true_cut, 1000, 800);
        canvas_true->SetLogz();
        true_cat_pred_e_h->Draw("COLZ");
        canvas_true->Draw();

        TString true_save = "../diagrams/cvn/energy_estimation/true_cat_";
        true_save += i;
        true_save += ".png";
        canvas_true->SaveAs(true_save);

        TCanvas *canvas_pred = new TCanvas(pred_cut, pred_cut, 1000, 800);
        canvas_pred->SetLogz();
        pred_cat_pred_e_h->Draw("COLZ");
        canvas_pred->Draw();

        TString pred_save = "../diagrams/cvn/energy_estimation/pred_cat_";
        pred_save += i;
        pred_save += ".png";
        canvas_pred->SaveAs(pred_save);

        //TH1F *true_cat_frac_e_h = new TH2F("true_cat_frac_e",
        //    "true_cat_frac_e ;True Energy (MeV); Estimated Energy (MeV)", 40, 0, 10000);
        //TH1F *pred_cat_frac_e_h = new TH2F("pred_cat_frac_e",
        //    "pred_cat_frac_e ;True Energy (MeV); Estimated Energy (MeV)", 40, 0, 10000);

        int cat = 0, classification = 0;
        double true_e = 0.0, true_pred_e = 0.0, pred_pred_e = 0.0;
        auto t_cat_b = tree->GetBranch("t_cat"); t_cat_b->SetAddress(&cat);
        auto t_classification_b = tree->GetBranch("t_classification"); t_classification_b->SetAddress(&classification);
        auto t_nuEnergy_b = tree->GetBranch("t_nuEnergy"); t_nuEnergy_b->SetAddress(&true_e);
        auto true_e_pred_b = tree->GetBranch("true_cat_pred_e"); true_e_pred_b->SetAddress(&true_pred_e);
        auto pred_e_pred_b = tree->GetBranch("pred_cat_pred_e"); pred_e_pred_b->SetAddress(&pred_pred_e);
        auto nevent = tree->GetEntries();

        
        for (Int_t i=0;i<nevent;i++) 
        {
            tree->GetEntry(i);
            
        }

        delete true_cat_pred_e_h;
        delete pred_cat_pred_e_h;
        delete canvas_true;
        delete canvas_pred;
    }

    file->Close();
}