import re
from icecream import ic


def get_letter_from_sentence(sentences, number_set):
    key_letter = []
    for idx, i in enumerate(sentences):
        try:
            sentence_words = i.strip().split(" ")
            which_word = sentence_words[number_set[idx]]
            key_letter.append(which_word[0])  # default = 0
        except:
            key_letter.append("_")
    return "".join(key_letter)


def get_letter_from_word(words, number_set):
    key_letter = []
    for idx, i in enumerate(words):
        try:
            char = words[idx][number_set[idx]]
            key_letter.append(char)
        except:
            key_letter.append("_")
    return "".join(key_letter)


def rotate_number_set(number_set, i):
    return number_set[i:] + number_set[:i]


def reverse_number_set(number_set):
    return [i for i in reversed(number_set)]


texts = {
    "enigma2_chap3": '''No one will forget the day it happened…
Ringing so immense you could not hear glass shattering across the city. A white-hot flash so severe covering your eyes was not enough to reduce the burn.
Complete sensory overload—so overpowering, it felt as though I had been transported to some blank void where nothing existed. Not even my own thoughts. Empty chaos.
I remember thinking, “This must be hell” but then… the ringing stopped.
And I saw what hell really looked like.
The screams.
Who you were or who you knew was meaningless. At that moment of dread all sense of compassion was lost. The weak were trampled into the ground beneath the shoes of those who could still stand. People scurried like animals—rats, chucking each other aside clawing at the entrance to that godforsaken bunker desperate for the salvation that awaited inside. That last ray of hope glistening in doom.
Self-preservation was all that mattered.
I am not proud of what I had to do to get into that filthy hovel we called our ‘sanctuary’, but I’d be lying if I said I wouldn’t do it again.
Far off in the distance, a giant dome shield reflected sun rays our way—The Utopion. It lay tranquil against the foreground of mayhem surrounding our streets, completely unfazed as it always had been towards the suffering of our people.
I wish I saved myself from watching what happened next—to bathe still in that blissful ignorance…that unknowing peace. It was inevitable, I guess…our undoing, our downfall. I suppose to them we were only sub-human. Inferior. A stain of the imperfect past waiting to be cleansed from the gene pool of the future. A crack in the cog of evolution. A defect.
The Bridged, that’s how they saw us.
“Look! It’s moving!” —a frightened shriek from the corner. I redirected my gaze towards the voice, then eyed where its speaker was pointing.
My heart stopped.
The Utopion Dome had opened for the first time…ever.
In that instance, I knew what was coming. Total annihilation. Absolute. Destruction. I witnessed the entire scope of civilization as I knew it, the one I called home, rendered completely decimated without mercy of a second thought.
I saw it. I felt it. It was…evil.
That day ended in pain—agony, torture, loss…I thought it was over, all of it. Everything.
It wasn’t. Our suffering had only just begun.''',
    "enigma2text": '''Here lies the Holy Enigma 2.0. The highly anticipated sequel to the original Holy Enigma that some of you may be unpleasantly familiar with. The original Enigma lies here if you have not yet experienced it. If you wish to undertake the new challenge we wish you luck:
The God’s horrifying presence still remains unexplained. They are trying to communicate with you. Each victory is guiding you one step forward towards understanding these terrifying beings and The Fracture.
An Army of 6,666 demented cross-dimentional entities hunting mercilessly. They are searching ruthlessly for something or someone. That is clear. Why? We do not know.
Supersymmetry was just a theory. That was what they said. After the incident the data was manipulated and nullified to the public. No one could know what they saw. He knew that each particle in our universe had a partner somewhere.. He just needed to see it himself. To confirm everything his Father had experienced. To see them.
''',
    "enigma2text_short": '''The God’s horrifying presence still remains unexplained. They are trying to communicate with you. Each victory is guiding you one step forward towards understanding these terrifying beings and The Fracture. An Army of 6,666 demented cross-dimentional entities hunting mercilessly. They are searching ruthlessly for something or someone. That is clear. Why? We do not know. Supersymmetry was just a theory. That was what they said. After the incident the data was manipulated and nullified to the public. No one could know what they saw. He knew that each particle in our universe had a partner somewhere.. He just needed to see it himself. To confirm everything his Father had experienced. To see them.''',
    "enigma2text_short_tweaked": '''The God’s horrifying presence still remains unexplained. They are trying to communicate with you. Each victory is guiding you one step forward towards understanding these terrifying beings and The Fracture. An Army of 6,666 demented cross-dimentional entities hunting mercilessly. They are searching ruthlessly for something or someone. That is clear. Why, we do not know. Supersymmetry was just a theory. That was what they said. After the incident the data was manipulated and nullified to the public. No one could know what they saw. He knew that each particle in our universe had a partner somewhere,  he just needed to see it himself. To confirm everything his Father had experienced, to see them.'''
    }

numbers = {"set_circle": [11, 6, 10, 7, 12, 4, 13, 3, 8, 1, 9, 5, 2],
           "set_inthecircle": [4, 6, 2, 3, 5],
           "set_red": [4, 1, 8, 1, 6, 2],
           "set_red_2": [4, 18, 16, 2],
           "set_enigma1": [4, 6, 2, 3, 5, 1, 4, 6, 0, 5, 3, 5, 2],
           "set_enigma1pluscircle": [15, 12, 12, 10, 17, 5, 17, 9, 8, 6, 12, 10, 4],
           "rando1": [4, 1, 8, 1, 6, 2, 3, 5, 1, 8, 1, 4],
           "rando2": [4, 1, 8, 1, 8, 8, 1, 8, 1, 4]}


for k, v in texts.items():
    #  texts to skip
    if k in ["enigma2_chap3", "enigma2text"]:
        continue
    sentences = re.split('\? |\. |\n', v.strip())
    words = v.split()
    ic(k, len(sentences), len(words))
    for k2, v2 in numbers.items():
        ic(k2, v2)
        for i in range(len(v2)):
            rot_num = rotate_number_set(v2, i)
            #ic(numbers)
            ic(get_letter_from_sentence(sentences, rot_num))
        for i in range(len(v2)):
            rot_num = rotate_number_set(v2, i)
            numbers_rev = reverse_number_set(rot_num)
            #ic(numbers)
            ic(get_letter_from_sentence(sentences, numbers_rev))
    for k3, v3 in numbers.items():
        continue
        for i in range(len(v3)):
            rot_num = rotate_number_set(v3, i)
            #ic(numbers)
            ic(get_letter_from_word(words, rot_num))
        for i in range(len(v3)):
            rot_num = rotate_number_set(v3, i)
            rot_rev_num = reverse_number_set(rot_num)
            #ic(numbers)
            ic(get_letter_from_word(words, rot_rev_num))





