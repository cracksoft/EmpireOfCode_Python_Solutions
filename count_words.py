def count_words(text, words):
	sum=0
	for word in words:
		if word in text.lower():
			sum+=1
	#print(sum)
	return sum

count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"})
count_words("Bananas, give me bananas!!!", {"banana", "bananas"})
count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
            {"sum", "hamlet", "infinity", "anything"})
'''
if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"

    print("All set? Click 'Check' to review your code and earn rewards!")
'''