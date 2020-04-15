# ROOT plotting macros and data

All initial data files used to generate those found in ./data are located at /unix/chips/jtingey/data at UCL

## flux

## xsec

```
$ gspl2root -f ./data/genie/xsecs_G1802a00000.xml -p 12 -t 1000010010 -o xsec_nuel.root
$ gspl2root -f ./data/genie/xsecs_G1802a00000.xml -p 12 -t 1000080160 -o xsec_nuel.root
$ gspl2root -f ./data/genie/xsecs_G1802a00000.xml -p -12 -t 1000010010 -o xsec_anuel.root
$ gspl2root -f ./data/genie/xsecs_G1802a00000.xml -p -12 -t 1000080160 -o xsec_anuel.root
$ gspl2root -f ./data/genie/xsecs_G1802a00000.xml -p 14 -t 1000010010 -o xsec_numu.root
$ gspl2root -f ./data/genie/xsecs_G1802a00000.xml -p 14 -t 1000080160 -o xsec_numu.root
$ gspl2root -f ./data/genie/xsecs_G1802a00000.xml -p -14 -t 1000010010 -o xsec_anumu.root
$ gspl2root -f ./data/genie/xsecs_G1802a00000.xml -p -14 -t 1000080160 -o xsec_anumu.root
```

These files can then be downloaded for use in plotting

## events



## profiles

- They are all at 2500MeV

## digi

