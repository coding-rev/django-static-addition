# Creating a class for counting number of lines of a file
class FileLinesCount:
    def __init__(self, path):
        self.path = path
        
    def getNumber(self):
        # Getting number of lines in the file
        with open(self.path,'r') as htmlFile:
            numberOfLines = 0
            for line in htmlFile:
                numberOfLines +=1
            return numberOfLines
        
        

class StaticProjectLogic:
    def logics(self, file_path):
        # Taking users html file to be edited
        with open(file_path,'r') as htmlFile:
            # Getting total lines from the filelinescount class
            totalLines = FileLinesCount(file_path).getNumber()
            # Creating an edited file for the user 
            with open('results.html', 'w') as resultFile:
                #Forloop for reading and writing from old to new file respectively
                count=1
                resultFile.write("{% load static %} \n")
                while count <= totalLines:
                    # Reading and writing
                    line = htmlFile.readline()
                    # ====================================
                    # I - DEALING WITH HREF AND EXTENSIONS
                    # ====================================
                    # Detecting
                    # 1. href=" and .css
                    if "href=\"" and ".css" in line:
                        line = line.replace("href=\"", "href=\"{% static '")
                        line = line.replace(".css", ".css' %}")
                        resultFile.write(line)


                    # ====================================
                    # II - DEALING WITH SRC AND EXTENTIONS
                    # ====================================
                    # Detecting
                    # 1. src=" and .js
                    elif "src=\"" and ".js" in line:
                        line = line.replace("src=\"", "src=\"{% static '")
                        line = line.replace(".js", ".js' %}")
                        resultFile.write(line)

                    # Detecting
                    # 2. src=" and .jpg
                    elif "src=\"" and ".jpg" in line:
                        line = line.replace("src=\"", "src=\"{% static '")
                        line = line.replace(".jpg", ".jpg' %}")
                        resultFile.write(line)

                    # Detecting
                    # 3. src=" and .png
                    elif "src=\"" and ".png" in line:
                        line = line.replace("src=\"", "src=\"{% static '")
                        line = line.replace(".png", ".png' %}")
                        resultFile.write(line)

                                                   
                    else:
                        resultFile.write(line)

                    # Move to next line
                    count += 1
                # Done
                return "201 CREATED"
