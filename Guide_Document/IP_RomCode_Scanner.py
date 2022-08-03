#!/usr/local/bin/python

# / --------------------------------------------------------------------------------------------------------------------
#   File        : IP_RomCode_Scanner.py
#   Description : Handle multiple *.vhe and *.bin code in ROM IP directory and output the duplicate result into Vhe_ROM.txt 
#                 Bin_ROM.txt
#
#   Author      : Lukas Johnny (Lukas.Johnny@xfab.com)
#   Date        : 10-October-2021
#   Version     : v1.0.0
#
#   Updates     : -

import os
import filecmp

class IPSort():
    def __init__(self):
        self.vheDir = []
        self.binDir = []
        self.compareBin = []
        self.value  = 0
        self.processList = ["aa035", "ah018", "ah035", "fc025", "xa035",  "xb06",
                            "xc013", "xc018", "xc06",  "xc10", "xh018", "xh035",
                            "xl035", "xo035", "xp018", "xr013", "xs018", "xt018",
                            "xt06" , "xu035"]

    def UserInput(self,key,value):
        note = dict()
        note[0] = ["""
                *****************************************************************
                *                    -XROM ROM CODE SCANNER-                    *
                *****************************************************************
                This script is used to scan for duplicate *.vhe and *.bin rom code
                that exist in ROM IP directory. Please correct the IP Path and
                ensure the ROM IP is in separate OPTION_* directory with its own
                *.gds, *.cal and *.vhe/.bin file.
                *****************************************************************
                Please Select the Process to run the Scan:

                1. aa035                     11. xh018
                2. ah018                     12. xh035
                3. ah035                     13. xl035
                4. fc025                     14. xo035
                5. xa035                     15. xp018
                6. xb06                      16. xr013
                7. xc013                     17. xs018
                8. xc018                     18. xt018
                9. xc06                      19. xt06
                10. xc10                     20. xu035

                ****************************************************************
            
                 """]

        note[1] = ["""
                ****************************************************************
                *                      Invalid Option                          *
                ****************************************************************
    
                """]

        print(note[key][value])
        
    def readPath(self):
        self.UserInput(0,self.value)
        self.choice = input(">>> ")

        try:
            self.techProcess = self.processList[int(self.choice)-1]
            self.IPPath = f"/fs078/sd7a/iprepdes/ip_replacement/ip_store/released/{self.techProcess}/compiler/generated"
            self.dirList = os.listdir(self.IPPath)
            
            for IP in range(len(self.dirList)):
                self.IPfullPath = os.path.join(self.IPPath,self.dirList[IP])
                for root, dirs,files,in os.walk(self.IPfullPath):
                    if "XROM" in self.IPfullPath:
                        for file in files:
                            if file.endswith(('.vhe','.bin')):
                                countVhe = sum(1 for i in files if i.endswith(".vhe"))
                                countBin = sum(1 for i in files if i.endswith(".bin"))
                                
                                #files.insert(2,root)
                                if countVhe > 1:
                                    self.RomFullPath = os.path.join(root,file)
                                    #print(self.RomFullPath)
                                    self.vheDir.append(self.RomFullPath[35:])
                                    #self.vheDir.append(self.RomFullPath)
                                print(*self.vheDir,sep="\n", file=open("Vhe_ROM.txt","w"))

                                if countBin > 1:
                                    self.RomFullPath = os.path.join(root,file)
                                    #print(self.RomFullPath)
                                    self.binDir.append(self.RomFullPath[35:])
                                    #self.binDir.append(self.RomFullPath)
                                print(*self.binDir,sep="\n", file=open("Bin_ROM.txt","w"))      

        except:
            self.UserInput(1,self.value)

    def readContent(self):
        with open('Bin_ROM.txt') as f:
            for line in f:
                print(line.strip())
                self.compareBin.append(line.strip())

            #print(self.compareBin)
            #for i in range(len(self.compareBin)):
            #    print(self.compareBin[i])
                    #result = filecmp.cmp(self.compareBin[0],self.compareBin[i],shallow=False)
                    #print(result)

               #head = os.path.split(line)
               #self.compareBin.append(os.path.join(head[0],head[1]))
            #print(self.compareBin[0],self.compareBin[1])

            #result = filecmp.cmp(self.compareBin[0],self.compareBin[1])
            #print(result)
            # for i in range(len(self.compareBin)):                
            #     result = filecmp.cmp(self.compareBin[0],self.compareBin[1],shallow=False)
            #     print(self.compareBin[1])
 
                #print(line.strip()[:180])
            #contents = f.read()
            #print(contents.strip())
            #self.compareBin.append(contents)
        #print(self.compareBin)

        #for self.compareBin in contents:
        #    print({self.compareBin})

        
   
if __name__ == "__main__":
    init = IPSort()
    path = init.readPath()
    read = init.readContent()
