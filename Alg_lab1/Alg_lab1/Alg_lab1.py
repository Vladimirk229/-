from random import randint
import string

def GenerateFile(size, name):
    print("File creation...")
    f=open(name, 'w')
    for i in range(size):
        f.write(str(randint(1,100)))
        f.write('\n')
        print(i)
    f.close()
    print("File created")

def CleanFile(filename):
    f=open(filename, 'w+')
    f.seek(0)
    f.close()

def Split(startfile, file1, file2, splitsize):
    a=open('test.txt', 'r')
    b=open('b.txt', 'w')
    c=open('c.txt', 'w')
    i=0
    j=0
    for line in a:
        if j==0:
            b.write(line)
        else:
            c.write(line)
        i=i+1
        if i==splitsize:
            i=0
            if j==0:
                j=1
            else:
                j=0
    a.close()
    b.close()
    c.close()

def Merge(file1, file2, mergefile, iterations, max):
    b=open(file1, 'r')
    c=open(file2, 'r')
    a=open(mergefile, 'w')
    for i in range(iterations):
        count_b=0
        count_c=0
        bufx=b.readline()
        bufx=bufx.rstrip('\n')
        x=int(bufx)
        bufy=c.readline()
        bufy=bufy.rstrip('\n')
        y=int(bufy)
        while count_b<max and count_c<max:
            if x>y:
                a.write(str(y))
                a.write('\n')
                if count_c<(max-1):
                    bufy=c.readline()
                    bufy=bufy.rstrip('\n')
                    y=int(bufy)
                count_c=count_c+1
            else:
                a.write(str(x))
                a.write('\n')
                if count_b<(max-1):
                    bufx=b.readline()
                    bufx=bufx.rstrip('\n')
                    x=int(bufx)
                count_b=count_b+1
        while count_c<max:
            a.write(str(y))
            a.write('\n')
            if count_c<(max-1):
                bufy=c.readline()
                bufy=bufy.rstrip('\n')
                y=int(bufy)
            count_c=count_c+1
        while count_b<max:
            a.write(str(x))
            a.write('\n')
            if count_b<(max-1):
                bufx=b.readline()
                bufx=bufx.rstrip('\n')
                x=int(bufx)
            count_b=count_b+1
    b.close()
    c.close()
    a.close()

#=================================================
size=4194304
iterations=size//2
max=1
GenerateFile(size,'test.txt')
while max<size:
    CleanFile('b.txt')
    CleanFile('c.txt')
    Split('test.txt', 'b.txt', 'c.txt', max)
    CleanFile('test.txt')
    Merge('b.txt', 'c.txt', 'test.txt', iterations, max)
    iterations=iterations//2
    max=max*2

