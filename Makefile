.phony: thesis.pdf clean

thesis.pdf:
	lualatex --halt-on-error --output-directory=build thesis.tex
	biber --output-directory=build thesis 
	lualatex --halt-on-error --output-directory=build thesis.tex
	lualatex --halt-on-error --output-directory=build thesis.tex

clean: 
	-@rm -f build/*.cut build/*.aux build/*.bbl build/*.bcf build/*.blg build/*.fdb_latexmk build/*.fls build/*.lof build/*.log build/*.lot build/*.out build/*.run.xml build/*.gz build/*.toc