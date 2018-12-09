class Solution(object):
    def uniqueMorseRepresentations(self, words):
        transformations = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
          string = ""
          for char in word:
            string += morse[ord(char) - 97]
          transformations.add(string)
        return len(transformations)