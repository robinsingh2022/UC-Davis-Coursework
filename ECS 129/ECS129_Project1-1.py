# DNA Replication
def reverse(my_seq1):
    x = list(my_seq1)
    x.reverse()
    reverse = ""
    for i in x:
        reverse = reverse + i
#    print(reverse)
    return reverse
#function used to reverse from 3'-5' to 5'-3' from my_seq


def replication(reverse):
    output = []
    for y in reverse:
        if y in base_pair_DNA:
            output.append(base_pair_DNA[y])
    comp1 = ""
    for i in output:
        comp1 = comp1 + i
#    print(comp1)
    return comp1
#function used to convert reversed template strand to 5'-3' replicated DNA 'coding' strand


# DNA Transcription
def transcription(my_seq):
    replacement = []
    lis = list(my_seq)
    for i in lis:
        if i in base_pair_DNA_to_RNA:
            replacement.append(base_pair_DNA_to_RNA1[i])      
    comp=""
    for i in replacement:
        comp = comp+i
#    print(comp)
    return comp
#function used to change both original DNA coding strand and replicated DNA coding strand


### RNA_ORF ###
def RNA_ORF (comp):
    start = comp.find('AUG')
    #function of the open reading frame is to find the first AUG
    comp = comp[start:]
    started = ([comp[i:i+3] for i in range(0, len(comp), 3)])
    #split strand every 3 for codons
#    print(started)
    positions = []
    for i in started:      
        if i == 'UAA':
            positions.append(started.index('UAA'))                            
        elif i =='UAG':           
            positions.append(started.index('UAG'))           
        elif i =='UGA':
            positions.append(started.index('UGA'))
    #find any of the 3 stop codon, then stop
    if len(positions)>=1:       
        end = min(positions)
    else:
        return("This strand does not have a stop codon.")
    #if no stop codon detected, will print the message
    stopped = started[:end + 1]
#    print(stopped)
    return stopped


### RNA Translation ###
def translate_mRNA(stopped):
    lis2 =[]   
    for element in stopped:
        if element in codon_table_mRNA:
            lis2.append(codon_table_mRNA[element])
#    print(lis2)
    return lis2
#function used for translating all the codon splitted from RNA_ORF and match with protein one letter code


### Convert List to String ###
def listToString(lis2): 
    comp=""
    for i in lis2:
        comp = comp+i
    print('Found protein sequence',comp, 'from the coding strand.')
    return comp
#converting a list from translate_mRNA back into a string to compare with endresult of listToString1

def listToString1(lis2): 
    comp=""
    for i in lis2:
        comp = comp+i
    print('Found protein sequence',comp, 'from the template strand.\n\nComparing for the longest Open Reading Frame...')
    return comp
#converting a list from translate_mRNA back into a string to compare with endresult of listToString


### Convert Configs ###
base_pair_DNA = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
base_pair_RNA = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
base_pair_DNA_to_RNA = {'A':'U', 'T':'A', 'G':'C', 'C':'G'}
base_pair_DNA_to_RNA1 = {'A':'A', 'T':'U', 'G':'G', 'C':'C'}
codon_table_mRNA = {'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M', 'ACA':'T',
                    'ACC':'T', 'ACG':'T', 'ACU':'T', 'AAC':'N', 'AAU':'N',
                    'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGU':'S', 'AGA':'R',
                    'AGG':'R', 'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
                    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P', 'CAC':'H',
                    'CAU':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R',
                    'CGG':'R', 'CGU':'R', 'GUA':'V', 'GUC':'V', 'GUG':'V',
                    'GUU':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
                    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G',
                    'GGC':'G', 'GGG':'G', 'GGU':'G', 'UCA':'S', 'UCC':'S',
                    'UCG':'S', 'UCU':'S', 'UUC':'F', 'UUU':'F', 'UUA':'L',
                    'UUG':'L', 'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
                    'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W'}


### Main Checker ###
def checker(my_seq):
    if len(my_seq) <3:
        print("You have entered less than 3 letters.\nNot enough letters to read.\nProgram aborted.")
        exit()
    for i in my_seq:
        if i != 'A' and i != 'C' and i != 'T' and i != 'G':
            print("Detected one or more non-DNA base pair letter.\nProgram aborted.\nPlease check your DNA Sequence and retry.\n")
            exit()

## Main Codes ###        
### Start by converting all lowercase -> uppercase ###
file_seq = input("Would you like to import sequence from file? (y/n/exit) \n")
#Reading a .txt file with a sequence in it
my_seq = ''
while my_seq == '':
    try:
        if file_seq == 'y':
            inputfile = input("Enter the location and the name of the DNA sequence file: \n")
            #inputfile = str(inputfile)
            with open(inputfile, 'rb') as f:
                my_seq = f.read().decode("utf-8")
                if not my_seq == '':
                    break
        elif file_seq == 'n':
            my_seq = input("Please Enter DNA Sequence in 5' to 3' Direction:\n")
            break
        elif file_seq == 'exit':
            exit()
        elif not file_seq == 'y' or  not file_seq == 'n':
            print('The character entered is not recognized.')
            file_seq = input("Would you like to import sequence from file? (y/n/exit) \n")
    except FileNotFoundError:
        print("No such file or directory was found")
        inputfile = input("Enter the location and the name of the DNA sequence file: \n")      
x = 0
#if user enters "Return", it will abort program
if my_seq == "":
    print('You entered nothing')
    exit()
for i in my_seq:  
    if i.islower() == True:
        my_seq = my_seq.upper()
        x = x+1
if x>=1:
    print('Detected one or more lowercase in DNA Sequence.\nConverted', x ,'lowercase(s) to uppercase(s).\nProgram continue to run.\n')
#create endresult list for comparison for longest open reading frame
endresult = []
#using checker to make sure sequence has met conditions
checker(my_seq)
#autocorrected any unwanted lowercase/non-basepairs letters
my_seq1 = my_seq
#copy an extra strand to work with
#my_seq = coding strand
#my_seq1 = template strand

endresult.append(listToString(translate_mRNA(RNA_ORF(transcription(my_seq)))))
#call all functions to translate from DNA coding strand -> RNA strand -> Protein
endresult.append(listToString1(translate_mRNA(RNA_ORF(transcription(replication(reverse(my_seq1)))))))
#call all functions to translate from DNA template strand -> reverse and replicate -> RNA strand -> Protein
print('The first longest open reading frame found has the protein sequence consist of...')
if max(endresult, key=len) == "":
    print('No protein sequence was found from either strands.')
elif max(endresult, key=len) == min(endresult, key=len):
    print(max(endresult, key=len), 'and', min(endresult, key=len))
else:
    print(max(endresult, key=len))

