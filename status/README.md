# Stream Status Log


Setup by creating a terminal function like this:

```
stream-status () {
  LOGFILE="$HOME/stream-status.log"
  touch $LOGFILE && echo "$(date +%s) $1" >> $LOGFILE
}
```

Then during the stream update the status by running 
```
stream-status "Working on problem X"
```

Finally, after the stream, parse the log like this:
```
python3 parse-log.py ~/stream-status.log <timestamp-of-stream-start>
```
There are a few extra options to improve the parsing. See the help or the example below.


## Example

My actual setup for a stream looked like this:

Setup:
```
stream-status () {
  curl -s 'http://127.0.0.1:9090/zetatwo/status' --data "status=$1" > /dev/null
  LOGFILE="$HOME/stream-status.log"
  touch $LOGFILE && echo "$(date +%s) $1" >> $LOGFILE
}

ssm-status () {
  stream-status "Säkerhets-SM - $1"
}
```

Parsing:
```
$ python3 parse-log.py ~/stream-status.log 1617357969 --ltrim "Säkerhets-SM - " --nudge -50
0:00:00 Intro
0:15:48 Forensics
0:16:22 Forensics - Datorer AB
0:29:11 Forensics - PDF Padlock
0:37:39 Forensics - Herr Robot
0:50:09 Forensics - Skumt Ljud
1:31:18 Forensics - Anamorfos
1:45:25 Forensics - Mosad Bild
2:09:26 Pwn - Buffertspill
2:43:11 Pwn - Printf i en loop
3:17:36 Reversing - Durins Dörrar
3:20:47 Reversing - Isengård
4:11:22 Reversing - Barad-Dur
4:51:12 Reversing - Kodlås
5:03:23 Reversing - Skum Kod
5:30:30 Reversing - Outro
```
