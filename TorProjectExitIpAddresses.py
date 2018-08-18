import requests


v_objResponse = requests.post('https://check.torproject.org/exit-addresses')
v_fTempFile = open("tempList.txt", "w+")
v_fExtractedListOfIps = open("torIpList.txt", "w+")


v_fTempFile.write(v_objResponse.text)
v_fTempFile.close()

with open("tempList.txt") as INF:
    for v_sLine in INF:
        if v_sLine.startswith('ExitAddress'):
            v_fExtractedListOfIps.write(v_sLine.split()[1] + "\n")
            
v_fExtractedListOfIps.close()
