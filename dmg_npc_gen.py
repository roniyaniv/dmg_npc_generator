# TODO add default flow of 1 npc in case of no arguments

import sys
import random

appearance = ['Distinctive jewelry: earrings, necklace, circlet, bracelets', 'Piercings', 'Flamboyant or outlandish clothes', 'Formal, clean clothes', 'Ragged, dirty clothes', 'Pronounced scar', 'Missing teeth', 'Missing fingers', 'Unusual eye color (or two different colors)', 'Tattoos', 'Birthmark', 'Unusual skin color', 'Bald', 'Braided beard or hair', 'Unusual hair color', 'Nervous eye twitch', 'Distinctive nose', 'Distinctive posture (crooked or rigid)', 'Exceptionally beautiful', 'Exceptionally ugly']

high_ability = ['Strength - powerful, brawny, strong as an ox', 'Dexterity - lithe, agile, graceful', 'Constitution - hardy, hale, healthy', 'Intelligence - studious, learned, inquisitive', 'Wisdom - perceptive, spiritual, insightful', 'Charisma - persuasive, forceful, born leader']

low_ability = ['Strength - feeble, scrawny', 'Dexterity - clumsy, fumbling', 'Constitution - sickly, pale', 'Intelligence - dim-witted, slow', 'Wisdom - oblivious, absentminded', 'Charisma - dull, boring']

talent = ['Plays a musical instrument','Speaks several languages fluently','Unbelievably lucky','Perfect memory','Great with animals','Great with children','Great at solving puzzles','Great at one game','Great at impersonations','Draws beautifully','Paints beautifully','Sings beautifully','Drinks everyone under the table','Expert carpenter','Expert cook','Expert dart thrower and rock skipper','Expert juggler','Skilled actor and master of disguise','Skilled dancer','Knows thieves\' cant']

mannerism = ['Prone to singing, whistling, or humming quietly','Speaks in rhyme or some other peculiar way','Particularly low or high voice','Slurs words, lisps, or stutters','Enunciates overly clearly','Speaks loudly','Whispers','Uses flowery speech or long words','Frequently uses the wrong word','Uses colorful oaths and exclamations','Makes constant jokes or puns','Prone to predictions of doom','Fidgets','Squints','Stares into the distance','Chews something','Paces','Taps fingers','Bites fingernails','Twirls hair or tugs beard']

trait = ['Argumentative', 'Arrogant', 'Blustering','Rude','Curious', 'Friendly','Honest','Hot tempered','Irritable','Ponderous','Quiet', 'Suspicious']

ideal = {
    "Good": ['Beauty', 'Charity', 'Greater good', 'Life', 'Respect', 'Self-sacrifice'],
    "Evil": ['Domination', 'Greed', 'Might', 'Pain', 'Retribution', 'Slaughter'],
    "Lawful": ['Community', 'Fairness', 'Honor', 'Logic', 'Responsibilty', 'Tradition'],
    "Chaotic": ['Change', 'Creativity','Freedom','Independence','No limits','Whimsy'],
    "Neutral": ['Balance','Knowledge','Live and let live','Moderation','Neutrality','People'],
    "Other": ['Aspiration','Discovery','Glory','Nation','Redemption','Self-knowledge']
}

bond = ['Dedicated to fulfilling a personal life goal','Protective of close family members','Protective of colleagues or compatriots','Loyal to a benefactor, patron, or employer','Captivated by a romantic interest','Drawn to a special place','Protective of a valuable possession','Out for revenge']

flaw_or_secret = ['Forbidden love or susceptibility to romance','Enjoys decadent pleasures','Arrogance','Envies another creature\'s possessions or station','Overpowering greed','Prone to rage','Has a powerful enemy','Specific phobia','Shameful or scandalous history','Secret crime or misdeed','Possession of forbidden lore','Foolhardy bravery']


def generate_npc(amount=1):

    # print('amount = ' + str(amount))    

    for i in range(amount):

        print('\r')
        print("Appearance: " + random.choice(appearance))

        high_ability_selected = random.choice(high_ability)
        low_ability_selected = random.choice(low_ability)

        while low_ability.index(low_ability_selected) == high_ability.index(high_ability_selected):
            low_ability_selected = random.choice(low_ability)

        print("High " + high_ability_selected)
        print("Low " + low_ability_selected)
        print("Talent: " + random.choice(talent))
        print("Mannerism: " + random.choice(mannerism))
        print("Trait: " + random.choice(trait))
        ideal_category = random.choice(list(ideal.keys()))
        print("Ideal: " + random.choice(ideal[ideal_category]) + " (" + ideal_category + ")")
        print("Bond: " + random.choice(bond))
        print("Flaw or Secret: " + random.choice(flaw_or_secret))
        print('\r')
        print("-------------------")

# print("args length = " + str(len(sys.argv)))

if len(sys.argv) == 1:
    generate_npc(1)
else:
    for i in sys.argv[1:]:
        generate_npc(int(i))
