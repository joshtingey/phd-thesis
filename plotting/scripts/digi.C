void digi()
{
    TFile *flux_file = new TFile("data/digi_sk1pe.root");
    TH1D *raw = (TH1D*)flux_file->Get("rawDigiPDF");
    TH1D *pois = (TH1D*)flux_file->Get("poissonDigiPDF_digiNorm_ln");

    // Modify the raw histogram
    raw->GetXaxis()->SetTitle("Incident Photons");
    raw->GetYaxis()->SetTitle("Digitised charge in p.e");
    raw->GetYaxis()->SetTitleOffset(0.65);
    raw->GetZaxis()->SetRangeUser(1e-5, 1e-2);
    raw->GetZaxis()->SetLabelSize(0.03);
    raw->GetZaxis()->SetLabelOffset(0);
    raw->SetTitle("");
    CenterTitles(raw);

    // Create the canvas and draw all histograms
    TCanvas *raw_canvas = new TCanvas("raw_canvas", "raw_canvas", 1000, 800);
    raw_canvas->SetLogz();
    raw_canvas->cd();
    raw->Draw("COLZ");
    raw_canvas->Draw();

    // Save canvas as png and root macro
    raw_canvas->SaveAs("../diagrams/cvn/digi_method.png");
    //raw_canvas->SaveAs("output/digi_method.C");

    // Modify the pois histogram
    pois->GetXaxis()->SetTitle("Predicted mean number of photons");
    pois->GetYaxis()->SetTitle("Digitised charge in p.e");
    pois->GetYaxis()->SetTitleOffset(0.65);
    pois->GetZaxis()->SetRangeUser(5, 25);
    pois->SetTitle("");
    CenterTitles(pois);

    // Create the canvas and draw all histograms
    TCanvas *pois_canvas = new TCanvas("pois_canvas", "pois_canvas", 1000, 800);
    pois_canvas->cd();
    pois->Draw("COLZ");
    pois_canvas->Draw();

    // Save canvas as png and root macro
    pois_canvas->SaveAs("../diagrams/cvn/digi_likelihood.png");
    //pois_canvas->SaveAs("output/digi_likelihood.C");
}