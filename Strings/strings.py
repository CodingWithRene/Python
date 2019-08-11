# Strings

first_name = 'Rene'
print first_name

last_name = "vanderWatt"
print last_name

multi_line_string = '''multi
line
comment
'''
print multi_line_string

# index
print first_name[0]
print first_name[0:]

#strip

toStrip = '     whiteSpace?         '
print toStrip.strip()

#len

print len(last_name)

#change case
print 'AbCdEfG'.upper()
print 'AbCdEfG'.lower()

#replace
print first_name.replace('e', '6')

#split
print 'a,b ,c,d, e,f, g,h ,i,j, k,l'.split(' ')1