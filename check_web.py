# Import libraries
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import numpy as np
import time 


TOTAL_ITERATIONS = 10
CHECK_INTERVAL = 5 # in seconds


url = 'http://nits.ac.in'
file_name = './log.txt'
text_file = open(file_name, "w")

# Header line
text_file.write("Date, Time, Status, Ping Time (ms), Remarks \n")



for i in range(0,TOTAL_ITERATIONS):
    print (['Checked ',str(i),' time'])
    
    # code goes here
    time.sleep(CHECK_INTERVAL)
    
        
    req = Request(url)
    try:
        current_date = time.strftime("%x")
        current_time = time.strftime("%X")
        response = urlopen(req)
        nf = urlopen(url)
        start = time.time()
        page = nf.read()
        end = time.time()
        nf.close()
        del_time = end - start
        del_time = (np.round(del_time*10000))/10000
        del_time = str (del_time)
        print (['Checking on ',str(current_date),' at time ', str(current_time)])
    except HTTPError as e:
        status = 'Not OK'
        remarks = 'The server couldn\'t fulfill the request with Error code: ' + str(e.code)
        print (remarks)
        status = 'Not OK'
        del_time = 'NA'
        text_file.write("%s,%s,%s,%s,%s\n" %(current_date,current_time,status,del_time,remarks))
    except URLError as e:
        status = 'Not OK'
        remarks = 'We failed to reach a server with Reason: '+ str(e.reason)
        print (remarks)
        status = 'Not OK'
        del_time = 'NA'
        text_file.write("%s,%s,%s,%s,%s\n" %(current_date,current_time,status,del_time,remarks))
    else:
        print ('Website is working fine')
        remarks = 'Website is working fine'
        status = 'OK'
        text_file.write("%s,%s,%s,%s,%s\n" %(current_date,current_time,status,del_time,remarks))
    
    
        
text_file.close()
        
    
    