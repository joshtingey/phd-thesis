# ROOT plotting macros and data

All initial data files used to generate those found in ./data are located at /unix/chips/jtingey/data at UCL

## To get cross section ROOT files from GENIE... 

```
$ gspl2root -f xsec_oxygen.xml -p 12 -t 1000010010 -o nuel_xsec.root
$ gspl2root -f xsec_oxygen.xml -p 12 -t 1000080160 -o nuel_xsec.root
$ gspl2root -f xsec_oxygen.xml -p -12 -t 1000010010 -o anuel_xsec.root
$ gspl2root -f xsec_oxygen.xml -p -12 -t 1000080160 -o anuel_xsec.root
$ gspl2root -f xsec_oxygen.xml -p 14 -t 1000010010 -o numu_xsec.root
$ gspl2root -f xsec_oxygen.xml -p 14 -t 1000080160 -o numu_xsec.root
$ gspl2root -f xsec_oxygen.xml -p -14 -t 1000010010 -o anumu_xsec.root
$ gspl2root -f xsec_oxygen.xml -p -14 -t 1000080160 -o anumu_xsec.root
```