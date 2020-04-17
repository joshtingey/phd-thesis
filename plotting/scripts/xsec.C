void make_plots(const char * in_file, const char * out_name)
{
    // Open the file and get all the graphs we need
    TFile *cs_file = new TFile(in_file);

    TString tot_cc_s = out_name; tot_cc_s += "/tot_cc";
    TString coh_cc_s = out_name; coh_cc_s += "/coh_cc";
    TString qel_cc_p_s = out_name; qel_cc_p_s += "/qel_cc_p";
    TString qel_cc_n_s = out_name; qel_cc_n_s += "/qel_cc_n";
    TString dis_cc_p_s = out_name; dis_cc_p_s += "/dis_cc_p";
    TString dis_cc_n_s = out_name; dis_cc_n_s += "/dis_cc_n";
    TString res_cc_p_s = out_name; res_cc_p_s += "/res_cc_p";
    TString res_cc_n_s = out_name; res_cc_n_s += "/res_cc_n";

    TString tot_nc_s = out_name; tot_nc_s += "/tot_nc";
    TString coh_nc_s = out_name; coh_nc_s += "/coh_nc";
    TString qel_nc_p_s = out_name; qel_nc_p_s += "/qel_nc_p";
    TString qel_nc_n_s = out_name; qel_nc_n_s += "/qel_nc_n";
    TString dis_nc_p_s = out_name; dis_nc_p_s += "/dis_nc_p";
    TString dis_nc_n_s = out_name; dis_nc_n_s += "/dis_nc_n";
    TString res_nc_p_s = out_name; res_nc_p_s += "/res_nc_p";
    TString res_nc_n_s = out_name; res_nc_n_s += "/res_nc_n";

    TGraph *tot_cc_g = (TGraph*)cs_file->Get(tot_cc_s);
    TGraph *coh_cc_g = (TGraph*)cs_file->Get(coh_cc_s);
    TGraph *qel_cc_g = (TGraph*)cs_file->Get(qel_cc_p_s);
    if(qel_cc_g == NULL) {
        qel_cc_g = (TGraph*)cs_file->Get(qel_cc_n_s);
    }
    TGraph *dis_cc_p_g = (TGraph*)cs_file->Get(dis_cc_p_s);
    TGraph *dis_cc_n_g = (TGraph*)cs_file->Get(dis_cc_n_s);
    TGraph *res_cc_p_g = (TGraph*)cs_file->Get(res_cc_p_s);
    TGraph *res_cc_n_g = (TGraph*)cs_file->Get(res_cc_n_s);

    TGraph *tot_nc_g = (TGraph*)cs_file->Get(tot_nc_s);
    TGraph *coh_nc_g = (TGraph*)cs_file->Get(coh_nc_s);
    TGraph *qel_nc_p_g = (TGraph*)cs_file->Get(qel_nc_p_s);
    TGraph *qel_nc_n_g = (TGraph*)cs_file->Get(qel_nc_n_s);
    TGraph *dis_nc_p_g = (TGraph*)cs_file->Get(dis_nc_p_s);
    TGraph *dis_nc_n_g = (TGraph*)cs_file->Get(dis_nc_n_s);
    TGraph *res_nc_p_g = (TGraph*)cs_file->Get(res_nc_p_s);
    TGraph *res_nc_n_g = (TGraph*)cs_file->Get(res_nc_n_s);

    // Apply manipulation to the graphs
    TF2 *func = new TF2("func","y*(1/x)");
    tot_cc_g->Apply(func);
    coh_cc_g->Apply(func);
    qel_cc_g->Apply(func);
    dis_cc_p_g->Apply(func);
    dis_cc_n_g->Apply(func);
    res_cc_p_g->Apply(func);
    res_cc_n_g->Apply(func);
    tot_nc_g->Apply(func);
    coh_nc_g->Apply(func);
    qel_nc_p_g->Apply(func);
    qel_nc_n_g->Apply(func);
    dis_nc_p_g->Apply(func);
    dis_nc_n_g->Apply(func);
    res_nc_p_g->Apply(func);
    res_nc_n_g->Apply(func);

    int size = tot_cc_g->GetN();
    double x[size];
    double dis_cc[size];
    double res_cc[size];
    double dis_nc[size];
    double qel_nc[size];
    double res_nc[size];
    for(int i=0; i<size; ++i) 
    {
        double x_bin = 0.0;
        double dis_cc_p, res_cc_p, dis_nc_p, qel_nc_p, res_nc_p = 0.0;
        double dis_cc_n, res_cc_n, dis_nc_n, qel_nc_n, res_nc_n = 0.0;
        dis_cc_p_g->GetPoint(i, x_bin, dis_cc_p);
        dis_cc_n_g->GetPoint(i, x_bin, dis_cc_n);
        res_cc_p_g->GetPoint(i, x_bin, res_cc_p);
        res_cc_n_g->GetPoint(i, x_bin, res_cc_n);
        dis_nc_p_g->GetPoint(i, x_bin, dis_nc_p);
        dis_nc_n_g->GetPoint(i, x_bin, dis_nc_n);
        qel_nc_p_g->GetPoint(i, x_bin, qel_nc_p);
        qel_nc_n_g->GetPoint(i, x_bin, qel_nc_n);
        res_nc_p_g->GetPoint(i, x_bin, res_nc_p);
        res_nc_n_g->GetPoint(i, x_bin, res_nc_n);

        x[i] = x_bin;
        dis_cc[i] = dis_cc_p + dis_cc_n;
        res_cc[i] = res_cc_p + res_cc_n;
        dis_nc[i] = dis_nc_p + dis_nc_n;
        qel_nc[i] = qel_nc_p + qel_nc_n;
        res_nc[i] = res_nc_p + res_nc_n;
    }

    TGraph *dis_cc_g = new TGraph(size, x, dis_cc); dis_cc_g->SetLineWidth(3);
    TGraph *res_cc_g = new TGraph(size, x, res_cc); res_cc_g->SetLineWidth(3);
    TGraph *dis_nc_g = new TGraph(size, x, dis_nc); dis_nc_g->SetLineWidth(3);
    TGraph *qel_nc_g = new TGraph(size, x, qel_nc); qel_nc_g->SetLineWidth(3);
    TGraph *res_nc_g = new TGraph(size, x, res_nc); res_nc_g->SetLineWidth(3);

    // Define an empty histogram to set global variables
    TH2F *hempty = new TH2F("hempty", ";Neutrino Energy (GeV); O^{16} #nu cross section/E_{#nu} (10^{-38} cm^{2} / GeV)", 1, 0, 15, 1, 1e-2, 20);
    CenterTitles(hempty);
    hempty->GetYaxis()->SetTitleOffset(0.8);

    // Set the graph colours
    tot_cc_g->SetLineColor(kBlack);
    qel_cc_g->SetLineColor(kBlue+1);
    res_cc_g->SetLineColor(kRed+1);
    dis_cc_g->SetLineColor(kGreen+1);
    coh_cc_g->SetLineColor(kYellow+1);

    tot_nc_g->SetLineColor(kBlack);
    qel_nc_g->SetLineColor(kBlue+1);
    res_nc_g->SetLineColor(kRed+1);
    dis_nc_g->SetLineColor(kGreen+1);
    coh_nc_g->SetLineColor(kYellow+1);

    // Create the legends
    TLegend *leg_cc = new TLegend(0.7, 0.22, 0.85, 0.42);
    leg_cc->AddEntry(tot_cc_g, "Total CC", "L");
    leg_cc->AddEntry(qel_cc_g, "CC QEL", "L");
    leg_cc->AddEntry(res_cc_g, "CC RES", "L");
    leg_cc->AddEntry(dis_cc_g, "CC DIS", "L");
    leg_cc->AddEntry(coh_cc_g, "CC COH", "L");
    leg_cc->SetFillStyle(0);
    
    TLegend *leg_nc = new TLegend(0.7, 0.22, 0.85, 0.42);
    leg_nc->AddEntry(tot_nc_g, "Total NC", "L");
    leg_nc->AddEntry(qel_nc_g, "NC QEL", "L");
    leg_nc->AddEntry(res_nc_g, "NC RES", "L");
    leg_nc->AddEntry(dis_nc_g, "NC DIS", "L");
    leg_nc->AddEntry(coh_nc_g, "NC COH", "L");
    leg_nc->SetFillStyle(0);

    // Create box showing CHIPS energy range [2,5] GeV
    TLine *low_line = new TLine(2, 0, 2, 20);
    low_line->SetLineWidth(3);
    low_line->SetLineColor(14);
    TBox *chips_box = new TBox(2, 0, 5, 20);
    chips_box->SetFillColor(14);
    chips_box->SetFillStyle(3345);
    TLine *high_line = new TLine(5, 0, 5, 20);
    high_line->SetLineWidth(3);
    high_line->SetLineColor(14);

    // Create the canvases and draw all graphs
    TCanvas *cs_canvas_cc = new TCanvas("genie_cross_sections_cc", "genie_cross_sections_cc", 1000, 800);
    cs_canvas_cc->SetLogy();
    cs_canvas_cc->cd();
    hempty->Draw();
    tot_cc_g->Draw("same");
    coh_cc_g->Draw("same");
    dis_cc_g->Draw("same");
    qel_cc_g->Draw("same");
    res_cc_g->Draw("same");
    leg_cc->Draw("same");
    low_line->Draw("same");
    chips_box->Draw("same");
    high_line->Draw("same");
    cs_canvas_cc->Draw();

    TCanvas *cs_canvas_nc = new TCanvas("genie_cross_sections_nc", "genie_cross_sections_nc", 1000, 800);
    cs_canvas_nc->SetLogy();
    cs_canvas_nc->cd();
    hempty->Draw();
    tot_nc_g->Draw("same");
    coh_nc_g->Draw("same");
    dis_nc_g->Draw("same");
    qel_nc_g->Draw("same");
    res_nc_g->Draw("same");
    leg_nc->Draw("same");
    low_line->Draw("same");
    chips_box->Draw("same");
    high_line->Draw("same");
    cs_canvas_nc->Draw();

    TString png_cc = "../diagrams/cvn/xsec_cc_";
    png_cc += out_name;
    png_cc += ".png";
    TString macro_cc = "./output/xsec_cc_";
    macro_cc += out_name;
    macro_cc += ".C";

    TString png_nc = "../diagrams/cvn/xsec_nc_";
    png_nc += out_name;
    png_nc += ".png";
    TString macro_nc = "./output/xsec_nc_";
    macro_nc += out_name;
    macro_nc += ".C";


    // Save canvas as png and root macro
    cs_canvas_cc->SaveAs(png_cc);
    //cs_canvas_cc->SaveAs(macro_cc);
    cs_canvas_nc->SaveAs(png_nc);
    //cs_canvas_nc->SaveAs(macro_nc);
}

void xsec()
{
    make_plots("data/xsec_nuel.root", "nu_e_O16");
    make_plots("data/xsec_anuel.root", "nu_e_bar_O16");
    make_plots("data/xsec_numu.root", "nu_mu_O16");
    make_plots("data/xsec_anumu.root", "nu_mu_bar_O16");
}