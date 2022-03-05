class CsvReader():
    def __init__(
        self,filename: str = None, sep: str = ',', header: bool = False,
        skip_top: int =0, skip_bottom: int =0 
        ) -> None:

        try:
            self.file = open(filename, 'r')
        except FileNotFoundError:
            print("File not found. Check the path of your file.")
            return None
        
        self.columns : list[str] = []
        self.data : list[list] = []
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

        for i,line in enumerate(self.file):
            if i == 0:
                for nb_col,word in enumerate(line.split(sep)):
                    if header == True:
                        self.columns.append(word.replace("\n",""))
                        self.data.append([])
                    else:
                        self.data.append([word.replace("\n","")])
                
            else:
                for j,word in enumerate(line.split(sep)):
                    if j <= nb_col:
                        self.data[j].append(word.replace("\n",""))
                    else:
                        print(f"The file is corrupted at line {i}")
                        return None
        
        self.skip()

    def getData(self) -> list[list]:
        return self.data
    
    def getHeader(self) -> list :
        return self.columns
    
    def skip(self) -> None:
        while self.skip_top > 0:
            for i in range(0,len(self.data)):
                del self.data[i][0]
            self.skip_top = self.skip_top - 1
        
        while self.skip_bottom > 0:
            for i in range(0,len(self.data)):
                del self.data[i][len(self.data[i]) - 1]
            self.skip_bottom = self.skip_bottom - 1
        
    def __enter__(self):
        return self
    
    def __exit__(self) -> None:
        self.file.close()

T = CsvReader("test.csv",header=True,skip_top=1,skip_bottom=1)
print(T.getData(),T.getHeader())