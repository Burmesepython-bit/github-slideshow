str = ('X-DSPAM-Confidence: 0.8475')
ipso = str.find(':')
piece = str[ipso+1:]
print(piece)