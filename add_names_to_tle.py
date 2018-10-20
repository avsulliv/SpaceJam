f = open("data/sample_tles_master.txt","r")
text = f.read()
result = open("result.txt","w")
all_lines = text.split("\n")
for index, line in enumerate(all_lines):
    if index%2==0:
        name = line.split()[1]
        line = name+"\n"+line
    result.write(line+"\n")
result.close()