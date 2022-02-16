class FileRepo():
    
    def exportDataString(self,Ltimes,Lpoints,delim): #
        string = ""
        for i in range (len(Ltimes)):
            string = string  + str(Ltimes[i]) + delim + str(Lpoints[i].getX()) + delim + str(Lpoints[i].getY())+"\n"
        return string
print("test")

    
