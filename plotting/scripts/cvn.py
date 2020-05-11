import ROOT
import utils

def cvn():
    root_file = ROOT.TFile("data/cvn_flux_output.root")
    tree = root_file.Get("events")

    utils.tree_hist("../diagrams/cvn/nuEnergy.png", tree, "t_nuEnergy", 
              ";Neutrino Energy (MeV); Fraction of Events", 30, 0, 15000)

    categories = 17
    for i in range(categories):
        true_cat_pred_e_h = ROOT.TH2F("true_cat_pred_e",
            "true_cat_pred_e ;True Energy (MeV); Estimated Energy (MeV)", 40, 0, 10000, 40, 0, 10000)
        pred_cat_pred_e_h = ROOT.TH2F("pred_cat_pred_e",
            "pred_cat_pred_e ;True Energy (MeV); Estimated Energy (MeV)", 40, 0, 10000, 40, 0, 10000)
        
        true_cut = "t_cat=="
        true_cut += i
        tree.Draw("t_nuEnergy:true_cat_pred_e>>true_cat_pred_e", true_cut)
        pred_cut = "classification=="
        pred_cut += i
        tree.Draw("t_nuEnergy:pred_cat_pred_e>>pred_cat_pred_e", pred_cut)

        canvas_true = ROOT.TCanvas(true_cut, true_cut, 1000, 800)
        canvas_true.SetLogz()
        true_cat_pred_e_h.Draw("COLZ")
        canvas_true.Draw()

        true_save = "../diagrams/cvn/energy_estimation/true_cat_"
        true_save += i
        true_save += ".png"
        canvas_true.SaveAs(true_save)

        canvas_pred = ROOT.TCanvas(pred_cut, pred_cut, 1000, 800)
        canvas_pred.SetLogz()
        pred_cat_pred_e_h.Draw("COLZ")
        canvas_pred.Draw()

        pred_save = "../diagrams/cvn/energy_estimation/pred_cat_"
        pred_save += i
        pred_save += ".png"
        canvas_pred.SaveAs(pred_save)

        #true_cat_frac_e_h = ROOT.TH2F("true_cat_frac_e",
        #    "true_cat_frac_e ;True Energy (MeV); Estimated Energy (MeV)", 40, 0, 10000)
        #pred_cat_frac_e_h = ROOT.TH2F("pred_cat_frac_e",
        #    "pred_cat_frac_e ;True Energy (MeV); Estimated Energy (MeV)", 40, 0, 10000)

        cat, classification = 0, 0
        true_e, true_pred_e, pred_pred_e = 0.0, 0.0, 0.0
        t_cat_b = tree.GetBranch("t_cat")
        t_cat_b.SetAddress(cat)
        t_classification_b = tree.GetBranch("t_classification")
        t_classification_b.SetAddress(classification)
        t_nuEnergy_b = tree.GetBranch("t_nuEnergy")
        t_nuEnergy_b.SetAddress(true_e)
        true_e_pred_b = tree.GetBranch("true_cat_pred_e")
        true_e_pred_b.SetAddress(true_pred_e)
        pred_e_pred_b = tree.GetBranch("pred_cat_pred_e")
        pred_e_pred_b.SetAddress(pred_pred_e)
        nevent = tree.GetEntries()

        for i in range(nevent):
            tree.GetEntry(i)

    root_file.Close()


if __name__ == "__main__":
    cvn()