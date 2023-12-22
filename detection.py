import sys
import numpy as np
from scapy.all import PcapNgReader

def read_pcapng(file_path):
    hm = {}
    size = {}
    try:
        with PcapNgReader(file_path) as pcap_reader:
            for packet in pcap_reader:
                packet_size = len(packet)
                
                ts = int(packet.time)
                if ts not in hm:
                    size[ts] = 0
                    hm[ts] = 0
                
                size[ts] += packet_size
                hm[ts] += 1

    except Exception as e:
        print(f"Error reading pcapng file: {e}")

    return hm, size

if len(sys.argv) < 2:
    print("Need a pcapng file to check. Provide the full path")
    sys.exit(1)

hm, size = read_pcapng(sys.argv[1])
pn, bw = [*hm.values()], [*size.values()]
th = 3 * np.mean(np.float32(bw) / np.float32(pn))

if np.std(np.array(bw)) < th:
    print("Traffic Shaping detected!") 
else:
    print("NO Traffic Shaping detected!")
