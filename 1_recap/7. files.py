# open an existing file
data_file = open('data/data.csv', 'r')




# reading data
print data_file.readline()
print type(data_file.readline())




# read all lines
# print data.readlines()




# process the data
for line in data_file.readlines():
    print line

    print line.split(',')


    print line.rstrip('\n').split(',')

    data = line.rstrip('\n').split(',')

print data

# close the file when done
data_file.close()


# writing data
output_file = open('data/processed.txt', 'w')

output_file.write('Hello, world!')
output_file.close()




# NOTE Reading and writing data can also be done as follows:
# Reading:
with open('data/data.csv', 'r') as f:
    print f.readline()

# Writing:
with open('data/processed.txt', 'w') as f:
    f.write('Hello, world!')
# This is generally considered the preferred way,
# since it guarantees the file get closed.