import random
import datetime
import time

def get_mogged():
    return 'https://media.tenor.com/LCmsGWpdn9sAAAAM/mogged-williams.gif https://media.tenor.com/dJG0JNTr6FwAAAAM/christian-mogged.gif https://media.tenor.com/di2oxH_FhWsAAAAM/bg.gif'



def Tribe():
    Current_Tribe = ('@here '
                     'Tribe = '
                     '1. <@527829189924093972>   '
                     '2. <@296672049496326144>    '
                     '3. <@821088912868507649>    '
                     '4. <@957701303092531240>    '
                     '5. <@308328540422537217>     '
                     '6. <@960216911696785418>     '
                     '7. <@350704548882677760>     ')

    return Current_Tribe

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'hello there'

    if p_message == 'shush':
        return 'No my life is a movie'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == 'gamble':
        return str(random.randint(1, 200))

    if p_message == 'help':
        return 'The list of commands are as follows: '

    if p_message == 'ping':
        return 'Hey there!'

    if p_message == 'lego city':
        return 'man has fallen into the river in Lego City! Start the new rescue helicopter! Hey! Build the helicopter and off to the rescue. Prepare the lifeline, lower the stretcher, and make the rescue. The new Emergency Collection from Lego City! https://media.tenor.com/QKnxD8q5DToAAAAM/korean-angry-korean.gif'

    if p_message == 'mogged':
        return str(get_mogged())

    if p_message == 'tribe':
        return str(Tribe())

    if p_message == 'need1':
        return '@everyone We have 1 more slot dm/msg for place '

    if p_message == '9999123':
        return '<@924041856134832188> i like pings :) '

    if p_message == 'poll':
        return '@everyone Greetings, esteemed Ark Tribe! As your Alien Boss, I decree that this season, we shall conquer Miami with an otherworldly ferocity!We are the masters of the cosmos, and our dominance is inevitable. Our superior technology and cunning strategies will crush our opponents like the insignificant insects they are.Our tribes unity and strength are the keys to our victory. We will work together like a well-oiled machine, each member playing their unique role in the grand symphony of success.We will not be deterred by the challenges ahead. We will face them head-on, with courage in our hearts and an unyielding determination to win So let us march into battle, Ark Tribe! Let our enemies tremble at the mention of our names. Let Miami know that we have arrived, and we will not leave until we claim victory as our own! For the Ark! For the Cosmos! We shall triumph!'

    if p_message == 'poll2':
        return '@everyone if yes @me and tell me which ais you would like and want via the https://ollama.com/library , in general 2 channel :) Note 10B max for model size'


    return ''  # Return an empty string for any other messages that don't start with !
