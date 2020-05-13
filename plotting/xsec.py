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
    cc_heights = None
    nc_heights = None
    if 'nu_e_O16' in out_name:
        axis_titles = ';Neutrino Energy (GeV); O^{16} #nu_{e} cross section/E_{#nu} (10^{-38} cm^{2} / GeV)'
        cc_heights = [14, 0.35, 1, 6, 0.035, 0.1]
        nc_heights = [4.5, 0.13, 0.65, 2.0, 0.018, 0.035]
    elif 'nu_e_bar_O16' in out_name: 
        axis_titles = ';Neutrino Energy (GeV); O^{16} #bar{#nu}_{e} cross section/E_{#nu} (10^{-38} cm^{2} / GeV)'
        cc_heights = [7, 0.3, 0.8, 2.1, 0.035, 0.09]
        nc_heights = [2.5, 0.11, 0.3, 0.9, 0.018, 0.032]
    elif 'nu_mu_O16' in out_name:
        axis_titles = ';Neutrino Energy (GeV); O^{16} #nu_{#mu} cross section/E_{#nu} (10^{-38} cm^{2} / GeV)'
        cc_heights = [14, 0.35, 1, 6, 0.032, 0.1]
        nc_heights = [4.5, 0.12, 0.35, 2.0, 0.018, 0.035]
    elif 'nu_mu_bar_O16' in out_name:
        axis_titles = ';Neutrino Energy (GeV); O^{16} #bar{#nu}_{#mu} cross section/E_{#nu} (10^{-38} cm^{2} / GeV)'
        cc_heights = [6.5, 0.3, 0.75, 2.2, 0.035, 0.09]
        nc_heights = [2.5, 0.12, 0.3, 0.9, 0.017, 0.032]
    else:
        print('WTF!')

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

    cc_plots = [tot_cc_g, qel_cc_g, res_cc_g, dis_cc_g, coh_cc_g, mec_cc_g]
    utils.plot(cc_plots, axis_titles, './output/xsec_cc_' + out_name + '.png',
               0, 15, 1e-2, 30, opt='L', cuts=[[2, 5]], log_y=True,
               texts=[
                   ['CHIPS', 2.45, 1.5e-2, 1.5/30.0, 13],
                   ['CC Total', 11, cc_heights[0], 1.2/30.0, ROOT.kBlack],
                   ['CC QE', 11, cc_heights[1], 1.2/30.0, ROOT.kBlue+1],
                   ['CC Res', 11, cc_heights[2], 1.2/30.0, ROOT.kRed+1],
                   ['CC DIS', 11, cc_heights[3], 1.2/30.0, ROOT.kGreen+1],
                   ['CC Coh', 11, cc_heights[4], 1.2/30.0, ROOT.kYellow+1],
                   ['CC Mec', 11, cc_heights[5], 1.2/30.0, ROOT.kCyan+1]
               ])


    nc_plots = [tot_nc_g, qel_nc_g, res_nc_g, dis_nc_g, coh_nc_g, mec_nc_g]
    utils.plot(nc_plots, axis_titles, './output/xsec_nc_' + out_name + '.png',
               0, 15, 1e-2, 30, opt='L', cuts=[[2, 5]], log_y=True,
               texts=[
                   ['CHIPS', 2.45, 1.5e-2, 1.5/30.0, 13],
                   ['NC Total', 11, nc_heights[0], 1.2/30.0, ROOT.kBlack],
                   ['NC QE', 11, nc_heights[1], 1.2/30.0, ROOT.kBlue+1],
                   ['NC Res', 11, nc_heights[2], 1.2/30.0, ROOT.kRed+1],
                   ['NC DIS', 11, nc_heights[3], 1.2/30.0, ROOT.kGreen+1],
                   ['NC Coh', 11, nc_heights[4], 1.2/30.0, ROOT.kYellow+1],
                   ['NC Mec', 11, nc_heights[5], 1.2/30.0, ROOT.kCyan+1]
               ])


    cs_file.Close()


def xsec():
    make_plots('./data/xsec_nuel.root', 'nu_e_O16')
    make_plots('./data/xsec_anuel.root', 'nu_e_bar_O16')
    make_plots('./data/xsec_numu.root', 'nu_mu_O16')
    make_plots('./data/xsec_anumu.root', 'nu_mu_bar_O16')


if __name__ == '__main__':
    with utils.CHIPSStyle():
        xsec()