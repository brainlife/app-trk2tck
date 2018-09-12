#!/usr/bin/env python
import json
import nibabel

with open('config.json') as config_json:
    config = json.load(config_json)

print("loading trk")
trk = nibabel.streamlines.load(config["trk"])
print(trk)

print("saving track.tck")
nibabel.streamlines.save(trk.tractogram, "track.tck")
print("done")
