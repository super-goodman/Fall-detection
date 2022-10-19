import json
import time, hmac, hashlib
import glob
import os
import time
from venv import create

HMAC_KEY = "ce9583a7c745646df5e0a8fe0f8f3e4a"

# Empty signature (all zeros). HS256 gives 32 byte signature, and we encode in hex, so we need 64 characters here
emptySignature = ''.join(['0'] * 64)

def get_x_filename(filename):
    m_codes = ['D01', 'D02', 'D03', 'D04', 'D05', 'D06', 'D07', 'D08', 'D09', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19']
    f_codes = ['F01', 'F02', 'F03', 'F04', 'F05', 'F06', 'F07', 'F08', 'F09', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15']
    code = filename.split('_')[0]
    
    label = ''

    if code in m_codes:
        label = 'ADL'

    if code in f_codes:
        label = 'FALL'

    if label == '':
        raise Exception('label not found')

    x_filename = '../data/{}.{}.json'.format(label, os.path.splitext(filename)[0])

    return x_filename 

if __name__ == "__main__":
    files = glob.glob("../SisFall_dataset/*/*.txt")
    CONVERT_G_TO_MS2 = 9.80665

    for index, path in enumerate(files):
        filename = os.path.basename(path)
        values = []
        with open(path) as infile:
            for line in infile:
                line = line.strip()
                if line:
                    row  = line.replace(" ", "") 
                    cols = row.split(',')
                    ax = ((2 * 16) / (2 ** 13)) * float(cols[0]) * CONVERT_G_TO_MS2 
                    ay = ((2 * 16) / (2 ** 13)) * float(cols[1]) * CONVERT_G_TO_MS2
                    az = ((2 * 16) / (2 ** 13)) * float(cols[2]) * CONVERT_G_TO_MS2
                    values.append([ax, ay, az])
        if (len(values) == 0):
            continue
    
        data = {
            "protected": {
                "ver": "v1",
                "alg": "HS256",
                "iat": time.time() # epoch time, seconds since 1970
            },
            "signature": emptySignature,
            "payload": {
                "device_name": "aa:bb:ee:ee:cc:ff",
                "device_type": "generic",
                "interval_ms": 5,
                "sensors": [
                    { "name": "accX", "units": "m/s2" },
                    { "name": "accY", "units": "m/s2" },
                    { "name": "accZ", "units": "m/s2" }
                ],
                "values": values
            }
        }
    
        # encode in JSON
        encoded = json.dumps(data)
    
        # sign message
        signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg = encoded.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()
    
        # set the signature again in the message, and encode again
        data['signature'] = signature
    
        encoded = json.dumps(data)
    
        x_filename = get_x_filename(filename)

        with open(x_filename, 'w') as fout:
            fout.write(encoded)
        
    



