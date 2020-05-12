from array import array
import ctypes
import ROOT
import utils

def make_plots(in_file, out_name):
    # Open the file and get all the graphs we need
    cs_file = ROOT.TFile(in_file)

    tot_cc_g = cs_file.Get(out_name + '/tot_cc')
    coh_cc_g = cs_file.Get(out_name + '/coh_cc')
    mec_cc_g = cs_file.Get(out_name + '/mec_cc')
    qel_cc_g = cs_file.Get(out_name + '/qel_cc_p')
    if qel_cc_g == None:
        qel_cc_g = cs_file.Get(out_name + '/qel_cc_n')
    dis_cc_p_g = cs_file.Get(out_name + '/dis_cc_p')
    dis_cc_n_g = cs_file.Get(out_name + '/dis_cc_n')
    res_cc_p_g = cs_file.Get(out_name + '/res_cc_p')
    res_cc_n_g = cs_file.Get(out_name + '/res_cc_n')

    tot_nc_g = cs_file.Get(out_name + '/tot_nc')
    coh_nc_g = cs_file.Get(out_name + '/coh_nc')
    mec_nc_g = cs_file.Get(out_name + '/mec_nc')
    qel_nc_p_g = cs_file.Get(out_name + '/qel_nc_p')
    qel_nc_n_g = cs_file.Get(out_name + '/qel_nc_n')
    dis_nc_p_g = cs_file.Get(out_name + '/dis_nc_p')
    dis_nc_n_g = cs_file.Get(out_name + '/dis_nc_n')
    res_nc_p_g = cs_file.Get(out_name + '/res_nc_p')
    res_nc_n_g = cs_file.Get(out_name + '/res_nc_n')

    # Apply 1/E function to the plots
    func = ROOT.TF2('func','y*(1/x)')
    tot_cc_g.Apply(func)
    coh_cc_g.Apply(func)
    mec_cc_g.Apply(func)
    qel_cc_g.Apply(func)
    dis_cc_p_g.Apply(func)
    dis_cc_n_g.Apply(func)
    res_cc_p_g.Apply(func)
    res_cc_n_g.Apply(func)
    tot_nc_g.Apply(func)
    coh_nc_g.Apply(func)
    mec_nc_g.Apply(func)
    qel_nc_p_g.Apply(func)
    qel_nc_n_g.Apply(func)
    dis_nc_p_g.Apply(func)
    dis_nc_n_g.Apply(func)
    res_nc_p_g.Apply(func)
    res_nc_n_g.Apply(func)

    size = tot_cc_g.GetN()
    x = array( 'd' )
    dis_cc = array( 'd' )
    res_cc = array( 'd' )
    dis_nc = array( 'd' )
    qel_nc = array( 'd' )
    res_nc = array( 'd' )
    for i in range(size): 
        x_bin = ctypes.c_double(0)
        dis_cc_p, res_cc_p, dis_nc_p, qel_nc_p, res_nc_p = ctypes.c_double(0), ctypes.c_double(0), ctypes.c_double(0), ctypes.c_double(0), ctypes.c_double(0)
        dis_cc_n, res_cc_n, dis_nc_n, qel_nc_n, res_nc_n = ctypes.c_double(0), ctypes.c_double(0), ctypes.c_double(0), ctypes.c_double(0), ctypes.c_double(0)
        dis_cc_p_g.GetPoint(i, x_bin, dis_cc_p)
        dis_cc_n_g.GetPoint(i, x_bin, dis_cc_n)
        res_cc_p_g.GetPoint(i, x_bin, res_cc_p)
        res_cc_n_g.GetPoint(i, x_bin, res_cc_n)
        dis_nc_p_g.GetPoint(i, x_bin, dis_nc_p)
        dis_nc_n_g.GetPoint(i, x_bin, dis_nc_n)
        qel_nc_p_g.GetPoint(i, x_bin, qel_nc_p)
        qel_nc_n_g.GetPoint(i, x_bin, qel_nc_n)
        res_nc_p_g.GetPoint(i, x_bin, res_nc_p)
        res_nc_n_g.GetPoint(i, x_bin, res_nc_n)

        x.append(x_bin.value)
        dis_cc.append(dis_cc_p.value + dis_cc_n.value)
        res_cc.append(res_cc_p.value + res_cc_n.value)
        dis_nc.append(dis_nc_p.value + dis_nc_n.value)
        qel_nc.append(qel_nc_p.value + qel_nc_n.value)
        res_nc.append(res_nc_p.value + res_nc_n.value)

    dis_cc_g = ROOT.TGraph(size, x, dis_cc)
    dis_cc_g.SetLineWidth(3)
    res_cc_g = ROOT.TGraph(size, x, res_cc) 
    res_cc_g.SetLineWidth(3)
    dis_nc_g = ROOT.TGraph(size, x, dis_nc) 
    dis_nc_g.SetLineWidth(3)
    qel_nc_g = ROOT.TGraph(size, x, qel_nc) 
    qel_nc_g.SetLineWidth(3)
    res_nc_g = ROOT.TGraph(size, x, res_nc) 
    res_nc_g.SetLineWidth(3)

    axis_titles = None
    if 'nu_e_O16' in out_name:
        axis_titles = ';Neutrino Energy (GeV); O^{16} #nu_{e} cross section/E_{#nu} (10^{-38} cm^{2} / GeV)'
    elif 'nu_e_bar_O16' in out_name: 
        axis_titles = ';Neutrino Energy (GeV); O^{16} #bar{#nu}_{e} cross section/E_{#nu} (10^{-38} cm^{2} / GeV)'
    elif 'nu_mu_O16' in out_name:
        axis_titles = ';Neutrino Energy (GeV); O^{16} #nu_{#mu} cross section/E_{#nu} (10^{-38} cm^{2} / GeV)'
    elif 'nu_mu_bar_O16' in out_name:
        axis_titles = ';Neutrino Energy (GeV); O^{16} #bar{#nu}_{#mu} cross section/E_{#nu} (10^{-38} cm^{2} / GeV)'
    else:
        print('WTF!')

    # Define an empty histogram to set global variables
    hempty = ROOT.TH2F('hempty', axis_titles, 1, 0, 15, 1, 1e-2, 20)
    utils.format_hist(hempty)
    hempty.GetYaxis().SetTitleOffset(0.8)

    # Set the graph colours
    tot_cc_g.SetLineColor(ROOT.kBlack)
    qel_cc_g.SetLineColor(ROOT.kBlue+1)
    res_cc_g.SetLineColor(ROOT.kRed+1)
    dis_cc_g.SetLineColor(ROOT.kGreen+1)
    coh_cc_g.SetLineColor(ROOT.kYellow+1)
    mec_cc_g.SetLineColor(ROOT.kCyan+1)

    tot_nc_g.SetLineColor(ROOT.kBlack)
    qel_nc_g.SetLineColor(ROOT.kBlue+1)
    res_nc_g.SetLineColor(ROOT.kRed+1)
    dis_nc_g.SetLineColor(ROOT.kGreen+1)
    coh_nc_g.SetLineColor(ROOT.kYellow+1)
    mec_nc_g.SetLineColor(ROOT.kCyan+1)

    # Create the legends
    leg_cc = ROOT.TLegend(0.7, 0.22, 0.85, 0.42)
    leg_cc.AddEntry(tot_cc_g, 'Total CC', 'L')
    leg_cc.AddEntry(qel_cc_g, 'CC QE', 'L')
    leg_cc.AddEntry(res_cc_g, 'CC Res', 'L')
    leg_cc.AddEntry(dis_cc_g, 'CC DIS', 'L')
    leg_cc.AddEntry(coh_cc_g, 'CC Coh', 'L')
    leg_cc.AddEntry(mec_cc_g, 'CC mec', 'L')
    leg_cc.SetFillStyle(0)
    
    leg_nc = ROOT.TLegend(0.7, 0.22, 0.85, 0.42)
    leg_nc.AddEntry(tot_nc_g, 'Total NC', 'L')
    leg_nc.AddEntry(qel_nc_g, 'NC QE', 'L')
    leg_nc.AddEntry(res_nc_g, 'NC Res', 'L')
    leg_nc.AddEntry(dis_nc_g, 'NC DIS', 'L')
    leg_nc.AddEntry(coh_nc_g, 'NC Coh', 'L')
    leg_nc.AddEntry(mec_nc_g, 'NC Mec', 'L')
    leg_nc.SetFillStyle(0)

    # Create box showing CHIPS energy range [2,5] GeV
    low_line = ROOT.TLine(2, 0, 2, 20)
    low_line.SetLineWidth(3)
    low_line.SetLineColor(14)
    chips_box = ROOT.TBox(2, 0, 5, 20)
    chips_box.SetFillColor(14)
    chips_box.SetFillStyle(3345)
    high_line = ROOT.TLine(5, 0, 5, 20)
    high_line.SetLineWidth(3)
    high_line.SetLineColor(14)
    text = ROOT.TLatex(.1, .93, '')
    text.SetTextSize(1.5/30.)
    text.SetTextColor(13)
    
    # Create the canvases and draw all graphs
    cs_canvas_cc = ROOT.TCanvas('genie_cross_sections_cc', 'genie_cross_sections_cc', 1000, 800)
    cs_canvas_cc.SetLogy()
    cs_canvas_cc.cd()
    hempty.Draw()
    tot_cc_g.Draw('same')
    coh_cc_g.Draw('same')
    mec_cc_g.Draw('same')
    dis_cc_g.Draw('same')
    qel_cc_g.Draw('same')
    res_cc_g.Draw('same')
    leg_cc.Draw('same')
    low_line.Draw('same')
    chips_box.Draw('same')
    high_line.Draw('same')
    text.DrawText(2.45, 10, 'CHIPS')
    cs_canvas_cc.Draw()

    cs_canvas_nc = ROOT.TCanvas('genie_cross_sections_nc', 'genie_cross_sections_nc', 1000, 800)
    cs_canvas_nc.SetLogy()
    cs_canvas_nc.cd()
    hempty.Draw()
    tot_nc_g.Draw('same')
    coh_nc_g.Draw('same')
    mec_nc_g.Draw('same')
    dis_nc_g.Draw('same')
    qel_nc_g.Draw('same')
    res_nc_g.Draw('same')
    leg_nc.Draw('same')
    low_line.Draw('same')
    chips_box.Draw('same')
    high_line.Draw('same')
    text.DrawText(2.5, 10, 'CHIPS')
    cs_canvas_nc.Draw()

    png_cc = '../diagrams/cvn/xsec_cc_'
    png_cc += out_name
    png_cc += '.png'
    macro_cc = './output/xsec_cc_'
    macro_cc += out_name
    macro_cc += '.C'

    png_nc = '../diagrams/cvn/xsec_nc_'
    png_nc += out_name
    png_nc += '.png'
    macro_nc = './output/xsec_nc_'
    macro_nc += out_name
    macro_nc += '.C'


    # Save canvas as png and root macro
    cs_canvas_cc.SaveAs(png_cc)
    cs_canvas_nc.SaveAs(png_nc)

    cs_file.Close()

def xsec():
    make_plots('./data/xsec_nuel.root', 'nu_e_O16')
    make_plots('./data/xsec_anuel.root', 'nu_e_bar_O16')
    make_plots('./data/xsec_numu.root', 'nu_mu_O16')
    make_plots('./data/xsec_anumu.root', 'nu_mu_bar_O16')


if __name__ == '__main__':
    xsec()