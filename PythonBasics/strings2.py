
In Python, a string is a sequence of characters used to represent text. Strings are one of the fundamental data types in Python and are used extensively for handling textual data. Here's a breakdown of strings in Python with examples:

1. Creating Strings:

You can create strings in Python using single quotes ('...'), double quotes ("..."), or triple quotes ('''...''' or """...""").

Single quotes:

Python

greeting = 'Hello'
country = 'Kenya'
Double quotes:

Python

message = "Welcome to Nairobi!"
quote = "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
Triple quotes: Triple quotes are useful for multi-line strings or when you want to include single or double quotes within the string without escaping them.

Python

paragraph = '''This is a
multi-line string
in Python.'''

html_code = """
<div>
    <p>This is some HTML content.</p>
</div>
"""
2. Immutability:

Strings in Python are immutable, which means once a string is created, you cannot change its individual characters directly. If you need to modify a string, you have to create a new string based on the original one.

Python

my_string = "Python"
# my_string[0] = 'J'  # This will raise a TypeError: 'str' object does not support item assignment

new_string = 'J' + my_string[1:]  # Creating a new string
print(new_string)  # Output: Jython
3. Accessing Characters (Indexing):

You can access individual characters in a string using their index. Python uses zero-based indexing, meaning the first character is at index 0, the second at index 1, and so on. You can also use negative indexing to access characters from the end of the string (-1 for the last character, -2 for the second to last, etc.).

Python

city = "Mombasa"
print(city[0])   # Output: M
print(city[3])   # Output: b
print(city[-1])  # Output: a
print(city[-3])  # Output: s
4. Slicing:

Slicing allows you to extract a substring (a portion of a string) by specifying a range of indices. The syntax for slicing is [start:end:step].

start: The index where the slice begins (inclusive). If omitted, it defaults to 0.
end: The index where the slice ends (exclusive). If omitted, it defaults to the end of the string.
step: The increment between indices (optional, defaults to 1).
Python

full_name = "Jomo Kenyatta"
first_name = full_name[0:4]  # Characters from index 0 up to (but not including) 4
print(first_name)  # Output: Jomo

last_name = full_name[5:]   # Characters from index 5 to the end
print(last_name)   # Output: Kenyatta

middle_name = full_name[5:13] # Characters from index 5 up to (but not including) 13
print(middle_name) # Output: Kenyatta

every_other = full_name[::2] # Every other character
print(every_other) # Output: JmKnatt

reversed_name = full_name[::-1] # Reversing the string
print(reversed_name) # Output: attaynek omoJ
5. String Operations:

Python supports several operations that can be performed on strings:

Concatenation (+): Used to combine two or more strings.

Python

part1 = "Kenya"
part2 = " is beautiful"
full_string = part1 + part2
print(full_string)  # Output: Kenya is beautiful
Repetition (*): Used to repeat a string a specified number of times.

Python

repeat_string = "Karibu! " * 3
print(repeat_string)  # Output: Karibu! Karibu! Karibu!
6. Built-in String Methods:

Python provides many built-in methods that allow you to perform various operations on strings. Here are some common ones:

len(): Returns the length (number of characters) of a string.

Python

word = "Uhuru"
print(len(word))  # Output: 5
lower(): Returns a new string with all characters converted to lowercase.

Python

text = "National Hospital"
lower_text = text.lower()
print(lower_text)  # Output: national hospital
upper(): Returns a new string with all characters converted to uppercase.

Python

text = "National Hospital"
upper_text = text.upper()
print(upper_text)  # Output: NATIONAL HOSPITAL
strip(): Returns a new string with leading and trailing whitespace removed. You can also specify characters to remove.

Python

text_with_spaces = "   Data Entry   "
stripped_text = text_with_spaces.strip()
print(stripped_text)  # Output: Data Entry

text_with_chars = "***Important***"
stripped_chars = text_with_chars.strip("*")
print(stripped_chars) # Output: Important
split(): Splits a string into a list of substrings based on a specified delimiter. If no delimiter is specified, it defaults to whitespace.

Python

sentence = "Blood Bank Management System"
words = sentence.split()
print(words)  # Output: ['Blood', 'Bank', 'Management', 'System']

data = "donor_id,name,blood_type"
fields = data.split(",")
print(fields) # Output: ['donor_id', 'name', 'blood_type']
join(): Concatenates a list or other iterable of strings into a single string, using the string on which the method is called as the separator.

Python

parts = ["Real-time", "Inventory", "Tracking"]
joined_string = " ".join(parts)
print(joined_string)  # Output: Real-time Inventory Tracking
find(): Returns the index of the first occurrence of a substring within the string. If the substring is not found, it returns -1.

Python

phrase = "Locate donation centers online"
index = phrase.find("donation")
print(index)  # Output: 7
replace(): Returns a new string where all occurrences of a specified substring are replaced with another substring.

Python

old_text = "manual donor records"
new_text = old_text.replace("manual", "digital")
print(new_text)  # Output: digital donor records
startswith(): Returns True if the string starts with the specified prefix, and False otherwise.

Python

filename = "report_2023.pdf"
starts_with_report = filename.startswith("report")
print(starts_with_report)  # Output: True
endswith(): Returns True if the string ends with the specified suffix, and False otherwise.

Python

email = "info@knbts.go.ke"
ends_with_ke = email.endswith(".ke")
print(ends_with_ke)  # Output: True
7. f-strings (Formatted String Literals):

Introduced in Python 3.6, f-strings provide a concise and readable way to embed expressions inside string literals 1  for formatting. You prefix the string with an f or F and then enclose variables or expressions you want to embed in curly braces {}.   
1.
github.com
github.com

Python

donor_name = "Alice"
blood_group = "O+"
message = f"Thank you, {donor_name}, for your O+ blood donation."
print(message)  # Output: Thank you, Alice, for your O+ blood donation.

stock_level = 50
expiry_date = "2025-05-15"
alert = f"Low stock alert: {stock_level} units expiring on {expiry_date}."
print(alert)  # Output: Low stock alert: 50 units expiring on 2025-05-15.
