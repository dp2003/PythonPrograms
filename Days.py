print('Enter the number of days')
	tdays=int(input())
	year=int((tdays)/365)
	month=int(tdays/30)
	week=int((tdays%365)/7)
	days=int((tdays%365)%7)
print('year',year)
print('month',month)
print('week',week)
print('days',days)