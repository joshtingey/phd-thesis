void event_numbers()
{
    // Open the file and get all the histograms we need
    TFile *flux_file = new TFile("data/flux_chips.root");
    TH1D *nuel_cc_h = (TH1D*)flux_file->Get("enufullfine_nue_allpar_tot_cc_CHIPSoffAXIS");
    TH1D *anuel_cc_h = (TH1D*)flux_file->Get("enufullfine_anue_allpar_tot_cc_CHIPSoffAXIS");
    TH1D *numu_cc_h = (TH1D*)flux_file->Get("enufullfine_numu_allpar_tot_cc_CHIPSoffAXIS");
    TH1D *anumu_cc_h = (TH1D*)flux_file->Get("enufullfine_anumu_allpar_tot_cc_CHIPSoffAXIS");
    TH1D *nuel_nc_h = (TH1D*)flux_file->Get("enufullfine_nue_allpar_tot_nc_CHIPSoffAXIS");
    TH1D *anuel_nc_h = (TH1D*)flux_file->Get("enufullfine_anue_allpar_tot_nc_CHIPSoffAXIS");
    TH1D *numu_nc_h = (TH1D*)flux_file->Get("enufullfine_numu_allpar_tot_nc_CHIPSoffAXIS");
    TH1D *anumu_nc_h = (TH1D*)flux_file->Get("enufullfine_anumu_allpar_tot_nc_CHIPSoffAXIS");

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

    std::cout << "###########################################################" << std::endl;
    std::cout << "Events/6*10^20 POT/kt in the range [0," << max << "]...\n" << std::endl;
    std::cout << "nuel_cc: " << nuel_cc << ", frac: " << (nuel_cc/total) << std::endl;
    std::cout << "anuel_cc: " << anuel_cc << ", frac: " << (anuel_cc/total) << std::endl;
    std::cout << "numu_cc: " << numu_cc << ", frac: " << (numu_cc/total) << std::endl;
    std::cout << "anumu_cc: " << anumu_cc << ", frac: " << (anumu_cc/total) << std::endl;
    std::cout << "nuel_nc: " << nuel_nc << ", frac: " << (nuel_nc/total) << std::endl;
    std::cout << "anuel_nc: " << anuel_nc << ", frac: " << (anuel_nc/total) << std::endl;
    std::cout << "numu_nc: " << numu_nc << ", frac: " << (numu_nc/total) << std::endl;
    std::cout << "anumu_nc: " << anumu_nc << ", frac: " << (anumu_nc/total) << std::endl;

    std::cout << "\nnuel_tot: " << nuel_tot << ", frac: " << (nuel_tot/total) << std::endl;
    std::cout << "anuel_tot: " << anuel_tot << ", frac: " << (anuel_tot/total) << std::endl;
    std::cout << "numu_tot: " << numu_tot << ", frac: " << (numu_tot/total) << std::endl;
    std::cout << "anumu_tot: " << anumu_tot << ", frac: " << (anumu_tot/total) << std::endl;
    std::cout << "###########################################################" << std::endl;

    ofstream myfile;
    myfile.open("output/weights.txt");
    myfile << (nuel_tot/total) << "\n";
    myfile << (anuel_tot/total) << "\n";
    myfile << (numu_tot/total) << "\n";
    myfile << (anumu_tot/total) << "\n";
    myfile.close();
}

void flux()
{
    // Open the file and get all the histograms we need
    TFile *flux_file = new TFile("data/flux_chips.root");
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
    TH2F *hempty = new TH2F("hempty", ";Neutrino Energy (GeV); Neutrinos/6#times10^{20}POT/kt", 1, 0, 15, 1, 1e2, 1.5e6);
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
    flux_canvas->SaveAs("../diagrams/cvn/flux.png");
    flux_canvas->SaveAs("output/flux.C");

    flux_file->Close();
    event_numbers();
}