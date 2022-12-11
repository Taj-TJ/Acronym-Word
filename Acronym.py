user_input=input('Enter the Phase:-')
clean_input=(user_input.replace('of',''))
phrase=clean_input.split()
acronym=""
for i in phrase:
    acronym=acronym+i[0].upper()
print('The acronym of '+ user_input +"is:- " + acronym)
def fxn(a):
    lst=a.split()
    output=""
    for word in lst:
        output+=word[0]
    output=output.upper()
    return output
input1=input('Enter the phrase:- ')
print(fxn(input1))
input2=input('Enter the phrase:- ')
print(fxn(input2))
input3=input('Enter the phrase:- ')
print(fxn(input3)) 
