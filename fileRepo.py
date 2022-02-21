class FileRepo():
    
    def exportDataString(self,Ltimes,Lpoints,delim): #
        string = ""
        for i in range (len(Ltimes)):
            string = string  + str(Ltimes[i]) + delim + str(Lpoints[i].getX()) + delim + str(Lpoints[i].getY())+"\n"
        return string
    
    def exportDataToCsv(self,filename,Ltimes,Lpoints,delim):
         nom = ""
         nom = filename + ".csv"
         try:
             f = open(nom,"w")
             try:
                 f.write(self.exportDataString(Ltimes,Lpoints,delim))
             except :
                 print("ne peut pas écrire dans le fichier")
            
         except :
            print("ne peut pas ouvrir/créer le fichier")
         f.close()
