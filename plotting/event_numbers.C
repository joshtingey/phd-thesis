void event_numbers()
{
    // Open the file and get all the histograms we need
    TFile *flux_file = new TFile("data/chips_location_flux.root");
    TH1D *nuel_cc_h = (TH1D*)flux_file->Get("enufullfine_nue_allpar_tot_cc_CHIPSoffAXIS");
    TH1D *anuel_cc_h = (TH1D*)flux_file->Get("enufullfine_anue_allpar_tot_cc_CHIPSoffAXIS");
    TH1D *numu_cc_h = (TH1D*)flux_file->Get("enufullfine_numu_allpar_tot_cc_CHIPSoffAXIS");
    TH1D *anumu_cc_h = (TH1D*)flux_file->Get("enufullfine_anumu_allpar_tot_cc_CHIPSoffAXIS");
    TH1D *nuel_nc_h = (TH1D*)flux_file->Get("enufullfine_nue_allpar_tot_nc_CHIPSoffAXIS");
    TH1D *anuel_nc_h = (TH1D*)flux_file->Get("enufullfine_anue_allpar_tot_nc_CHIPSoffAXIS");
    TH1D *numu_nc_h = (TH1D*)flux_file->Get("enufullfine_numu_allpar_tot_nc_CHIPSoffAXIS");
    TH1D *anumu_nc_h = (TH1D*)flux_file->Get("enufullfine_anumu_allpar_tot_nc_CHIPSoffAXIS");

    double min = 0.0;
    double max = 10.0;
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

    std::cout << "Events/6*10^20 POT/kt in the range [0," << max << "]..." << std::endl;
    std::cout << "nuel_cc: " << nuel_cc << std::endl;
    std::cout << "anuel_cc: " << anuel_cc << std::endl;
    std::cout << "numu_cc: " << numu_cc << std::endl;
    std::cout << "anumu_cc: " << anumu_cc << std::endl;
    std::cout << "nuel_nc: " << nuel_nc << std::endl;
    std::cout << "anuel_nc: " << anuel_nc << std::endl;
    std::cout << "numu_nc: " << numu_nc << std::endl;
    std::cout << "anumu_nc: " << anumu_nc << std::endl;

}