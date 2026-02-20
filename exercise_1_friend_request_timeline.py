def Count_Uppercase(phrase):
    uppercase_count = 0
    for i in range(len(phrase)):
        if phrase[i] >= 'A' and phrase[i] <= 'Z':
            uppercase_count = uppercase_count + 1
    return uppercase_count

def Count_Letter(phrase):
    letter_count = 0
    for i in range(len(phrase)):
        if (phrase[i] >= 'A' and phrase[i] <= 'Z') or (phrase[i] >= 'a' and phrase[i] <= 'z'):
            letter_count = letter_count + 1
    return letter_count

def Count_Punctuation(phrase):
    punctuation_count = 0
    for i in range(len(phrase)):
        if phrase[i] == '!' or phrase[i] == '?':
            punctuation_count = punctuation_count + 1
    return punctuation_count

def Check_Repeated(phrase):
    previous = ''
    repetition = 1
    for i in range(len(phrase)):
        if phrase[i] == previous:
            repetition = repetition + 1
            if repetition > 3:
                return True 
        else:
            repetition = 1
        previous = phrase[i]
    return False


def Analyse_Messaging(message):
    uppercase = Count_Uppercase(message)
    letter = Count_Letter(message)
    punctuation = Count_Punctuation(message)
    potential_spam = Check_Repeated(message)

    if letter > 0:
        caps_ratio = uppercase / letter
    else:
        caps_ratio = 0
    
    if caps_ratio >= 0.6 or punctuation >= 5:
        status = "AGGRESSIVE"
    elif caps_ratio >= 0.3 or punctuation >= 3:
        status = "URGENT"
    else:
        status = "CALM"

    print(f" Statut : {status}")
    if potential_spam:
        print("ALERTE : SPAM")
    
    return status

test_cases = [
    "Hey, want to connect?",
    "PLEASE ACCEPT MY REQUEST!!!",
    "Are you free? I need to talk!!!",
    "heyyyyy, noooo",
    "", 
    "12345 !!!", 
    "ABCdef", 
    "hi!!!!!", 
    "aaabbb", 
    "aaaa", 
    "PLEASE!!!"
]

for tc in test_cases:
    print(f"Message: '{tc}'")
    Analyse_Messaging(tc)
    print()