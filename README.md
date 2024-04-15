# decode_morse
This program is a port of PD0WM's [nn-morse](https://github.com/pd0wm/nn-morse) to the Raspberry Pi 4.
It uses [onnxruntime provided by nknytk](https://github.com/nknytk/built-onnxruntime-for-raspberrypi-linux) and runs on the Raspberry Pi OS (32bit bullseye).

The Morse code pitch frequecy range and symbols used were retrained to work with SatNOGS observations.
The results of real data [#928942](https://network.satnogs.org/observations/9284942/) are shown below.

```
$ time python3 decode_morse.py 9284942.ogg 
CHNOLOG 3TOKYO METROPOLITAN COLLEGEOFINDUSTRIALTECHNOLOGY 3 TOKYO METROPOLITNCOLLEGEOFINDUSTRIALTECHNOLOGY 3TEI M METROPOLITANCOLLEGEOFINDUSTRIAL TECHN   H 3TOKYO METROPOLITANCOLLEGEOFIN

real	0m34.087s
user	0m39.695s
sys	0m7.896s
```
