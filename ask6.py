#gia na treksei to programma prepei na ektelestei sto cmd 
#h entolh "python -m pip install chuck-norris-python"
from chuck import ChuckNorris
cn = ChuckNorris()
data = cn.random()
print(data.joke)
joke=data.joke
spl=joke.split()


for word in spl:
    if (len(word) > 2):
        print ( (ord(word[0]) + ord(word[-1])) % 3 )
    else:
        print (-1)
