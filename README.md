# <h2> <b> Exfiltrating data via GET (http(s)) </b></h2>

DISCLAIMER!
Educational purposes only. 
Exfiltrating and leaking not authorized data may suffer law and consequences is at your own risk. 

Bypass your DLP protection sending data split in base64 via GET URI Path or Inserting into headers. 
Server side will remount the file keeping the same as original

CLIENT SIDE: 

Powershell (tested with Linux too under Powershell core) 


SERVER SIDE:

Python (Simple HTTPServer)


<b>How do I Prevent that?</b>

There is no silver bullet, since GET is widely used and many different parameters and applications using many strings around.

1) Deep packet inspection your navigation and proxy traffic, mirroring the traffic and creating anomaly rules. 
2) Collect powershell logs. Monitor your endpoints and avoid permitting executing powershell stuff (if is there no legitimate reason for that.)
3) Netflow based solutions also user behaviour analysis for unusual transfer data. 

This code was produced using python 3.6.7. <br>
