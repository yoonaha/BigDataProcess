import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

genreDic = {}

with open(input_file, 'r', encoding = 'utf-8') as fp:
    data = fp.read()

    rows = data.split("\n")
    for row in rows:
        fields = row.split('::')
        elements = (fields[0], fields[1], fields[2])
        genres = fields[2].split('|')

        for genre in genres:
            if genre in genreDic:
                genreDic[genre] += 1
            else:
                genreDic[genre] = 1
        

with open(output_file, 'w', encoding = 'utf-8') as output_file:
    for g, c in genreDic.items():
        output_file.write(f"{g} {c}\n")