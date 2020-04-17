void Partition(TCanvas *C, Int_t Nx, Int_t Ny,
               Float_t lMargin, Float_t rMargin, Float_t bMargin, Float_t tMargin)
{
    if (!C)
        return;
    // Setup Pad layout:
    Float_t vSpacing = 0.01;
    Float_t vStep = (1. - bMargin - tMargin - (Ny - 1) * vSpacing) / Ny;
    Float_t hSpacing = 0.01;
    Float_t hStep = ((1. - lMargin - rMargin - (Nx - 1) * hSpacing) / Nx)*0.88;
    Float_t vposd, vposu, vmard, vmaru, vfactor;
    Float_t hposl, hposr, hmarl, hmarr, hfactor;
    for (Int_t i = 0; i < Nx; i++)
    {
        if (i == 0)
        {
            hposl = 0.0;
            hposr = lMargin + hStep;
            hfactor = hposr - hposl;
            hmarl = lMargin / hfactor;
            hmarr = 0.0;
        }
        else if (i == Nx - 1)
        {
            hposl = hposr + hSpacing;
            hposr = hposl + hStep + rMargin;
            hfactor = hposr - hposl;
            hmarl = 0.0;
            hmarr = rMargin / (hposr - hposl);
        }
        else
        {
            hposl = hposr + hSpacing;
            hposr = hposl + hStep;
            hfactor = hposr - hposl;
            hmarl = 0.0;
            hmarr = 0.0;
        }
        for (Int_t j = 0; j < Ny; j++)
        {
            if (j == 0)
            {
                vposd = 0.0;
                vposu = bMargin + vStep;
                vfactor = vposu - vposd;
                vmard = bMargin / vfactor;
                vmaru = 0.0;
            }
            else if (j == Ny - 1)
            {
                vposd = vposu + vSpacing;
                vposu = vposd + vStep + tMargin;
                vfactor = vposu - vposd;
                vmard = 0.0;
                vmaru = tMargin / (vposu - vposd);
            }
            else
            {
                vposd = vposu + vSpacing;
                vposu = vposd + vStep;
                vfactor = vposu - vposd;
                vmard = 0.0;
                vmaru = 0.0;
            }
            C->cd(0);
            char name[16];
            sprintf(name, "pad_%i_%i", i, j);
            TPad *pad = (TPad *)gROOT->FindObject(name);
            if (pad)
                delete pad;
            pad = new TPad(name, "", hposl, vposd, hposr, vposu);
            pad->SetLeftMargin(hmarl);
            pad->SetRightMargin(hmarr);
            pad->SetBottomMargin(vmard);
            pad->SetTopMargin(vmaru);
            pad->SetFrameBorderMode(0);
            pad->SetBorderMode(0);
            pad->SetBorderSize(0);
            pad->SetLogz();
            pad->Draw();
        }
    }
}

void profiles()
{
    TFile *el_file = new TFile("data/profile_electrons.root");
    TFile *mu_file = new TFile("data/profile_muons.root");
    TFile *pi_file = new TFile("data/profile_pions.root");
    TFile *pr_file = new TFile("data/profile_protons.root");

    // Get the emission distance plots
    TH1F *el_d = (TH1F *)el_file->Get("fRho");
    TH1F *mu_d = (TH1F *)mu_file->Get("fRho");
    TH1F *pi_d = (TH1F *)pi_file->Get("fRho");
    TH1F *pr_d = (TH1F *)pr_file->Get("fRho");

    // Define an empty histogram to set global variables
    TH2F *hempty = new TH2F("hempty", ";Distance (cm); Fraction of emitted photons", 1, 0, 1400, 1, 0, 0.006);
    hempty->GetYaxis()->SetLabelSize(0.03);
    CenterTitles(hempty);

    // Set the histogram colours
    el_d->SetLineColor(kGreen + 1);
    mu_d->SetLineColor(kRed + 1);
    pi_d->SetLineColor(kBlue + 1);
    pr_d->SetLineColor(kBlack);

    // Create the legend
    TLegend *leg = new TLegend(0.75, 0.55, 0.85, 0.85);
    leg->AddEntry(el_d, "e", "L");
    leg->AddEntry(mu_d, "#mu", "L");
    leg->AddEntry(pi_d, "#pi^{#pm}", "L");
    leg->AddEntry(pr_d, "P", "L");
    leg->SetFillStyle(0);

    // Create the canvas and draw all histograms
    TCanvas *distance_c = new TCanvas("distance_c", "distance_c", 1000, 800);
    distance_c->cd();
    hempty->Draw();
    el_d->Draw("same");
    mu_d->Draw("same");
    pi_d->Draw("same");
    pr_d->Draw("same");
    leg->Draw("same");
    distance_c->Draw();

    // Save canvas as png and root macro
    distance_c->SaveAs("../diagrams/cvn/emission_distance.png");
    //distance_c->SaveAs("output/emission_distance.C");

    gStyle->SetOptLogz(1);

    // Get the normalised emission profiles
    TH2F *el_g = (TH2F *)el_file->Get("fGFine");
    el_g->GetXaxis()->SetTitle("Cosine emission angle");
    el_g->GetYaxis()->SetTitle("Distance (cm)");
    TH2F *mu_g = (TH2F *)mu_file->Get("fGFine");
    mu_g->GetXaxis()->SetTitle("Cosine emission angle");
    mu_g->GetYaxis()->SetTitle("Distance (cm)");
    TH2F *pi_g = (TH2F *)pi_file->Get("fGFine");
    pi_g->GetXaxis()->SetTitle("Cosine emission angle");
    pi_g->GetYaxis()->SetTitle("Distance (cm)");
    TH2F *pr_g = (TH2F *)pr_file->Get("fGFine");
    pr_g->GetXaxis()->SetTitle("Cosine emission angle");
    pr_g->GetYaxis()->SetTitle("Distance (cm)");

    TCanvas *profile_c = new TCanvas("profile_c", "profile_c", 1000, 800);
    profile_c->SetFillStyle(4000);
    // Number of PADS
    const int Nx = 2;
    const int Ny = 2;
    // Margins
    float lMargin = 0.1;
    float rMargin = 0.02;
    float bMargin = 0.1;
    float tMargin = 0.05;
    // Canvas setup
    Partition(profile_c, Nx, Ny, lMargin, rMargin, bMargin, tMargin);

    TPaletteAxis *palette;
    TPad *pad[Nx][Ny];
    for (Int_t i = 0; i < Nx; i++)
    {
        for (Int_t j = 0; j < Ny; j++)
        {
            profile_c->cd(0);
            // Get the pads previously created.
            char pname[16];
            sprintf(pname, "pad_%i_%i", i, j);
            pad[i][j] = (TPad *)gROOT->FindObject(pname);
            gPad->SetLogz();
            pad[i][j]->Draw();
            pad[i][j]->SetFillStyle(4000);
            pad[i][j]->SetFrameFillStyle(4000);
            pad[i][j]->cd();
            // Size factors
            float xFactor = pad[0][0]->GetAbsWNDC() / pad[i][j]->GetAbsWNDC();
            float yFactor = pad[0][0]->GetAbsHNDC() / pad[i][j]->GetAbsHNDC();
            char hname[16];
            sprintf(hname, "h_%i_%i", i, j);
            TH2F *hFrame = (TH2F*)el_g->Clone(hname);
            hFrame->Reset();
            // Format for y axis
            hFrame->GetYaxis()->SetRangeUser(10, 1400);
            hFrame->GetYaxis()->SetLabelFont(43);
            hFrame->GetYaxis()->SetLabelSize(16);
            hFrame->GetYaxis()->SetLabelOffset(0.02);
            hFrame->GetYaxis()->SetTitleFont(43);
            hFrame->GetYaxis()->SetTitleSize(30);
            hFrame->GetYaxis()->SetTitleOffset(2.5);
            hFrame->GetYaxis()->CenterTitle();
            hFrame->GetYaxis()->SetNdivisions(505);
            hFrame->GetYaxis()->SetTickLength(xFactor * 0.04 / yFactor);
            // Format for x axis
            hFrame->GetXaxis()->SetRangeUser(0.3, 1.1);
            hFrame->GetXaxis()->SetLabelFont(43);
            hFrame->GetXaxis()->SetLabelSize(16);
            hFrame->GetXaxis()->SetLabelOffset(0.02);
            hFrame->GetXaxis()->SetTitleFont(43);
            hFrame->GetXaxis()->SetTitleSize(30);
            hFrame->GetXaxis()->SetTitleOffset(2.5);
            hFrame->GetXaxis()->CenterTitle();
            hFrame->GetXaxis()->SetNdivisions(505);
            hFrame->GetXaxis()->SetTickLength(yFactor * 0.06 / xFactor);
            // Format for the z axis
            hFrame->GetZaxis()->SetRangeUser(0, 0.01);


            // Draw the frame and the plot
            hFrame->Draw();
            TLatex* text = new TLatex(.1, .93, "hello");

            if(i==0 && j==0) 
            {
                text->SetTextSize(2.6/30.);
                text->DrawText(0.375, 1200, "charged pion");
                pi_g->Draw("sameCOL");
            }
            if(i==0 && j==1)
            {
                text->SetTextSize(3/30.);
                text->DrawText(0.375, 1200, "electron");
                el_g->Draw("sameCOL");
            }
            if(i==1 && j==0)
            {
                text->SetTextSize(2.6/30.);
                text->DrawText(0.375, 1200, "proton");
                pr_g->Draw("sameCOL");
            }
            if(i==1 && j==1) 
            {
                text->SetTextSize(3/30.);
                text->DrawText(0.375, 1200, "muon");
                mu_g->Draw("sameCOL");
                palette = new TPaletteAxis(0.90,0.1,0.93,0.95, mu_g);
            }

            gPad->Update();
            gPad->RedrawAxis();
            TLine l;
            l.SetLineWidth(3);
            l.DrawLine(gPad->GetUxmin(), gPad->GetUymin(), gPad->GetUxmax(), gPad->GetUymin());
            l.DrawLine(gPad->GetUxmin(), gPad->GetUymin(), gPad->GetUxmin(), gPad->GetUymax());
            l.DrawLine(gPad->GetUxmin(), gPad->GetUymax(), gPad->GetUxmax(), gPad->GetUymax());
            l.DrawLine(gPad->GetUxmax(), gPad->GetUymin(), gPad->GetUxmax(), gPad->GetUymax());

            
        }
    }
    profile_c->cd();
    palette->Draw("same");
    profile_c->SetLogz();
    profile_c->Draw();

    // Save canvas as png and root macro
    profile_c->SaveAs("../diagrams/cvn/emission_profile.png");
    //profile_c->SaveAs("output/emission_profile.C");
}