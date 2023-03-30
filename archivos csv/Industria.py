class industria:
    def __init__(self,index,organizationid,name,website,country,description,founded,industry, numberemployes):
        self.__index=index
        self.__organizationid=organizationid
        self.__name=name
        self.__website=website
        self.__country=country
        self.__decription=description
        self.__founded=founded
        self.__industry=industry
        self.__nemployes=numberemployes
        
    def getAll(self):
        return self.__index+' '+self.__organizationid+' '+self.__name+' '+self.__website+' '+self.__country+' '+self.__decription+' '+self.__founded+' '+self.__industry+' '+self.__nemployes

    def getIndex(self):
        return self.__index
    
    def getOrgaId(self):
        return self.__organizationid
    
    def getName(self):
        return self.__name
    
    def getCountry(self):
        return self.__country
    
    def getNEmplo(self):
        return self.__nemployes