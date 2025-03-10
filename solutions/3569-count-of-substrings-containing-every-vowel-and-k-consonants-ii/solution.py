class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
    
        # find all substrings with all vowels and AT LEAST k consonants
        def atleastk(k):
            l = 0

            sub_count = 0
            vowel_counts = {
                "a": 0,
                "e": 0,
                "i": 0,
                "o": 0,
                "u": 0
            }
            consonant_count = 0
            vowel_total = 0

            for r in range(0, len(word)):
                char = word[r]
                if(char in vowel_counts):
                    prev_vowel_count = vowel_counts[char]
                    if(prev_vowel_count == 0):
                        vowel_total += 1
                    vowel_counts[char] += 1
                else:
                    consonant_count += 1
                
                while vowel_total == 5 and consonant_count >= k:
                    sub_count += len(word) - r
                    char = word[l]
                    if char in vowel_counts:
                        vowel_counts[char] -= 1
                        if(vowel_counts[char] == 0):
                            vowel_total -= 1
                    else:
                        consonant_count -= 1

                    l += 1

            return sub_count

        return atleastk(k) - atleastk(k + 1)
