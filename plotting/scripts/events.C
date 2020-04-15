void events()
{
    double nuel_weight = 0.0;
    double anuel_weight = 0.0;
    double numu_weight = 0.0;
    double anumu_weight = 0.0;

    ifstream myfile;
    myfile.open("output/weights.txt");
    myfile >> nuel_weight;
    myfile >> anuel_weight;
    myfile >> numu_weight;
    myfile >> anumu_weight;
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

    int_type->Add(numu_int_type);
    int_type->Add(anumu_int_type);
    int_type->Add(nuel_int_type);
    int_type->Add(anuel_int_type);

    TCanvas *int_canvas = new TCanvas("chips_flux", "chips_flux", 1000, 800);
    int_type->Draw("HIST"); 
    int_canvas->Draw();

    nuel_file->Close();
    anuel_file->Close();
    numu_file->Close();
    anumu_file->Close();

    // Can't really do anymore until the disks are back and I can run filtering again for fix bugs
    // - None of the anti energy distributions shows
    // - I can definitely remove some of the categories we don't see
    // - Can I combine nu and anti-nu res categories together?
    // - Check anti particles are treated exactly the same
    // - Add a combined final state plot across all categories like the int type one
}