CSC 321 Final ....

The script I used to capture all the differnt files on different nodes was ..
# tcpdump -i eth0 -w wuclient.py.pcap
After completing all pcap files, I used this script to merge all pcap files through Wireshark
# mergecap -w full-take.pcap wuserver.pcap wuclient.pcap taskvent.pcap taskwork.pcap tasksink.pcap
 I used this script to seperate pcap files to weather.pcap 
# tcpdump -n -r full-take.pcap port 5556 -w weather.pcap:
Secondly, I used this script to seperate pcap files to task.pcap
# tcpdump -n -r full-take.pcap port 5557 or port 5558 -w task.pcap
A few pointers I documented throughout this project to help me as well was
# wuclient.py is on node00
# wuserver.py is ran on node00 but connects to node01
# taskwork.py is reciever node00 and server node02
# tasksink is ran on node02
# taskvent is ran on node00
# taskwork is ran on node01
