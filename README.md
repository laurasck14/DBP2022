Databases and Practical programming course 2022 at the University of Potsdam (Msc Bioinformatics).

This code is and exercise from the Databases and Practical Programming course from the Msc Bioinformatics at the University of Potsdam. The goal was to create file parser for UniProt data files in order to extract relevant information from them (uniprot-microsporidian-data-2022-02.dat file for example file).

**LauraSantaCruzUniProtParser2.py**\
Simple terminal parser to extract all the KEGGS and Gene Ontology (GO) IDs from un/compressed Uniprot datafiles.

Required arguments:\
tab-separated file(s) to be processed

Optional arguments:\
   --help: display help page.\
   --go: show mapping between protein ID and GO ID.\
   --doi: show mapping between protein ID and GO ID (not inmplemented here).\

Example usage: python3 LauraSantaCruzUniProtParser2.py --go uniprot-microsporidian-data-2022-02.dat\
The parser prints the results directly at the terminal.

**LauraSantaCruzUniProtParser3.py**\
Built-on version of the previous parser including a simple GUI from tkinter to better visualize the results. It inherits the functionallities from the Parser2.py.
The user must select the directory where the data files are located. Then the GUI will show the found files in the first column, the functionallities that can be used in the second one and the results in the third. The functionallity must be clicked twice after a file has been selected to display the results.

Example usage: python3 LauraSantaCruzUniProtParser3.py

**LauraSantaCruzUniProtParser3Combo.py**\
Different GUI display using a combobox to select the desired functionallity. The results are displayed after double-clicking on the data file selected.

Example usage: python3 LauraSantaCruzUniProtParser3Combo.py
