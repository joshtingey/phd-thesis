import os
import ROOT
import utils


def flux():
    # Open the file and get all the histograms we need
    root_file = ROOT.TFile(os.path.join('./data/', 'flux.root'))
    nuel_cc_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_nue_allpar_tot_cc_CHIPSoffAXIS')
    anuel_cc_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_anue_allpar_tot_cc_CHIPSoffAXIS')
    numu_cc_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_numu_allpar_tot_cc_CHIPSoffAXIS')
    anumu_cc_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_anumu_allpar_tot_cc_CHIPSoffAXIS')
    nuel_nc_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_nue_allpar_tot_nc_CHIPSoffAXIS')
    anuel_nc_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_anue_allpar_tot_nc_CHIPSoffAXIS')
    numu_nc_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_numu_allpar_tot_nc_CHIPSoffAXIS')
    anumu_nc_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_anumu_allpar_tot_nc_CHIPSoffAXIS')
    nuel_flux_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_nue_allpar_NoXSec_CHIPSoffAXIS')
    anuel_flux_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_anue_allpar_NoXSec_CHIPSoffAXIS')
    numu_flux_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_numu_allpar_NoXSec_CHIPSoffAXIS')
    anumu_flux_h = root_file.Get('enufullfine/CHIPSoffAXIS/enufullfine_anumu_allpar_NoXSec_CHIPSoffAXIS')

    numu_flux_nova_h = root_file.Get('enufullfine/NOvA_FD_Shift/enufullfine_numu_allpar_NoXSec_NOvA_FD_Shift')
    numu_flux_minos_h = root_file.Get('enufullfine/MINOS_FD/enufullfine_numu_allpar_NoXSec_MINOS_FD')

    min = 0.0
    max = 15.0
    nuel_cc = nuel_cc_h.Integral(nuel_cc_h.FindFixBin(min), nuel_cc_h.FindFixBin(max), '')
    anuel_cc = anuel_cc_h.Integral(anuel_cc_h.FindFixBin(min), anuel_cc_h.FindFixBin(max), '')
    numu_cc = numu_cc_h.Integral(numu_cc_h.FindFixBin(min), numu_cc_h.FindFixBin(max), '')
    anumu_cc = anumu_cc_h.Integral(anumu_cc_h.FindFixBin(min), anumu_cc_h.FindFixBin(max), '')
    nuel_nc = nuel_nc_h.Integral(nuel_nc_h.FindFixBin(min), nuel_nc_h.FindFixBin(max), '')
    anuel_nc = anuel_nc_h.Integral(anuel_nc_h.FindFixBin(min), anuel_nc_h.FindFixBin(max), '')
    numu_nc = numu_nc_h.Integral(numu_nc_h.FindFixBin(min), numu_nc_h.FindFixBin(max), '')
    anumu_nc = anumu_nc_h.Integral(anumu_nc_h.FindFixBin(min), anumu_nc_h.FindFixBin(max), '')

    scale = (6*pow(10,20))/(50*pow(10,6))
    nuel_cc = nuel_cc * scale
    anuel_cc = anuel_cc * scale
    numu_cc = numu_cc * scale
    anumu_cc = anumu_cc * scale
    nuel_nc = nuel_nc * scale
    anuel_nc = anuel_nc * scale
    numu_nc = numu_nc * scale
    anumu_nc = anumu_nc * scale
    total = nuel_cc + anuel_cc + numu_cc + anumu_cc + nuel_nc + anuel_nc + numu_nc + anumu_nc

    nuel_tot = nuel_cc + nuel_nc
    anuel_tot = anuel_cc + anuel_nc
    numu_tot = numu_cc + numu_nc
    anumu_tot = anumu_cc + anumu_nc

    print('###########################################################')
    print('Events/6*10^20 POT/kt in the range [0,{}]...\n'.format(max))
    print('nuel_cc: {}, frac: {}'.format(nuel_cc, nuel_cc/total))
    print('anuel_cc: {}, frac: {}'.format(anuel_cc, anuel_cc/total))
    print('numu_cc: {}, frac: {}'.format(numu_cc, numu_cc/total))
    print('anumu_cc: {}, frac: {}'.format(anumu_cc, anumu_cc/total))
    print('nuel_nc: {}, frac: {}'.format(nuel_nc, nuel_nc/total))
    print('anuel_nc: {}, frac: {}'.format(anuel_nc, anuel_nc/total))
    print('numu_nc: {}, frac: {}'.format(numu_nc, numu_nc/total))
    print('anumu_nc: {}, frac: {}'.format(anumu_nc, anumu_nc/total))
    print('Total: {}'.format(total))

    print('\nnuel_tot: {}, frac: {}'.format(nuel_tot, (nuel_tot/total)))
    print('anuel_tot: {}, frac: {}'.format(anuel_tot, (anuel_tot/total)))
    print('numu_tot: {}, frac: {}'.format(numu_tot, (numu_tot/total)))
    print('anumu_tot: {}, frac: {}'.format(anumu_tot, (anumu_tot/total)))
    print('###########################################################')

    weight_file = open('./output/weights.txt', 'w')
    weight_file.write(str(nuel_tot/total) + '\n')
    weight_file.write(str(anuel_tot/total) + '\n')
    weight_file.write(str(numu_tot/total) + '\n')
    weight_file.write(str(anumu_tot/total) + '\n')
    weight_file.write(str(total) + '\n')
    weight_file.close()

    scale = (6*pow(10,20))/(50*pow(10,6))
    nuel_flux_h.Scale(scale)
    nuel_flux_h.SetTitle('#nu_{e}') 
    nuel_flux_h.SetLineColor(ROOT.kGreen+1)
    anuel_flux_h.Scale(scale) 
    anuel_flux_h.SetTitle('#bar{#nu}_{e}') 
    anuel_flux_h.SetLineColor(ROOT.kGreen+2)
    numu_flux_h.Scale(scale) 
    numu_flux_h.SetTitle('#nu_{#mu}') 
    numu_flux_h.SetLineColor(ROOT.kBlue+1)
    anumu_flux_h.Scale(scale) 
    anumu_flux_h.SetTitle('#bar{#nu}_{#mu}') 
    anumu_flux_h.SetLineColor(ROOT.kBlue+2)
 
    hists = [nuel_flux_h, anuel_flux_h, numu_flux_h, anumu_flux_h]
    utils.plot(hists, '; Neutrino Energy (GeV); #nu/6#times10^{20}POT/kt', './output/flux.png',
               0, 15, 1e2, 1.5e6, opt='samehist', leg_opt='L', log_y=True)

    numu_flux_h.SetTitle('CHIPS #nu_{#mu} Flux') 
    numu_flux_h.SetLineColor(ROOT.kBlue+1)
    numu_flux_nova_h.Scale(scale) 
    numu_flux_nova_h.SetTitle('Nova #nu_{#mu} Flux') 
    numu_flux_nova_h.SetLineColor(ROOT.kRed+1)
    numu_flux_minos_h.Scale(scale) 
    numu_flux_minos_h.SetTitle('Minos #nu_{#mu} Flux') 
    numu_flux_minos_h.SetLineColor(ROOT.kGreen+1)

    hists = [numu_flux_h, numu_flux_nova_h, numu_flux_minos_h]
    utils.plot(hists, '; Neutrino Energy (GeV); #nu/6#times10^{20}POT/kt', './output/flux_comparison.png',
               0, 15, 0, 1.4e6, opt='samehist', leg_opt='L')


    root_file.Close()


if __name__ == '__main__':
    with utils.CHIPSStyle():
        flux()