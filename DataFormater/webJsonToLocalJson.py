from fileinput import close
import json
import time,hmac, hashlib


HMAC_KEY = "ce9583a7c745646df5e0a8fe0f8f3e4a"
emptySignature = ''.join(['0'] * 64)


# read json
f = open("123.json", "r")
dataj = f.read()

data = json.loads(dataj)
data = data['payload']
data = data['values']
f.close()
print(len(data))

#change to .txt
f = open("data.txt", "w")
i = 1200
dataList = '['
for j  in range(800):
  i = i + 1
  str1 =  str(data[i])
  str1 = str1.replace('[','')
  str1 = str1.replace(']','')
  if i < 2000:
    str1 += ','
    str1 += '\n'
  f.writelines(str1)
f.close()

values = []
with open("data.txt") as infile:
    for line in infile:
        line = line.strip()
        if line:
            row  = line.replace(" ", "") 
            cols = row.split(',')
            ax = float(cols[0])
            ay = float(cols[1])
            az = float(cols[2])
            values.append([ax, ay, az])

dataj = {
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
print(dataj)

encoded = json.dumps(dataj)
    
# sign message
signature = hmac.new(bytes(HMAC_KEY, 'utf-8'), msg = encoded.encode('utf-8'), digestmod = hashlib.sha256).hexdigest()

# set the signature again in the message, and encode again
dataj['signature'] = signature

encoded = json.dumps(dataj)


with open('uploadJson.json', 'w') as fout:
    fout.write(encoded)