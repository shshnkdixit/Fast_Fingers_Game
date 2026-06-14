import random
import time 
print('='*60)
print("         ⌨️   WELCOME TO TYPING SPEED TEST GAME  ⌨️     ")
print('='*60)

sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "She sells seashells by the seashore.",
    "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
    "Peter Piper picked a peck of pickled peppers.",
]

sentence = random.choice(sentences)

print("\nType the following sentence:\n")
print(sentence)

(input("\nPress Enter to start the Test..."))

# time taken checker
start_time = time.time()
typed_text = input("\nStart typing:\n")
end_time = time.time()
time_taken = end_time - start_time

# mistakes checker
mistakes = 0

original_words = sentence.lower().split()
typed_words = typed_text.lower().split()

for i in range(min(len(original_words), len(typed_words))):
    if original_words[i] != typed_words[i]:
        mistakes += 1

mistakes += abs(len(original_words) - len(typed_words))

# accuracy checker
total_words = len(original_words)
accuracy = max(0, (total_words - mistakes) / total_words * 100)

# speed checker meaured in words per minute
words = len(typed_text.split())
wpm = words/ (time_taken/60)


# printing the results
print("\n" + "="*60+ "\n")

print(f"Time taken   : {time_taken:.2f} seconds".upper())
print(f"Typing Speed : {wpm:.2f} wpm ".upper())
print(f"Accuracy     : {accuracy:.2f}%".upper())
print(f"Mistakes     : {mistakes}".upper())

if accuracy == 100:
  print("\n🏆 Perfect! Outstanding typing!")
elif accuracy >= 90:
  print("\n🎉 Great job! Keep it up!")
elif accuracy >= 75:
  print("\n👍 Good effort! Practice more.")
else:
  print("\n💪 Keep practicing. You'll improve!")
  
 
print("\n" + "="*60)
