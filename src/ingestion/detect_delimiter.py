import csv

def detect_delimiter(path, enc):
    with open(path, "r", encoding=enc, errors="replace") as f:
        sep = csv.Sniffer().sniff(f.read(5000)).delimiter
        return sep