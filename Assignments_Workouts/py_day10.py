"""#installing modules
#pip list
#Downloading a google file and write into another file
import requests
resp=requests.get("https://www.google.co.in/", verify = False)
print(resp,dir(resp))
print(resp.url)
print(resp.content)
#print(resp.text)

with open('google.html','w')as w_obj:
    w_obj.write(resp.text)
  """ 
import requests

def get_method(url):
    resp= requests.get(url, verify= False)
    if resp.status_code in [200, '200']:
        return(resp.content)

def write_file(filename, data):
    with open(filename,'wb')as w_obj:
        w_obj.write(data)
        return True
    return False

data = get_method("https://en.wikipedia.org/wiki/Python_(programming_language)")
status = write_file("AboutPython.html",data)
if status:
    with open("C://Users//ann//AppData//Local//Programs//Python//Python38-32//Py_Training//AboutPython.html","r") as readObj:
        out=readObj.readlines()
        for lines in out:
            if "<li>" in lines:
                print(lines)
else: 
    print("html file not downloaded")


