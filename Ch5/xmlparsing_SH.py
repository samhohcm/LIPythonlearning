# 
# Example file for parsing and processing XML
# keep it in memory, work on the dom

import xml.dom.minidom


def main():
  # use the parse() function to load and parse an XML file
  doc = xml.dom.minidom.parse("Ch5\samplexml.xml")  # creates the dom

  
  # print out the document node and the name of the first child tag
  print(doc.nodeName)
  print(doc.firstChild.tagName)
  
  # get a list of XML tags from the document and print each one
  skills = doc.getElementsByTagName("skill")
  print("%d skills: " %skills.length)
  for skill in skills:
      print(skill.getAttribute("name"))  #can see in the xml document


    
  # create a new XML tag and add it into the document
  newSkill = doc.createElement("skill")
  newSkill.setAttribute("name", "jQuery")
  doc.firstChild.appendChild(newSkill)
  
  skills = doc.getElementsByTagName("skill")
  print("%d skills: " %skills.length)
  for skill in skills:
      print(skill.getAttribute("name"))  #can see in the xml document

if __name__ == "__main__":
  main();

