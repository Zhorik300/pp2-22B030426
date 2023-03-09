life = ['Money', 'time', 'work']
with open(r'C.txt', 'w') as fp:
    for item in life:
        
        fp.write("%s\n" % item)
    print('Done')