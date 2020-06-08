# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

metacount = 0

class MyHTMLParser(HTMLParser):   #MyHTMLParser subclass
    def handle_comment(self, data):
        # when parser comes across comment, will call handle_comment
        # pass the text data
        print("Encountered comment: ", data)
        pos = self.getpos() # this function comes back with line number and character postn
        print("\tAt line: ", pos[0], " position ", pos[1])
    
    def handle_starttag(self, tag, attrs):
        # gets called when the closing angle bracket of an opening tag is reached i.e. at the end of <title>
        # some tags have attributes in them, which will be passed in attrs 
        global metacount
        if tag == 'meta':
            metacount += 1
        print("Encountered tag: ", tag)
        pos = self.getpos() # this function comes back with line number and character postn
        print("\tAt line: ", pos[0], " position ", pos[1])
        
        if attrs.__len__() > 0:  #length property
            print("\tAttributes")
            for a in attrs:
                print("\t", a[0], "=", a[1])   # a[0] is name, a[1] is value

    def handle_endtag(self, tag):
        print("Encountered tag: ", tag)
        pos = self.getpos() # this function comes back with line number and character postn
        print("\tAt line: ", pos[0], " position ", pos[1])


    def handle_data(self, data):
        if data.isspace():
          return
        print("Encountered data: ", data)  #want to skip over white space lines
        pos = self.getpos() # this function comes back with line number and character postn
        print("\tAt line: ", pos[0], " position ", pos[1])

    # feed()
    #take HTML and run line by line, each time it encounters specific kind of data
    # in the HTML like comments or tags, it will call functions that you 
    # override in subclass  


def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f = open("Ch5\samplehtml.html")
  if f.mode == 'r':
      contents = f.read()
      parser.feed(contents)  #pass the string that reps the HTML
      
  print("Meta tags found: " + str(metacount))

if __name__ == "__main__":
  main()
  