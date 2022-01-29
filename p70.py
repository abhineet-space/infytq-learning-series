'''Write a python function to generate and return the list of all possible sentences created from the given lists of Subject, Verb and Object.

Note: The sentence should contain only one subject, verb and object each.

Sample Input
::::::::::
Expected Output

subjects=["I", "You"]
verbs=["Play", "Love"]
objects=["Hockey","Football"]
:::::::::::
I Play Hockey
I Play Football
I Love Hockey
I Love Football
You Play Hockey
You Play Football
You Love Hockey
You Love Football

'''

#lex_auth_0127136011356405761166

def generate_sentences(subjects,verbs,objects):
	#start writing your code here
    sentence_list = []
    for i in subjects:
        for j in verbs:
            for k in objects:
                sentence_list.append(i+" "+j+" "+k)
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))