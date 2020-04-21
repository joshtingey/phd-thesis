void events()
{
    double nuel_weight = 0.0;
    double anuel_weight = 0.0;
    double numu_weight = 0.0;
    double anumu_weight = 0.0;
    double total = 0.0;

    ifstream myfile;
    myfile.open("output/weights.txt");
    myfile >> nuel_weight;
    myfile >> anuel_weight;
    myfile >> numu_weight;
    myfile >> anumu_weight;
    myfile >> total;
    myfile.close();

    std::cout << "nuel weight: " << nuel_weight << std::endl;
    std::cout << "anuel weight: " << anuel_weight << std::endl;
    std::cout << "numu weight: " << numu_weight << std::endl;
    std::cout << "anumu weight: " << anumu_weight << std::endl;

    TFile *nuel_file = new TFile("data/events_nuel.root");
    TFile *anuel_file = new TFile("data/events_anuel.root");
    TFile *numu_file = new TFile("data/events_numu.root");
    TFile *anumu_file = new TFile("data/events_anumu.root");

    THStack *int_type = new THStack("int_type","");
    TH1F *nuel_int_type = (TH1F*)nuel_file->Get("h_intType");
    nuel_int_type->Sumw2();
    nuel_int_type->SetFillColor(kGreen+1);
    //nuel_int_type->Scale(nuel_weight);
    TH1F *anuel_int_type = (TH1F*)anuel_file->Get("h_intType");
    anuel_int_type->Sumw2();
    anuel_int_type->SetFillColor(kGreen+2);
    //anuel_int_type->Scale(anuel_weight);
    TH1F *numu_int_type = (TH1F*)numu_file->Get("h_intType");
    numu_int_type->Sumw2();
    numu_int_type->SetFillColor(kBlue+1);
    //numu_int_type->Scale(numu_weight);
    TH1F *anumu_int_type = (TH1F*)anumu_file->Get("h_intType");
    anumu_int_type->Sumw2();
    anumu_int_type->SetFillColor(kBlue+2);
    //anumu_int_type->Scale(anumu_weight);

    double nuel_entries = nuel_int_type->GetEntries();
    double anuel_entries = anuel_int_type->GetEntries();
    double numu_entries = numu_int_type->GetEntries();
    double anumu_entries = anumu_int_type->GetEntries();
    std::cout << nuel_entries << "-" << anuel_entries << "-" << numu_entries << "-" << anumu_entries << std::endl;
    double entries_total = (nuel_weight*nuel_entries) + (anuel_weight*anuel_entries) + (numu_weight*numu_entries) + (anumu_weight*anumu_entries);
    double event_scale = total/entries_total;
    std::cout << "Entries total: " << entries_total << ", total: " << total << ", Scale: " << event_scale << std::endl;

    int_type->Add(numu_int_type);
    int_type->Add(anumu_int_type);
    int_type->Add(nuel_int_type);
    int_type->Add(anuel_int_type);

    TCanvas *int_canvas = new TCanvas("int_canvas", "int_canvas", 1000, 800);
    int_type->Draw("HIST"); 
    int_canvas->Draw();

    // Save canvas as png and root macro
    int_canvas->SaveAs("../diagrams/cvn/events.png");
    //int_canvas->SaveAs("output/events.C");

    // Can't really do anymore until the disks are back and I can run filtering again for fix bugs
    // - None of the anti energy distributions shows
    // - I can definitely remove some of the categories we don't see
    // - Can I combine nu and anti-nu res categories together?
    // - Check anti particles are treated exactly the same
    // - Add a combined final state plot across all categories like the int type one

    TString name = "h_nuEnergy_";
    TH1F *numu_ccqel_e = (TH1F*)numu_file->Get(name + "CCQE");
    numu_ccqel_e->SetTitle("CCQE");
    TH1F *numu_ccmec_e = (TH1F*)numu_file->Get(name + "kCCMEC");
    numu_ccmec_e->SetTitle("CCMEC");
    TH1F *numu_onepi_e = (TH1F*)numu_file->Get(name + "CCNuPtoLPPiPlus");
    numu_onepi_e->Add((TH1F*)numu_file->Get(name + "CCNuNtoLPPiZero"));
    numu_onepi_e->Add((TH1F*)numu_file->Get(name + "CCNuNtoLNPiPlus"));
    numu_onepi_e->SetTitle("CC1#pi");
    TH1F *numu_cccoh_e = (TH1F*)numu_file->Get(name + "CCCoh");
    numu_cccoh_e->SetTitle("CCCoh");
    TH1F *numu_ccdis_e = (TH1F*)numu_file->Get(name + "CCDIS");
    numu_ccdis_e->SetTitle("CCDIS");
    TH1F *numu_ccother_e = (TH1F*)numu_file->Get(name + "kOtherResonant");
    numu_ccother_e->SetTitle("CCother");
    TH1F *numu_nc_e = (TH1F*)numu_file->Get(name + "NCQE");
    numu_nc_e->Add((TH1F*)numu_file->Get(name + "NCNuPtoNuPPiZero"));
    numu_nc_e->Add((TH1F*)numu_file->Get(name + "NCNuPtoNuNPiPlus"));
    numu_nc_e->Add((TH1F*)numu_file->Get(name + "NCNuNtoNuNPiZero"));
    numu_nc_e->Add((TH1F*)numu_file->Get(name + "NCNuNtoNuPPiMinus"));
    numu_nc_e->Add((TH1F*)numu_file->Get(name + "kNCMEC"));
    numu_nc_e->Add((TH1F*)numu_file->Get(name + "NCDIS"));
    numu_nc_e->Add((TH1F*)numu_file->Get(name + "NCCoh"));
    numu_nc_e->SetTitle("NC");

    TString int_names[27] = {
        "CCQE", "NCQE",
        "CCNuPtoLPPiPlus", "CCNuNtoLPPiZero", "CCNuNtoLNPiPlus", 
        "NCNuPtoNuPPiZero", "NCNuPtoNuNPiPlus", "NCNuNtoNuNPiZero", "NCNuNtoNuPPiMinus", 
        "kCCNuBarNtoLNPiMinus", "kCCNuBarPtoLNPiZero", "kCCNuBarPtoLPPiMinus",
        "kNCNuBarPtoNuBarPPiZero", "kNCNuBarPtoNuBarNPiPlus", "kNCNuBarNtoNuBarNPiZero", "kNCNuBarNtoNuBarPPiMinus",
        "kOtherResonant", "kCCMEC", "kNCMEC", "kIMD",
        "CCDIS", "NCDIS", "NCCoh", "CCCoh", "ElasticScattering", "InverseMuDecay",
        "CosmicMuon"
    };

    TH1F *anumu_e = (TH1F*)anumu_file->Get("h_nuEnergy_Other");
    anumu_e->SetTitle("#bar{#nu}_{#mu}");
    TH1F *nuel_e = (TH1F*)nuel_file->Get("h_nuEnergy_Other");
    nuel_e->SetTitle("#nu_{e}");
    TH1F *anuel_e = (TH1F*)anuel_file->Get("h_nuEnergy_Other");
    anuel_e->SetTitle("#bar{#nu}_{e}");

    for(int i=0; i<27; i++)
    {
        TString name = "h_nuEnergy_";
        name += int_names[i];
        anumu_e->Add((TH1F*)anumu_file->Get(name));
        nuel_e->Add((TH1F*)nuel_file->Get(name));
        anuel_e->Add((TH1F*)anuel_file->Get(name));
    }


    numu_ccqel_e->Rebin(2);
    numu_ccmec_e->Rebin(2);
    numu_onepi_e->Rebin(2);
    numu_cccoh_e->Rebin(2);
    numu_ccdis_e->Rebin(2);
    numu_ccother_e->Rebin(2);
    numu_nc_e->Rebin(2);
    anumu_e->Rebin(2);
    nuel_e->Rebin(2);
    anuel_e->Rebin(2);

    numu_ccqel_e->SetFillColor(2);
    numu_ccmec_e->SetFillColor(3);
    numu_onepi_e->SetFillColor(4);
    numu_cccoh_e->SetFillColor(5);
    numu_ccdis_e->SetFillColor(6);
    numu_ccother_e->SetFillColor(7);
    numu_nc_e->SetFillColor(8);
    anumu_e->SetFillColor(9);
    nuel_e->SetFillColor(10);
    anuel_e->SetFillColor(11);

    numu_ccqel_e->Scale(numu_weight);
    numu_ccmec_e->Scale(numu_weight);
    numu_onepi_e->Scale(numu_weight);
    numu_cccoh_e->Scale(numu_weight);
    numu_ccdis_e->Scale(numu_weight);
    numu_ccother_e->Scale(numu_weight);
    numu_nc_e->Scale(numu_weight);
    anumu_e->Scale(anumu_weight);
    nuel_e->Scale(nuel_weight);
    anuel_e->Scale(anuel_weight);

    numu_ccqel_e->Scale(event_scale);
    numu_ccmec_e->Scale(event_scale);
    numu_onepi_e->Scale(event_scale);
    numu_cccoh_e->Scale(event_scale);
    numu_ccdis_e->Scale(event_scale);
    numu_ccother_e->Scale(event_scale);
    numu_nc_e->Scale(event_scale);
    anumu_e->Scale(event_scale);
    nuel_e->Scale(event_scale);
    anuel_e->Scale(event_scale);

    //numu_ccqel_e->SetFillStyle(3004);
    //numu_ccmec_e->SetFillStyle(3007);
    //numu_onepi_e->SetFillStyle(3005);
    //numu_cccoh_e->SetFillStyle(3005);
    //numu_ccdis_e->SetFillStyle(3013);
    //numu_ccother_e->SetFillStyle(3002);
    //numu_nc_e->SetFillStyle(3015);
    //anumu_e->SetFillStyle(3015);
    //nuel_e->SetFillStyle(3015);
    //anuel_e->SetFillStyle(3015);

    TLegend *leg = new TLegend(0.65, 0.40, 0.85, 0.85);
    leg->SetFillStyle(0);
    leg->AddEntry(numu_ccqel_e, numu_ccqel_e->GetTitle(), "FB");
    leg->AddEntry(numu_ccmec_e, numu_ccmec_e->GetTitle(), "FB");
    leg->AddEntry(numu_onepi_e, numu_onepi_e->GetTitle(), "FB");
    leg->AddEntry(numu_cccoh_e, numu_cccoh_e->GetTitle(), "FB");
    leg->AddEntry(numu_ccdis_e, numu_ccdis_e->GetTitle(), "FB");
    leg->AddEntry(numu_ccother_e, numu_ccother_e->GetTitle(), "FB");
    leg->AddEntry(numu_nc_e, numu_nc_e->GetTitle(), "FB");
    leg->AddEntry(anumu_e, anumu_e->GetTitle(), "FB");
    leg->AddEntry(nuel_e, nuel_e->GetTitle(), "FB");
    leg->AddEntry(anuel_e, anuel_e->GetTitle(), "FB");
    
    THStack *es = new THStack("es","");
    es->Add(numu_ccqel_e);
    es->Add(numu_ccmec_e);
    es->Add(numu_onepi_e);
    es->Add(numu_cccoh_e);
    es->Add(numu_ccdis_e);
    es->Add(numu_ccother_e);
    es->Add(numu_nc_e);
    es->Add(anumu_e);
    es->Add(nuel_e);
    es->Add(anuel_e);
    
    TCanvas *es_canvas = new TCanvas("es_canvas", "es_canvas", 1000, 800);
    es->Draw("PFC HIST");
    leg->Draw("same");
    es->GetXaxis()->SetTitle("Neutrino Energy (MeV)");
    es->GetYaxis()->SetTitle("Number of Events/6#times10^{20}POT/kt");
    es->GetXaxis()->CenterTitle();
    es->GetYaxis()->CenterTitle();
    es->GetXaxis()->SetRangeUser(0, 10000);
    es_canvas->Modified();
    es_canvas->Draw();

    // Save canvas as png and root macro
    es_canvas->SaveAs("../diagrams/cvn/events_energies.png");
    //int_canvas->SaveAs("output/events_energies.C");

    /*
    const int num_types = 28;
    TString int_names[num_types] = {
        "Other", "CCQE", "NCQE",
        "CCNuPtoLPPiPlus", "CCNuNtoLPPiZero", "CCNuNtoLNPiPlus", 
        "NCNuPtoNuPPiZero", "NCNuPtoNuNPiPlus", "NCNuNtoNuNPiZero", "NCNuNtoNuPPiMinus", 
        "kCCNuBarNtoLNPiMinus", "kCCNuBarPtoLNPiZero", "kCCNuBarPtoLPPiMinus",
        "kNCNuBarPtoNuBarPPiZero", "kNCNuBarPtoNuBarNPiPlus", "kNCNuBarNtoNuBarNPiZero", "kNCNuBarNtoNuBarPPiMinus",
        "kOtherResonant", "kCCMEC", "kNCMEC", "kIMD",
        "CCDIS", "NCDIS", "NCCoh", "CCCoh", "ElasticScattering", "InverseMuDecay",
        "CosmicMuon"
    };

    int int_colours[num_types] = {
        kBlack, kGreen, kRed,
        kGreen+1, kGreen+2, kGreen+3,
        kRed+1, kRed+2, kRed+3, kRed+4,
        kGreen+1, kGreen+2, kGreen+3,
        kRed+1, kRed+2, kRed+3, kRed+4,
        kYellow, kBlue, kBlue+1, kYellow,
        kBlue+2, kBlue+3, kBlue+4, kBlue+5, kYellow, kYellow,
        kYellow
    };

    int int_styles[num_types] = {
        3001, 3004, 3001,
        3005, 3005, 3005,
        3006, 3006, 3006, 3006,
        3005, 3005, 3005,
        3006, 3006, 3006, 3006,
        3001, 3013, 3001, 3001,
        3007, 3008, 3009, 3010, 3001, 3001,
        3001
    };

    TLegend *leg = new TLegend(0.6, 0.30, 0.85, 0.85);
    leg->SetFillStyle(0);
    THStack *energy_stacked = new THStack("energy_stacked","");
    TH1F *energy_hists[num_types];
    for(int i=0; i<num_types; i++)
    {
        TString name = "h_nuEnergy_";
        name += int_names[i];
        energy_hists[i] = (TH1F*)numu_file->Get(name);
        energy_hists[i]->Rebin(2);
        if(energy_hists[i]->GetEntries() > 5000)
        {
            energy_hists[i]->SetFillColor(int_colours[i]);
            energy_hists[i]->SetFillStyle(int_styles[i]);
            energy_stacked->Add(energy_hists[i]);
            leg->AddEntry(energy_hists[i], int_names[i], "FB");
        } 
    }


    TCanvas *energy_canvas = new TCanvas("energy_canvas", "energy_canvas", 1000, 800);
    energy_stacked->Draw("PFC");
    leg->Draw("same");
    energy_stacked->GetXaxis()->SetTitle("Neutrino Energy (MeV)");
    energy_stacked->GetYaxis()->SetTitle("Number of Events/6#times10^{20}POT/kt");
    energy_stacked->GetXaxis()->CenterTitle();
    energy_stacked->GetYaxis()->CenterTitle();
    energy_stacked->GetXaxis()->SetRangeUser(0, 10000);
    energy_canvas->Modified();
    energy_canvas->Draw();
    */

    //nuel_file->Close();
    //anuel_file->Close();
    //numu_file->Close();
    //anumu_file->Close();
}