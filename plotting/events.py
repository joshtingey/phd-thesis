import ROOT
import utils

def events():
    weights_file = open("./output/weights.txt", "r")
    nuel_w = float(weights_file.readline())
    anuel_w = float(weights_file.readline())
    numu_w = float(weights_file.readline())
    anumu_w = float(weights_file.readline())
    total = float(weights_file.readline())
    weights_file.close()
    print("nuel: {}, anuel: {}, numu: {}, anumu:{}, total: {}".format(
        nuel_w, anuel_w, numu_w, anumu_w, total
    ))

    nuel_file = ROOT.TFile("./data/events_nuel.root")
    anuel_file = ROOT.TFile("./data/events_anuel.root")
    numu_file = ROOT.TFile("./data/events_numu.root")
    anumu_file = ROOT.TFile("./data/events_anumu.root")

    nuel_t_all_h = nuel_file.Get("int_types_all")
    anuel_t_all_h = anuel_file.Get("int_types_all")
    numu_t_all_h = numu_file.Get("int_types_all")
    anumu_t_all_h = anumu_file.Get("int_types_all")

    nuel_num = nuel_t_all_h.GetEntries()
    anuel_num = anuel_t_all_h.GetEntries()
    numu_num = numu_t_all_h.GetEntries()
    anumu_num = anumu_t_all_h.GetEntries()
    total_num = (nuel_w*float(nuel_num)) + (anuel_w*float(anuel_num)) + (numu_w*float(numu_num)) + (anumu_w*float(anumu_num))
    event_scale = total/total_num
    print("Entries total: {}, total: {}, scale: {}".format(total_num, total, event_scale))

    nuel_t_all_h.SetFillColor(ROOT.kGreen+1)
    nuel_t_all_h.SetTitle("#nu_{e}")
    nuel_t_all_h.Scale(nuel_w)
    nuel_t_all_h.Scale(event_scale)
    anuel_t_all_h.SetFillColor(ROOT.kGreen+2)
    anuel_t_all_h.SetTitle("#bar{#nu}_{e}")
    anuel_t_all_h.Scale(anuel_w)
    anuel_t_all_h.Scale(event_scale)
    numu_t_all_h.SetFillColor(ROOT.kBlue+1)
    numu_t_all_h.SetTitle("#nu_{#mu}")
    numu_t_all_h.Scale(numu_w)
    numu_t_all_h.Scale(event_scale)
    anumu_t_all_h.SetFillColor(ROOT.kBlue+2)
    anumu_t_all_h.SetTitle("#bar{#nu}_{#mu}")
    anumu_t_all_h.Scale(anumu_w)
    anumu_t_all_h.Scale(event_scale)

    hists_t = [nuel_t_all_h, anuel_t_all_h, numu_t_all_h, anumu_t_all_h]
    utils.plot(hists_t, "; Interaction Type Code; Number of Events/6#times10^{20}POT/kt", "./output/events_types.png",
               0, 28, 0.1, 200, opt="sameHIST", leg_opt='FB', stack=True, log_y=True)


    # Make stacked int type energy plot
    int_types = 27
    int_names = [
        "CCQE", "NCQE",
        "CCNuPtoLPPiPlus", "CCNuNtoLPPiZero", "CCNuNtoLNPiPlus", 
        "NCNuPtoNuPPiZero", "NCNuPtoNuNPiPlus", "NCNuNtoNuNPiZero", "NCNuNtoNuPPiMinus", 
        "CCNuBarNtoLNPiMinus", "CCNuBarPtoLNPiZero", "CCNuBarPtoLPPiMinus",
        "NCNuBarPtoNuBarPPiZero", "NCNuBarPtoNuBarNPiPlus", "NCNuBarNtoNuBarNPiZero", "NCNuBarNtoNuBarPPiMinus",
        "OtherResonant", "CCMEC", "NCMEC", "IMD",
        "CCDIS", "NCDIS", "NCCoh", "CCCoh", "ElasticScattering", "InverseMuDecay",
        "CosmicMuon"
    ]

    name_e = "h_nuEnergy_"
    ccqel_e = numu_file.Get(name_e + "CCQE")
    ccmec_e = numu_file.Get(name_e + "kCCMEC")
    onepi_e = numu_file.Get(name_e + "CCNuPtoLPPiPlus")
    onepi_e.Add(numu_file.Get(name_e + "CCNuNtoLPPiZero"))
    onepi_e.Add(numu_file.Get(name_e + "CCNuNtoLNPiPlus"))
    cccoh_e = numu_file.Get(name_e + "CCCoh")
    ccdis_e = numu_file.Get(name_e + "CCDIS")
    ccother_e = numu_file.Get(name_e + "kOtherResonant")
    nc_e = numu_file.Get(name_e + "NCQE")
    nc_e.Add(numu_file.Get(name_e + "NCNuPtoNuPPiZero"))
    nc_e.Add(numu_file.Get(name_e + "NCNuPtoNuNPiPlus"))
    nc_e.Add(numu_file.Get(name_e + "NCNuNtoNuNPiZero"))
    nc_e.Add(numu_file.Get(name_e + "NCNuNtoNuPPiMinus"))
    nc_e.Add(numu_file.Get(name_e + "kNCMEC"))
    nc_e.Add(numu_file.Get(name_e + "NCDIS"))
    nc_e.Add(numu_file.Get(name_e + "NCCoh"))
    anumu_e = anumu_file.Get("h_nuEnergy_Other")
    nuel_e = nuel_file.Get("h_nuEnergy_Other")
    anuel_e = anuel_file.Get("h_nuEnergy_Other")
    for i in range(int_types):
        name_e = "h_nuEnergy_"
        name_e += int_names[i]
        anumu_e.Add(anumu_file.Get(name_e))
        nuel_e.Add(nuel_file.Get(name_e))
        anuel_e.Add(anuel_file.Get(name_e))

    ccqel_e.Rebin(2) 
    ccqel_e.SetFillColor(2) 
    ccqel_e.SetTitle("CCQE") 
    ccmec_e.Rebin(2) 
    ccmec_e.SetFillColor(3) 
    ccmec_e.SetTitle("CCMEC")
    onepi_e.Rebin(2) 
    onepi_e.SetFillColor(4) 
    onepi_e.SetTitle("CC1#pi")
    cccoh_e.Rebin(2) 
    cccoh_e.SetFillColor(5) 
    cccoh_e.SetTitle("CCCoh")
    ccdis_e.Rebin(2) 
    ccdis_e.SetFillColor(6) 
    ccdis_e.SetTitle("CCDIS")
    ccother_e.Rebin(2) 
    ccother_e.SetFillColor(7) 
    ccother_e.SetTitle("CCother")
    nc_e.Rebin(2) 
    nc_e.SetFillColor(8) 
    nc_e.SetTitle("NC")  
    anumu_e.Rebin(2) 
    anumu_e.SetFillColor(9) 
    anumu_e.SetTitle("#bar{#nu}_{#mu}")
    nuel_e.Rebin(2) 
    nuel_e.SetFillColor(10) 
    nuel_e.SetTitle("#nu_{e}")
    anuel_e.Rebin(2) 
    anuel_e.SetFillColor(11) 
    anuel_e.SetTitle("#bar{#nu}_{e}")

    ccqel_e.Scale(numu_w) 
    ccqel_e.Scale(event_scale)
    ccmec_e.Scale(numu_w) 
    ccmec_e.Scale(event_scale)
    onepi_e.Scale(numu_w) 
    onepi_e.Scale(event_scale)
    cccoh_e.Scale(numu_w) 
    cccoh_e.Scale(event_scale)
    ccdis_e.Scale(numu_w) 
    ccdis_e.Scale(event_scale)
    ccother_e.Scale(numu_w) 
    ccother_e.Scale(event_scale)
    nc_e.Scale(numu_w) 
    nc_e.Scale(event_scale)
    anumu_e.Scale(anumu_w) 
    anumu_e.Scale(event_scale)
    nuel_e.Scale(nuel_w) 
    nuel_e.Scale(event_scale)
    anuel_e.Scale(anuel_w) 
    anuel_e.Scale(event_scale)
    
    hists_e = [ccqel_e, ccmec_e, onepi_e, cccoh_e, ccdis_e, ccother_e, nc_e, anumu_e, nuel_e, anuel_e]
    utils.create_plot("../diagrams/cvn/events_energies.png", hists_e, ";Neutrino Energy (MeV); Number of Events/6#times10^{20}POT/kt",
                      0, 10000, 1, 50, "FB", "same PFC HIST", False, True, log_y=True)


    # Make stacked final states plot
    name_s = "h_finalStates_"
    ccqel_s = numu_file.Get(name_s + "CCQE")
    ccmec_s = numu_file.Get(name_s + "kCCMEC")
    onepi_s = numu_file.Get(name_s + "CCNuPtoLPPiPlus")
    onepi_s.Add(numu_file.Get(name_s + "CCNuNtoLPPiZero"))
    onepi_s.Add(numu_file.Get(name_s + "CCNuNtoLNPiPlus"))
    cccoh_s = numu_file.Get(name_s + "CCCoh")
    ccdis_s = numu_file.Get(name_s + "CCDIS")
    ccother_s = numu_file.Get(name_s + "kOtherResonant")
    nc_s = numu_file.Get(name_s + "NCQE")
    nc_s.Add(numu_file.Get(name_s + "NCNuPtoNuPPiZero"))
    nc_s.Add(numu_file.Get(name_s + "NCNuPtoNuNPiPlus"))
    nc_s.Add(numu_file.Get(name_s + "NCNuNtoNuNPiZero"))
    nc_s.Add(numu_file.Get(name_s + "NCNuNtoNuPPiMinus"))
    nc_s.Add(numu_file.Get(name_s + "kNCMEC"))
    nc_s.Add(numu_file.Get(name_s + "NCDIS"))
    nc_s.Add(numu_file.Get(name_s + "NCCoh"))

    ccqel_s.SetFillColor(2) 
    ccqel_s.SetTitle("CCQE") 
    ccmec_s.SetFillColor(3) 
    ccmec_s.SetTitle("CCMEC")
    onepi_s.SetFillColor(4) 
    onepi_s.SetTitle("CC1#pi")
    cccoh_s.SetFillColor(5) 
    cccoh_s.SetTitle("CCCoh")
    ccdis_s.SetFillColor(6) 
    ccdis_s.SetTitle("CCDIS")
    ccother_s.SetFillColor(7) 
    ccother_s.SetTitle("CCother")
    nc_s.SetFillColor(8) 
    nc_s.SetTitle("NC")  

    ccqel_s.Scale(numu_w) 
    ccqel_s.Scale(event_scale)
    ccmec_s.Scale(numu_w) 
    ccmec_s.Scale(event_scale)
    onepi_s.Scale(numu_w) 
    onepi_s.Scale(event_scale)
    cccoh_s.Scale(numu_w) 
    cccoh_s.Scale(event_scale)
    ccdis_s.Scale(numu_w) 
    ccdis_s.Scale(event_scale)
    ccother_s.Scale(numu_w) 
    ccother_s.Scale(event_scale)
    nc_s.Scale(numu_w) 
    nc_s.Scale(event_scale)
    
    hists_s = [ccqel_s, ccmec_s, onepi_s, cccoh_s, ccdis_s, ccother_s, nc_s]
    utils.create_plot("../diagrams/cvn/events_states.png", hists_s, ";Final State Type Code; Number of Events/6#times10^{20}POT/kt",
                      0, 33, 0, 200, "FB", "same PFC HIST", False, True);

    nuel_file.Close()
    anuel_file.Close()
    numu_file.Close()
    anumu_file.Close()

    # Can't really do anymore until the disks are back and I can run filtering again for fix bugs
    # - None of the anti energy distributions shows
    # - I can definitely remove some of the categories we don't see
    # - Can I combine nu and anti-nu res categories together?
    # - Check anti particles are treated exactly the same
    # - Add a combined final state plot across all categories like the int type one  


if __name__ == "__main__":
    with utils.CHIPSStyle():
        events()