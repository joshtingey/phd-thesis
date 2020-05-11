import ROOT
import utils

def digi():
    root_file = ROOT.TFile("data/digi_sk1pe.root")
    raw = root_file.Get("rawDigiPDF")
    pois = root_file.Get("poissonDigiPDF_digiNorm_ln")

    raw.GetZaxis().SetLabelSize(0.3)
    raw.GetZaxis().SetLabelSize(0.03)
    raw.GetZaxis().SetLabelOffset(0)

    utils.create_plot_2d("../diagrams/cvn/digi_method.png", raw, ";Incident Photons; Digitised charge in p.e; ",
                         0, 10, 0, 10, 1e-5, 1e-2 ,"same COLZ", False, True)

    utils.create_plot_2d("../diagrams/cvn/digi_likelihood.png", pois, ";Predicted mean number of photons; Digitised charge in p.e; ",
                         0, 10, 0, 10,  5, 25, "same COLZ", False, False)

    root_file.Close()


if __name__ == "__main__":
    digi()