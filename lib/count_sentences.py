#!/usr/bin/env python3

class MyString:
  def __init__(self, mstr=""):
    self.setValue(mstr);
  
  def getValue(self): return self._value;

  def setValue(self, mstr):
    if (type(mstr) == str): self._value = mstr;
    else: print("The value must be a string.");

  value = property(getValue, setValue);
  
  def is_sentence(self): return self.value.endswith(".");

  def is_question(self): return self.value.endswith("?");

  def is_exclamation(self): return self.value.endswith("!");

  def remExtraPunctuation(self, mystr):
    myostr = "" + mystr;
    i = 0;
    while(i < len(myostr)):
      #print(f"myostr[{i}]={myostr[i]}");
      if (myostr[i] == "?" or myostr[i] == "." or myostr[i] == "!"):
        if (i + 1 < len(myostr)):
          if (myostr[i + 1] == "?" or myostr[i + 1] == "." or myostr[i + 1] == "!"):
            myostr = myostr[0:i] + myostr[(i + 1):];
            i -= 1;
            #print(f"NEW myostr = {myostr}");
      i += 1;
    #print(f"FINAL myostr = {myostr}");
    return myostr;

  def count_sentences(self):
    myostr = self.remExtraPunctuation(self.value);
    print(f"myostr = {myostr}");
    #although it is not proper no one gave us a list of abbreviations we would have to search for...
    #unfortunately something like "My DNA. is different than yours." would change the count
    #it is easy without an ignore list, but something like that would have 2 instead of 1.
    cnt = 0;
    for letter in myostr:
      if (letter == "?" or letter == "." or letter == "!"):
        cnt += 1;
    return cnt;

tststr = MyString("Stupid sentence!!!");
print(tststr.count_sentences());
