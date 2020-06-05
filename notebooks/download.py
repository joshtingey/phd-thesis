import os
import urllib.request
import utils


def main():
    print('Downloading data if required...')
    url = 'http://www.hep.ucl.ac.uk/~jtingey/data/'
    files = [
        'flux.root',
        'xsec_nuel.root',
        'xsec_anuel.root',
        'xsec_numu.root',
        'xsec_anumu.root',
        'events_nuel.root',
        'events_anuel.root',
        'events_numu.root',
        'events_anumu.root',
        'events_nuel.txt',
        'events_anuel.txt',
        'events_numu.txt',
        'events_anumu.txt',
        'profile_electrons.root',
        'profile_muons.root',
        'profile_pions.root',
        'profile_protons.root',
        'digi_sk1pe.root',
        'cvn_flux_output.root',
        'cvn_uniform_output.root',
    ]

    for file in files:
        if not os.path.exists(os.path.join('./data/', file)):
            urllib.request.urlretrieve(url+file, os.path.join('./data/', file))

if __name__ == "__main__":
    main()