from func import shortestWordPath

class TestSuite:
    
    def __init__(self):
        simpleList = ["bat", "but", "cut", "cot"]
        complexList1 = ["bat", "bot", "but", "spit", "cut", "scat", "cat", "dot", "cot", "goat", "got" "shot"]
        complexList2 = ["bat", "cat", "bath", "bathe", "path", "ice", "mice", "twice", "wrath", "can", "cane", "cape", "chase", "chose", "choose", "goose", "choke", "pith", "pits", "sits", "mits", "mite", "fits"]
        
        self.simpleDict = {word:True for word in simpleList}
        self.complexDict1 = {word:True for word in complexList1}
        self.complexDict2 = {word:True for word in complexList2}

    def testEqual(self, startWord, endWord, wordDict, expectedAnswer):
        if shortestWordPath(startWord, endWord, wordDict) == expectedAnswer:
            print("True")
            return True
        print("False")
        return False
    
    # -------
    # Simplified version of unit tests (without using unittest library) and not extensive

    # Testing when startWord == endWord
    def test_same_word_simple_path_exists(self):
        return self.testEqual("but", "but", self.simpleDict, "but")
    
    def test_same_word_complex_path_exists(self):
        return self.testEqual("spit", "spit", self.complexDict1, "spit")
    
    # Testing that checking whether two words differ by a single letter works as expected
    def test_letterchange_path(self):
        return self.testEqual("bot", "but", self.complexDict1, "bot - but")
    
    def test_letteraddition_path(self):
        return self.testEqual("cat", "scat", self.complexDict1, "cat - scat")
    
    def test_letterdeletion_path(self):
        return self.testEqual("goat", "got", self.complexDict1, "goat - got")
    
    # Testing path answers are as expected
    def test_simple_path_exists(self):
        return self.testEqual("bat", "cut", self.complexDict1, "bat - but - cut")
    
    def test_simple_path_exists2(self): # NOTE: unclear about directions on whether startWord/endWord are proper words
        return self.testEqual("bat", "hut", self.complexDict1, "bat - but - hut")
    
    def test_simple_path_not_exists(self):
        return self.testEqual("bat", "ran", self.complexDict1, None)
    
    def test_complex_path_exists(self):
        return self.testEqual("bat", "ice", self.complexDict2, "bat - bath - path - pith - pits - mits - mite - mice - ice")
    
    def test_complex_path_not_exists(self):
        return self.testEqual("bath", "wrath", self.complexDict2, None)

    # Run all tests
    def runTestSuite(self):
        self.test_same_word_simple_path_exists()
        self.test_same_word_complex_path_exists()
        self.test_letterchange_path()
        self.test_letteraddition_path()
        self.test_letterdeletion_path()
        self.test_simple_path_exists()
        self.test_simple_path_exists2()
        self.test_simple_path_not_exists()
        self.test_complex_path_exists()
        self.test_complex_path_not_exists()
    

# MAIN CALL
testsuite = TestSuite()
testsuite.runTestSuite()

