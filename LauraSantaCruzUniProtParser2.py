#!/usr/bin/env python3
''' Laura Santa Cruz Kaster
'''
import sys, os, re, gzip

def usage(args):
   print("Usage: LauraSantaCruzUniProtParser2.py --help | --go | --doi [FILE] ?[FILE]?") #  %args[0])
   exit(0)

def mhelp(args):
   print('Fasta-Parser by Laura Santa Cruz, 2023')
   print('Extract information from Uniprot data files.')
   print('-----------------------------------------------')
   print('Optional arguments are:')
   print('\t --help \t -  display this help page')
   print('\t --go \t - show a protein ID to GO id mapping ')
   print('\t --doi \t - show a protein ID to DOI mapping (not today)')
   print('Mandatory arguments are:')
   print('\t FILE \t \t - one ore more compressed or uncompressed Uniprot data files')
   usage(args)

def get_go_ids(filename):
    if re.search('.gz$',filename):
        file = gzip.open(filename,'rt')
    else:
        file = open(filename,'rt')

    currentIDGO=''
    sol=filename #so on the first line the filename is printed
    for line in file:
        if re.search('^ID',line):
            sol=sol+'\n'+currentIDGO
            protids=line[4:15]
            currentIDGO = protids+'\t'+'NA'

        if re.search('GO:[0-9]',line):
            protgo = line[9:19]
            currentIDGO=protids+'\t'+protgo
            sol=sol+'\n'+currentIDGO
        
    file.close()
    return sol

def get_doi_ids(filename):
    sol = 'DOI: not implemented yet \n'
    return sol

def get_keggs_ids(filename):
    if re.search('.gz$',filename):
        file = gzip.open(filename,'rt')
    else:
        file = open(filename,'rt')

    currentIDKEGGS=''
    sol=filename # so on the first line the filename is printed
    for line in file:
        if re.search('^ID',line):
            sol=sol+'\n'+currentIDKEGGS
            protids=line[4:15]
            currentIDKEGGS = protids+'\t'+'NA'

        if re.search('^//',line):
            pass

        if re.search('KEGG;',line):
            protkegg = line[5:22]
            currentIDKEGGS=protids+'\t'+protkegg
            sol=sol+'\n'+currentIDKEGGS
        
    file.close()
    return sol

def main(args):
    if len(args) <= 2 or "--help" in args:
        mhelp(args)

    if len(args) >= 3: 
        command = args[1]
        filename = args[2] #store variables

        # we check if each the input files are valid
        for i in range(2,len(args)):
            filename = args[i]

            if not (re.search('.+(dat$)|.+(dat.gz$)',filename)):
                print(f'Error: File {filename} does not have the right format')
                usage(args)

            elif not (os.path.exists(filename)):                
                print(f"Error: File {filename} does not exist")
                usage(args)

            elif '--go' in command:
                sol = get_go_ids(filename)

            elif '--doi' in command:
                sol = get_doi_ids(filename)
            
            elif '--keggs' in command:
                sol = get_keggs_ids(filename)

            else:
                print(f'Error: {command} is not a valid command')
                usage(args)
            print(sol)

if __name__ == "__main__":
   main(sys.argv)