# string methods

a = "devil-client"

print("Starting")
print(len(a))
print(a.upper())
print(a.lower())
print(a.split(" "))
print(a.rstrip())
print(a.replace("devil-client","evdev-client"))
print(a)

text = "  Python is a versatile language!  "

# 1. Formatting and Padding
print(f"Original: '{text}'")

# center(width, fillchar): Centers the string within a specified width.
centered = text.center(40, "*")
print(f"center(40, '*'): '{centered}'")

# ljust(width, fillchar): Left-justifies the string within a specified width.
left_justified = text.ljust(40, "-")
print(f"ljust(40, '-'): '{left_justified}'")

# rjust(width, fillchar): Right-justifies the string within a specified width.
right_justified = text.rjust(40, ".")
print(f"rjust(40, '.'): '{right_justified}'")

# zfill(width): Pads the string with leading zeros to a specified width.
number_str = "42"
zero_filled = number_str.zfill(5)
print(f"zfill(5): '{zero_filled}'")

# 2. String Transformations
print(f"\nOriginal: '{text}'")

# expandtabs(tabsize): Replaces tab characters with spaces.
tabbed_text = "Hello\tWorld"
expanded = tabbed_text.expandtabs(8)
print(f"expandtabs(8): '{expanded}'")

# encode(encoding, errors): Encodes the string using the specified encoding.
encoded = text.encode("utf-8")
print(f"encode('utf-8'): {encoded}")

# 3. String Partitioning
print(f"\nOriginal: '{text}'")

# partition(sep): Splits the string at the first occurrence of sep and returns a tuple (before, sep, after).
partitioned = text.partition("is")
print(f"partition('is'): {partitioned}")

# rpartition(sep): Splits the string at the last occurrence of sep and returns a tuple (before, sep, after).
rpartitioned = text.rpartition("language")
print(f"rpartition('language'): {rpartitioned}")

# 4. Checking String Types
print(f"\nOriginal: '{text}'")

# isdecimal(): Returns True if all characters are decimal characters.
decimal_str = "12345"
print(f"isdecimal(): {decimal_str.isdecimal()}")

# isnumeric(): Returns True if all characters are numeric characters.
numeric_str = "123⁴" #includes superscripts and other numeric chars
print(f"isnumeric(): {numeric_str.isnumeric()}")

# isprintable(): Returns True if all characters are printable.
printable_str = "Hello\nWorld"
print(f"isprintable(): {printable_str.isprintable()}") #Will return false due to the \n

# isidentifier(): Returns True if the string is a valid identifier.
identifier_str = "my_variable"
print(f"isidentifier(): {identifier_str.isidentifier()}")

# 5. String Translation
print(f"\nOriginal: '{text}'")

# translate(table): Returns a copy of the string where each character has been mapped through the given translation table.
translation_table = str.maketrans("aeiou", "12345") #creates a translation table.
translated = text.translate(translation_table)
print(f"translate(table): '{translated}'")

# 6. Boolean checks

print(f"\nOriginal: '{text}'")

#isascii(): returns true if all characters are ascii characters.
ascii_string = "Hello"
non_ascii_string = "こんにちは"
print(f"isascii(): {ascii_string.isascii()}")
print(f"isascii(): {non_ascii_string.isascii()}")