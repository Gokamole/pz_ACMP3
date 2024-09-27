input_data = open('input.txt', 'r')
data = input_data.read ()

data = data.split()
a = int(data[0])
b = int(data[1])
c = int(a + b - 1)
a1 = str(c - a)
b1 = str(c - b)
output_data = open ('output.txt', 'w')
output_data.write(a1, b1)

input_data.close()
output_data.close()