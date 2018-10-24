import json
import csv
import sys
import getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    print('Input file is "', inputfile)
    print('Output file is "', outputfile)

    data_from_file = open(inputfile,'r')
    json_data = json.load(data_from_file)
    data_from_file.close()

    yarn_data = json_data['apps']['app']

    csv_to_file = open(outputfile, 'w', newline = '\n')
    csv_writer = csv.writer(csv_to_file, delimiter=',')
    csv_writer.writerow(["id","name", "state", "startedTime", "finishedTime", "elapsedTime"])

    for yarn_row in yarn_data:
        id = yarn_row['id']
        name = yarn_row['name']
        state = yarn_row['state']
        startedTime : float = yarn_row['startedTime']
        finishedTime : float = yarn_row['finishedTime']
        elapsedTime : int  = yarn_row['elapsedTime']
        csv_writer.writerow([id, name, state, startedTime, finishedTime, elapsedTime])

    csv_to_file.close()

if __name__ == "__main__":
    main(sys.argv[1:])
