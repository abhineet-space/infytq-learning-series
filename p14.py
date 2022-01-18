from xmlrpc.server import list_public_methods


name = "Abhineet"
print(name.replace('e','E'))
name.upper()
print(name.upper())
print(name.lower())
name.split('i')
print(name)
song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
print(song)
song_words=song.split()
print(song_words)
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)
list=[]
list.append(name)
list.append(name)
print(list)