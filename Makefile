LaTeXSources= $(wildcard *.tex *.bib)

default: build

build: $(LaTeXSources)
	lualatex --halt-on-error --output-directory=build main.tex
	bibtex build/main
	lualatex --halt-on-error --output-directory=build main.tex
	lualatex --halt-on-error --output-directory=build main.tex

clean: 
	-@rm -f build/*.cut build/*.aux build/*.bbl build/*.bcf build/*.blg build/*.fdb_latexmk build/*.fls build/*.lof build/*.log build/*.lot build/*.out build/*.run.xml build/*.gz build/*.toc