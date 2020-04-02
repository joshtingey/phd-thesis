void genie_plots()
{
    // Open the file and get all the histograms we need
    TFile *flux_file = new TFile("data/chips_location_flux.root");
    TH1D *nue_flux_h = (TH1D*)flux_file->Get("enufullfine_nue_allpar_NoXSec_CHIPSoffAXIS");
    TH1D *anue_flux_h = (TH1D*)flux_file->Get("enufullfine_anue_allpar_NoXSec_CHIPSoffAXIS");
    TH1D *numu_flux_h = (TH1D*)flux_file->Get("enufullfine_numu_allpar_NoXSec_CHIPSoffAXIS");
    TH1D *anumu_flux_h = (TH1D*)flux_file->Get("enufullfine_anumu_allpar_NoXSec_CHIPSoffAXIS");

    // Apply manipulation to the histograms
    double scale = (6*pow(10,20))/(50*pow(10,6));
    nue_flux_h->Scale(scale);
    anue_flux_h->Scale(scale);
    numu_flux_h->Scale(scale);
    anumu_flux_h->Scale(scale);

    // Define an empty histogram to set global variables
    TH2F *hempty = new TH2F("hempty", ";Neutrino Energy (GeV); Neutrinos/6#times10^{20}POT/kt", 1, 0, 10, 1, 1e2, 1.5e6);
    CenterTitles(hempty);

    // Set the histogram colours
    nue_flux_h->SetLineColor(kGreen+1);
    anue_flux_h->SetLineColor(kGreen+2);
    numu_flux_h->SetLineColor(kBlue+1);
    anumu_flux_h->SetLineColor(kBlue+2);

    // Create the legend
    TLegend *leg = new TLegend(0.7, 0.65, 0.85, 0.85);
    leg->AddEntry(numu_flux_h, "#nu_{#mu}", "L");
    leg->AddEntry(anumu_flux_h, "#bar{#nu}_{#mu}", "L");
    leg->AddEntry(nue_flux_h, "#nu_{e}", "L");
    leg->AddEntry(anue_flux_h, "#bar{#nu}_{e}", "L");
    leg->SetFillStyle(0);
    
    // Create the canvas and draw all histograms
    TCanvas *flux_canvas = new TCanvas("chips_flux", "chips_flux", 1000, 800);
    flux_canvas->SetLogy();
    flux_canvas->cd();
    hempty->Draw();
    nue_flux_h->Draw("samehist");
    anue_flux_h->Draw("samehist");
    numu_flux_h->Draw("samehist");
    anumu_flux_h->Draw("samehist");
    leg->Draw("same");
    flux_canvas->Draw();

    // Save canvas as png and root macro
    flux_canvas->SaveAs("../diagrams/cvn/chips_flux.png");
    flux_canvas->SaveAs("output/chips_flux.C");
}