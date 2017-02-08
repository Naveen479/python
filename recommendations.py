# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
      'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
      'The Night Listener': 3.0},
     'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
      'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
      'You, Me and Dupree': 3.5},
     'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
      'Superman Returns': 3.5, 'The Night Listener': 4.0},
     'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
      'The Night Listener': 4.5, 'Superman Returns': 4.0,
      'You, Me and Dupree': 2.5},
     'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
      'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
      'You, Me and Dupree': 2.0},
     'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
      'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
     'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0},
	'naveen': {'Snakes on a Plane':3.2},
	'babu': {'Superman Returns':4.1}}




from math import sqrt

def sim_distance(datasets,person1,person2):
	counter = 0
	total = 0
	for movies in datasets[person1]:
		if movies in datasets[person2]:

			total+=(datasets[person1][movies]-datasets[person2][movies])**2

	total = sqrt(total)


	if counter == 0:
		return 0
	else:
		return 1/(1+total)


print ( sim_distance(critics,'naveen','babu'))








def sim_person(datasets,person1,person2):
	n=0
	sum1=0
	sum2=0
	sum_sq1=0
	sum_sq2=0
	psum=0
	denominator=0

	for movies in datasets[person1]:
		if movies in datasets[person2]:
			n=n+1
			sum1+= datasets[person1][movies]
			sum2+= datasets[person2][movies]
			sum_sq1+= datasets[person1][movies]**2
			sum_sq2+= datasets[person2][movies]**2
			psum+=datasets[person1][movies]*datasets[person2][movies]
			numerator=n*psum-sum1*sum2
			denominator=sqrt(n*sum_sq1-sum1**2)*sqrt(n*sum_sq2-sum2**2)


	if denominator==0:
		return 0
	else:
		return numerator/denominator

print(sim_person(critics,'Toby','Michael Phillips'))



def topmatch(datasets, person,ranked):
	rank=[]
	for other in datasets:
		if other!= person:
			rank.append((ranked(datasets,person,other), other))
	rank.sort()
	rank.reverse()
	return rank 

print(topmatch(critics,'Lisa Rose',sim_person))


def getrecommendations(matched,person,datasets):
	total={}
	simsums={}
	for other in  datasets:
		if other != person:
			simsums=method(datasets,person,other)
			for movies in datasets[others]:
				if movies not in totals:
					total[movies] = 0
					simsums[movies] = 0

				totl[movies]+=datasets[other][movies]*sim
				simsums[movies'+=sim
	for movies in total:
		if simsums[movies]==0:
			rank.append(0,movies)
		else:
			rank.append((totla[movies]/simsums[movies],movies))
ranking.sort()
ranking.reverse()
retunr rank

print(getrecommendations(critics,'Tody',sim_person)
