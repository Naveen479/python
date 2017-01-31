#!/usr/bin/python

base_hours = 40
ot_multiplier = 1.5

hours = float(raw_input('Enter number of hours you worked:'))

pay_rate = float(raw_input('Enter the hourly pay rate:'))

if hours > base_hours:

	overtime_hours = hours - base_hours

	overtime_pay = overtime_hours * pay_rate * ot_multiplier
	gross_pay = base_hours * pay_rate + overtime_pay

else:
	gross_pay = hours * pay_rate


print('the gross pay is $'+ str(gross_pay))
