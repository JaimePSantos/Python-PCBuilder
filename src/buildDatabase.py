from pcpartpicker import API

class DatabaseBuilder:
    fileName = ""

    def __init__(self,fileName):
        self.fileName = fileName
        self.api = API("es")
        
    def partData(self,part):
        partList = []
        partInfo = ""
        partData = self.api.retrieve(part)
        for data in partData.values():
            for component in data:
                partInfo +=  part + "," + component.brand + "," + component.model+","+str(component.price.amount)+"\n"
                partList.append(partInfo)
                partInfo = ""
        return partList 

    def buildFile(self):
        cpuList = self.partData("cpu")
        gpuList = self.partData("video-card")
        print(self.api.supported_parts)
        try:
            with open(self.fileName,"w+") as f:
                f.write("#\tProcessor\t#\n\n")
                for cpu in cpuList:
                    f.write(cpu)
                f.write("\n#\tGraphicsCard\t#\n\n")
                for gpu in gpuList:
                    f.write(gpu)
                f.close()
        except:
            print("%s could not be found."%fileName)


   # api = API()
   # cpu_data = api.retrieve("cpu")
   # #all_data = api.retrieve_all()
   # for data in cpu_data.values():
   #     for cpus in data:
   #         print(type(cpus))
