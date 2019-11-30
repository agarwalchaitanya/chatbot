import string
import re
import random

class eliza:
  def __init__(self):
    self.keys = list(map(lambda x:re.compile(x[0], re.IGNORECASE),gPats))
    self.values = list(map(lambda x:x[1],gPats))

  #to clean the input string
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

#reflection in the hindi language
gReflections = {
  "हूँ"   : "हो",
  "था"  : "थे",
  "मैं"    : "आप",
  "मेरे पास"  : "आपके पास",
  "मेरा"  : "आपका",
  "हो"  : "हूँ",
  "आपके पास": "मेरे पास",
  "आपका"  : "मेरा",
  "आप"  : "मैं",
  "मुझे"  : "आपको"
}

#regular expressions for matching
gPats = [
  [r'मुझे (.*) चाहिए',
  [  "आपको %1 क्यों चाहिए ?",
    "क्या आपको %1 से मदद मिलेगी??",
    "क्या आपको यकीन है आपको %1 चाहिए??"]],

  [r'में (.*) हूँ',
  [  "क्या आप मेरे पास आये क्यूंकि आप %1 हो??",
    "आप कितने टाइम से %1 हो??",
    "आप को कैसा लगता है की आप (.*) हो??"]],

  [r'क्या आप ([^\?]*) हो\??',
  [  "क्या फरक पड़ता है की मैं %1 हूँ?",
    "क्या आपको बेहतर लगेगा की मैं %1 ना हूँ?",
    "मशायद आपको लगता है मैं %1 हूँ।",
    "मैं शायद %1 हूँ। आपको क्या लगता है?"]],

  [r'क्यूंकि (.*)',
  [  "क्या यह असली कारन है %1?",
    "और क्या कारन आते है आपके दिमाग में?",
    "क्या यह किसी और पे भी लागू होता है?",
    "अगर %1, तो और क्या सच है?"]],

  [r'नमस्ते(.*)',
  [  "नमस्ते में खुश हूँ की आप आये।",
    "नमस्ते, आज आप कैसे हो?"]],

  [r'(.*) दोस्त (.*)',
  [  "मुझे अपने दोस्तों के बारे में और बताइये",
    "आपके सबसे अच्छे बचपन के दोस्त के बारे में बताइये"]],

  [r'हाँ',
  [  "आप काफी विशवास से बोल रहे हो।",
    "ठीक है। पर इस बारे में क्या आप और बता सकते है?"]],

  [r'मेरा|मेरी (.*)',
  [  "अच्छा, आपका %1.",
    "आप ऐसा क्यों कह रहे की आपका %1?"]],

  [r'आप (.*)',
  [  "हमे आपके बारे में बात करनी है, मेरे नहीं",
    "आप ऐसा मेरे बारे में क्यों बोल रहे हो?",]],

  [r' (.*) क्यों (.*)',
  [  "आपको क्या लगता है क्यों?",
    "यह आप मुझे बताइये?" ]],

  [r'मुझे (.*) चाहिए',
  [  "आपके लिए %1 का क्या महत्व है??",
    "आपको %1 क्यों चाहिए??",
    "अगर आपको मिलेगा तो आप क्या करोगे?"]],

  [r'(.*) पिताजी|पिता|पापा|बाप(.*)',
  [  "अपने पिताजी के बारे में और बताइये?",
    "आप अपने पिताजी के बारे में क्या सोचते है?",]],

  [r'(.*)\?',
  [  "आप ऐसा क्यों पूछ रहे है?",
    "शायद जवाब आपके पास ही है?",
    "इस सवाल का जवाब आप ही क्यों नहीं देते?"]],

  [r'अलविदा',
  [  "मुझ से बात करने के लिए शुक्रिया।",
    "अलविदा",
    "धन्यवाद। आपका १५००० रूपए का बिल है।"]],

  [r'(.*)',
  [  "मुझ इस बारे में और बताइये। ",
    "चलिए हम विषय बदलते है.... आप अपने परिवार के बारे में बताइये।",
    "आप %1 क्यों बोल रहे है?",
    "अच्छा...",
    "बहुत ही रोचक।",
    "%1.",
    "इससे आपको कैसा महसुस हो रहा है?",
    "यह कह कर कैसा महसूस करते हो?"]]
  ]

def command_interface():
  print('Therapist - ELIZA (hindi)\n---------')
  print('Interact with the program by typing in Hindi,')
  print('Enter "अलविदा" when done.')
  print('='*72)
  print('आपका स्वागत है। आज आप कैसे है? ?')

  s = ''
  therapist = eliza()
  while s != 'अलविदा':
    try:
      s = input('You: ')
    except EOFError:
      s = 'अलविदा'
    print(s)
    while s[-1] in '!.':
      s = s[:-1]
    print("ELIZA: " + therapist.respond(s))


#main function
if __name__ == "__main__":
  command_interface()
