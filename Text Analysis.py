#Scenario: Text Analysis

#PART-A

## Step 1: Define a string
givenstring="Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

## Step 2: Define the class and its attributes
class TextAnalyzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        formattedText = text.replace('.','').replace('!','').replace('?','').replace(',','')
        
        # make text lowercase
        formattedText = formattedText.lower()
        
        self.fmtText = formattedText
        
    def freqAll(self):        
        # split text into words
        wordList = self.fmtText.split(' ')
        
        # Create dictionary
        freqMap = {}
        for word in set(wordList): # use set to remove duplicates in list
            freqMap[word] = wordList.count(word)
        
        return freqMap
           
    def freqOf(self,word):
        # get frequency map
        freqDict = self.freqAll()
        
        if word in freqDict:
            return freqDict[word]
        else:
            return 0
        
#PART-B

## Step 1: Create an instance of TextAnalyzer class
analyzed = TextAnalyzer(givenstring)

## Step 2: Call the function that converts the data into lowercase
print("Formatted Text:", analyzed.fmtText)

## Step 3: Call the function that counts the frequency of all unique words from the data
print("Frequency of all words:", analyzed.freqAll())

## Step 4: Call the function that counts the frequency of a specific word
count_words = analyzed.freqOf("lorem")
print(count_words)