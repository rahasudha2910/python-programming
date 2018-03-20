num2words1 = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
def number(Number):
	num1=Number
	if (num1 >= 1) or (num1 < 19):
		print(num2words1[num1])
		return (num2words1[num1])
	elif (num1 > 20) or (num1 < 99):
		print(num2words2[num1])
		return (num2words2[num1])
	else:
		print("Number Out Of Range")
		
number(12)
