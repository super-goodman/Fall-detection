import json
import requests
import logging
import threading

API_KEY  = "ei_a86e54bc057311e0e72857f67ca387a62336f07c74e13ada38c7a0274ef38b0d"
projectId = "142816"

headers = {
    "Accept": "application/json",
    "x-api-key": API_KEY
}

def get_sample_len(sampleId):
    url = f'https://studio.edgeimpulse.com/v1/api/{projectId}/raw-data/{sampleId}'
    response = requests.request("GET", url, headers=headers)
    resp =  json.loads(response.text)
    return resp['sample']['totalLengthMs']

def get_segments(sampleId):
    url = f'https://studio.edgeimpulse.com/v1/api/{projectId}/raw-data/{sampleId}/find-segments'
    payload = {
        "shiftSegments": False,
        "segmentLengthMs": 4000
    }
    response = requests.request("POST", url, json=payload, headers=headers)
    return json.loads(response.text)["segments"] 

def crop_sample(sampleId):
    sample_len = get_sample_len(sampleId)
    cropStart  = 200
    cropEnd    = int(sample_len/5)
    payload    = {"cropStart": cropStart, "cropEnd": cropEnd}
    #print(payload)
    url        = f'https://studio.edgeimpulse.com/v1/api/{projectId}/raw-data/{sampleId}/crop'
    response   = requests.request("POST", url, json=payload, headers=headers)
    resp =  json.loads(response.text)
    if resp['success']:
        logging.info(f'Crop: {sampleId}')
    else:
        logging.error(f'Crop: {sampleId} {resp["error"]}')

def segment(tid, ids):
    for sampleId in ids:
        try:
            crop_sample(sampleId)
            segments = get_segments(sampleId)
            
            if len(segments) > 0:
                payload = {"segments": segments}
                url = f'https://studio.edgeimpulse.com/v1/api/{projectId}/raw-data/{sampleId}/segment'
                response = requests.request("POST", url, json=payload, headers=headers)
                resp =  json.loads(response.text)
                if resp['success']:
                    logging.info(f'Segment: {tid} {sampleId}')
                else:
                    logging.error(f'Segment: {tid} {sampleId} {resp["error"]}')
        except Exception as e:
            logging.error(f'Segment: exception {sampleId}')
            continue 

def get_id_list():
    querystring = {"category":"training", "excludeSensors":"true", "labels": '["FALL"]'}
    url = f'https://studio.edgeimpulse.com/v1/api/{projectId}/raw-data'
    response = requests.request("GET", url, headers=headers, params=querystring)

    resp = json.loads(response.text)
    id_list = list(map(lambda s: s["id"], resp["samples"]))

    return id_list
 
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    id_list = get_id_list()
    logging.info('Sample Count: {}'.format(len(id_list)))

    div = 8
    n = int(len(id_list) / div)
    threads = list()

    for i in range(div):
        if i ==  (div - 1):
            ids = id_list[n*i: ]
        else:
            ids = id_list[n*i: n*(i+1)]

        x = threading.Thread(target=segment, args=(i, ids))
        threads.append(x)
        x.start()

    for thread in threads:
        thread.join()

    logging.info("Finished")
