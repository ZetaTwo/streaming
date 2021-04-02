#!/usr/bin/env python3

import time
import argparse
import datetime

parser = argparse.ArgumentParser(description='Parse streaming status log and create TOC')
parser.add_argument('logfile', type=argparse.FileType('r'), help='The logfile of status changes to parse')
parser.add_argument('starttime', default=-1, type=int, nargs='?', help='The timestamp when the stream started. If not provided, first entry in log will be used.')
#parser.add_argument('--format', default='HH:MM:SS', help='The format of the timestamp output') # TODO?
parser.add_argument('--ltrim', default='', help='A prefix to remove from every log entry')
parser.add_argument('--nudge', default=0, type=int, help='A small delta to apply to the timestamps')
args = parser.parse_args()

with args.logfile:
    for line in args.logfile:
        ts_str, status = line.strip().split(' ', 1)
        ts = int(ts_str)
        status = status[len(args.ltrim):] if status.startswith(args.ltrim) else status
        if args.starttime == -1:
            args.starttime = ts
        ts_delta = max(0, ts - args.starttime + args.nudge)
        ts_delta = datetime.timedelta(seconds=ts_delta)
        print(f'{ts_delta} {status}')
