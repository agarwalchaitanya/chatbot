import string
import re
import random

class eliza:
  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
    self.values = list(map(lambda x:x[1],gPats))

  def translate(self,str,dict):
    words = str.lower().split()
    keys = dict.keys();
    for i in range(0,len(words)):
      if words[i] in keys:
        words[i] = dict[words[i]]
    return ' '.join(words)

  def respond(self,str):
    # find a match among keys
    for i in range(0, len(self.keys)):
      match = self.keys[i].match(str)
      if match:
        # found a match ... stuff with corresponding value
        # chosen randomly from among the available options
        resp = random.choice(self.values[i])
        # we've got a response... stuff in reflected text where indicated
        pos = resp.find('%')
        while pos > -1:
          num = int(resp[pos+1:pos+2])
          resp = resp[:pos] + \
            self.translate(match.group(num),gReflections) + \
            resp[pos+2:]
          pos = resp.find('%')
        # fix munged punctuation at the end
        if resp[-2:] == '?.': resp = resp[:-2] + '.'
        if resp[-2:] == '??': resp = resp[:-2] + '?'
        return resp

gReflections = {
  "am"   : "are",
  "was"  : "were",
  "मैं"    : "आप ",
  "i'd"  : "you would",
  "मेरे पास"  : "आपके पास",
  "i'll"  : "you will",
  "मेरा"  : "आपका",
  "are"  : "am",
  "you've": "I have",
  "you'll": "I will",
  "your"  : "my",
  "आपका"  : "मेरा",
  "you"  : "me",
  "मुझे"  : "आपको"
}

gPats = [
  [r'मुझे (.*) चाहिए',
  [  "आपको %1 क्यों चाहिए ?",
    "क्या आपको %1 से मदद मिलेगी??",
    "क्या आपको यकीन है आपको %1 चाहिए??"]],

  [r'Why don\'?t you ([^\?]*)\??',
  [  "Do you really think I don't %1?",
    "Perhaps eventually I will %1.",
    "Do you really want me to %1?"]],

  [r'Why can\'?t I ([^\?]*)\??',
  [  "Do you think you should be able to %1?",
    "If you could %1, what would you do?",
    "I don't know -- why can't you %1?",
    "Have you really tried?"]],

  [r'I can\'?t (.*)',
  [  "How do you know you can't %1?",
    "Perhaps you could %1 if you tried.",
    "What would it take for you to %1?"]],

  [r'में (.*) हूँ',
  [  "क्या आप मेरे पास आये क्यूंकि आप %1 हो??",
    "आप कितने टाइम से %1 हो??",
    "आप को कैसा लगता है की आप (.*) हो??"]],

  [r'I\'?m (.*)',
  [  "How does being %1 make you feel?",
    "Do you enjoy being %1?",
    "Why do you tell me you're %1?",
    "Why do you think you're %1?"]],

  [r'क्या आप ([^\?]*) हो\??',
  [  "क्या फरक पड़ता है की मैं %1 हूँ?",
    "क्या आपको बेहतर लगेगा की मैं %1 ना हूँ?",
    "मशायद आपको लगता है मैं %1 हूँ।",
    "मैं शायद %1 हूँ। आपको क्या लगता है?"]],

  [r'What (.*)',
  [  "Why do you ask?",
    "How would an answer to that help you?",
    "What do you think?"]],

  [r'How (.*)',
  [  "How do you suppose?",
    "Perhaps you can answer your own question.",
    "What is it you're really asking?"]],

  [r'क्यूंकि (.*)',
  [  "क्या यह असली कारन है %1?",
    "और क्या कारन आते है आपके दिमाग में?",
    "क्या यह किसी और पे भी लागू होता है?",
    "अगर %1, तो और क्या सच है?"]],

  [r'(.*) sorry (.*)',
  [  "There are many times when no apology is needed.",
    "What feelings do you have when you apologize?"]],

  [r'नमस्ते(.*)',
  [  "नमस्ते में खुश हूँ की आप आये।",
    "नमस्ते, आज आप कैसे हो?"]],

  [r'I think (.*)',
  [  "Do you doubt %1?",
    "Do you really think so?",
    "But you're not sure %1?"]],

  [r'(.*) friend (.*)',
  [  "Tell me more about your friends.",
    "When you think of a friend, what comes to mind?",
    "Why don't you tell me about a childhood friend?"]],

  [r'हाँ',
  [  "आप काफी विशवास से बोल रहे हो।",
    "ठीक है। पर इस बारे में क्या आप और बता सकते है?"]],

  [r'(.*) computer(.*)',
  [  "Are you really talking about me?",
    "Does it seem strange to talk to a computer?",
    "How do computers make you feel?",
    "Do you feel threatened by computers?"]],

  [r'Is it (.*)',
  [  "Do you think it is %1?",
    "Perhaps it's %1 -- what do you think?",
    "If it were %1, what would you do?",
    "It could well be that %1."]],

  [r'It is (.*)',
  [  "You seem very certain.",
    "If I told you that it probably isn't %1, what would you feel?"]],

  [r'Can you ([^\?]*)\??',
  [  "What makes you think I can't %1?",
    "If I could %1, then what?",
    "Why do you ask if I can %1?"]],

  [r'Can I ([^\?]*)\??',
  [  "Perhaps you don't want to %1.",
    "Do you want to be able to %1?",
    "If you could %1, would you?"]],

  [r'You are (.*)',
  [  "Why do you think I am %1?",
    "Does it please you to think that I'm %1?",
    "Perhaps you would like me to be %1.",
    "Perhaps you're really talking about yourself?"]],

  [r'You\'?re (.*)',
  [  "Why do you say I am %1?",
    "Why do you think I am %1?",
    "Are we talking about you, or me?"]],

  [r'I don\'?t (.*)',
  [  "Don't you really %1?",
    "Why don't you %1?",
    "Do you want to %1?"]],

  [r'I feel (.*)',
  [  "Good, tell me more about these feelings.",
    "Do you often feel %1?",
    "When do you usually feel %1?",
    "When you feel %1, what do you do?"]],

  [r'I have (.*)',
  [  "Why do you tell me that you've %1?",
    "Have you really %1?",
    "Now that you have %1, what will you do next?"]],

  [r'I would (.*)',
  [  "Could you explain why you would %1?",
    "Why would you %1?",
    "Who else knows that you would %1?"]],

  [r'Is there (.*)',
  [  "Do you think there is %1?",
    "It's likely that there is %1.",
    "Would you like there to be %1?"]],

  [r'मेरा|मेरी (.*)',
  [  "अच्छा, आपका %1.",
    "आप ऐसा क्यों कह रहे की आपका %1?"]],

  [r'You (.*)',
  [  "We should be discussing you, not me.",
    "Why do you say that about me?",
    "Why do you care whether I %1?"]],

  [r'Why (.*)',
  [  "Why don't you tell me the reason why %1?",
    "Why do you think %1?" ]],

  [r'मुझे (.*) चाहिए',
  [  "आपके लिए %1 का क्या महत्व है??",
    "आपको %1 क्यों चाहिए??",
    "अगर आपको मिलेगा तो आप क्या करोगे?"]],

  [r'(.*) mother(.*)',
  [  "Tell me more about your mother.",
    "What was your relationship with your mother like?",
    "How do you feel about your mother?",
    "How does this relate to your feelings today?",
    "Good family relations are important."]],

  [r'(.*) father(.*)',
  [  "Tell me more about your father.",
    "How did your father make you feel?",
    "How do you feel about your father?",
    "Does your relationship with your father relate to your feelings today?",
    "Do you have trouble showing affection with your family?"]],

  [r'(.*) child(.*)',
  [  "Did you have close friends as a child?",
    "What is your favorite childhood memory?",
    "Do you remember any dreams or nightmares from childhood?",
    "Did the other children sometimes tease you?",
    "How do you think your childhood experiences relate to your feelings today?"]],

  [r'(.*)\?',
  [  "आप ऐसा क्यों पूछ रहे है?",
    "Please consider whether you can answer your own question.",
    "Perhaps the answer lies within yourself?",
    "इस सवाल का जवाब आप ही क्यों नहीं देते?"]],

  [r'अलविदा',
  [  "मुझ से बात करने के लिए शुक्रिया।",
    "अलविदा",
    "धन्यवाद। आपका १५००० रूपए का बिल है।"]],

  [r'(.*)',
  [  "मुझ इस बारे में और बताइये। ",
    "Let's change focus a bit... Tell me about your family.",
    "आप %1 क्यों बोल रहे है?",
    "अच्छा...",
    "बहुत ही रोचक।",
    "%1.",
    "इससे आपको कैसा महसुस हो रहा है?",
    "यह कह कर कैसा महसूस करते हो?"]]
  ]

def command_interface():
  print('Therapist\n---------')
  print('Talk to the program by typing in plain English, using normal upper-')
  print('and lower-case letters and punctuation.  Enter "quit" when done.')
  print('='*72)
  print('Hello.  How are you feeling today?')

  s = ''
  therapist = eliza();
  while s != 'quit':
    try:
      s = input('> ')
    except EOFError:
      s = 'quit'
    print(s)
    while s[-1] in '!.':
      s = s[:-1]
    print(therapist.respond(s))


if __name__ == "__main__":
  command_interface()
