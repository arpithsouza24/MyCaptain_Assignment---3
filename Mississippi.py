string = input("please enter desired string to analyse")


def most_frequent(string):
  freq_counts = {}
  for char in string:
    freq_counts.setdefault(char, 0)
    freq_counts[char] += 1

  sorted_freq_counts = sorted(freq_counts.items(), key=lambda x : x[1], reverse=True)
  print("char, freq")
  for char, count in sorted_freq_counts:
    print(f"{char},{count}")

most_frequent(string)
