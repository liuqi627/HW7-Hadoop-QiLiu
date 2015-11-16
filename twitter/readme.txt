Answer to the output file number question:
1.How many output files are there?
answer:3
2.Do they all have useful information in them?
answer:No
3.Why?
answer:Because only one reducer was assigned and worked.


A description of your program:

Map part:

Defined a method called find_candidate(line) which returns the candidate subject in the line passed in.
In the main body of the program, simply insert the name into each print line.

Reduce part:
aggregate provide by AWS/word count reducer



Final output:

Donald-neg	99923
Donald-pos	48595
Ben-neg	77291
Ben-pos	60027
Bernie-neg	35165
Bernie-pos	17368
Hillary-neg	58703
Hillary-pos	35634

