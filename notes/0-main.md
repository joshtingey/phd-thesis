# Main plan

```mermaid
gantt
section Writing
Completed                   :done,    total, 2020-05-13, 2020-08-17
Neutrino oscillations       :active,  theory, 2020-05-13, 2020-05-24
The CHIPS R&D project       :         chips, after theory, 2w
Data acquisition            :         daq, after chips, 2w
CNN Finalise                :         cvnwork, after daq, 1w
CNNs for CHIPS              :         cvn, after cvnwork, 2w
Detector Studies            :         studies, after cvn, 2w
Intro and Conclusion        :         intconc, after studies, 2w
Tidy and Improve            :         tidy, after intconc, 1w

section Work
Getting data ready          :         data, 2020-05-13, 39d

section Deadlines
Theory, CHIPS, DAQ Comments :crit,    com1, 2020-06-21, 1d
CVN Comments                :crit,    com2, 2020-07-12, 1d
Final Comments              :crit,    com2, 2020-08-16, 1d

section Other
ml-course                   :active,  course, 2020-05-13, 2020-06-08
write-cv                    :active,  cv, 2020-05-13, 2020-08-17
the-trains                  :active,  trains, 2020-05-13, 2020-08-17
```

- Keep the gantt chart updated as progress is made
- Under each chapter heading have the following
  - Rough length chapter will be
  - Goal statement for the chapter
  - Sub-sections (if any) and a brief description for each
  - Diagrams in their sub-sections
  - References in their sub-sections

## Frontmatter (~?)

## Introduction and Authors Contribution (~5)

[](@note/2-introduction.md)

## Neutrino oscillations: theoretical background and current status (~30)

[](@note/3-theory.md)

## The CHIPS R&D project (~20)

[](@note/4-chips.md)

## Data acquisition for CHIPS (~20)

[](@note/5-daq.md)

## A Convolutional neural network for CHIPS (~50)

[](@note/6-cvn.md)

## Detector optimisation for CHIPS (~20)

[](@note/7-optimisation.md)

## Conclusion (~5)

[](@note/8-conclusion.md)

## Appendices (~?)

## genie xsec commands

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

