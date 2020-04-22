# ()
# *, /
# +, -
# <, <=, >, >=, !=, ==
# not
# and
# or

# Highest precedence at top, lowest at bottom.
# Operators in the same line evaluate left to right.

# a + b * c
# 1 + 2 * 3

a = 1
b = 2
c = 3

print("a + b * c =", a + b * c)
print("(a + b) * c =", (a + b) * c)