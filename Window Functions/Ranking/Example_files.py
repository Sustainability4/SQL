'''
Table Schema 


Cats:
name	varchar
breed	varchar
weight	float
color	varchar
age	int



Question 1 : We would like to find the fattest cat. Order all our cats by weight.The two heaviest cats should both be 1st. The next heaviest should be 3rd.

SQL Code : select rank() over (order by weight desc) as ranking, weight, name from cats order by ranking,name

output : 

ranking	weight	name
1	6.1	Oscar
1	6.1	Smokey
3	5.7	Misty
4	5.5	Alfie
5	5.4	Millie
6	5.1	Puss
7	5.0	Felix
8	4.9	Smudge
9	4.8	Charlie
10	4.5	Ashes
11	4.2	Molly
12	3.8	Tigger


Question 2: Each cat would like to know what percentage of other cats weigh less than it

Return: name, weight, percent
Order by: weight

SQL Code : select name, weight, percent_rank() over(order by weight) *100 as percent from cats

output :

name	weight	percent
Tigger	3.8	0.0
Molly	4.2	9.1
Ashes	4.5	18.2
Charlie	4.8	27.3
Smudge	4.9	36.4
Felix	5.0	45.5
Puss	5.1	54.5
Millie	5.4	63.6
Alfie	5.5	72.7
Misty	5.7	81.8
Oscar	6.1	90.9
Smokey	6.1	90.9


Question 3: Each cat would like to know what weight percentile it is in. This requires casting to an integer

Return: name, weight, percent
Order by: weight

SQL Code : select name, weight, cast(cume_dist() over(order by weight) *100 as integer) as percent from cats

Output: 

name	weight	percent
Tigger	3.8	8
Molly	4.2	17
Ashes	4.5	25
Charlie	4.8	33
Smudge	4.9	42
Felix	5.0	50
Puss	5.1	58
Millie	5.4	67
Alfie	5.5	75
Misty	5.7	83
Oscar	6.1	100
Smokey	6.1	100

Question 4: We are worried our cats are too fat and need to diet.We would like to group the cats into quartiles by their weight.

Return: name, weight, weight_quartile
Order by: weight

SQL Query : select name, weight, ntile(4) over(order by weight) as weight_quartile from cats

Output:

name	weight	weight_quartile
Tigger	3.8	1
Molly	4.2	1
Ashes	4.5	1
Charlie	4.8	2
Smudge	4.9	2
Felix	5.0	2
Puss	5.1	3
Millie	5.4	3
Alfie	5.5	3
Misty	5.7	4
Oscar	6.1	4
Smokey	6.1	4


Question 5 : Cats are fickle. Each cat would like to lose weight to be the equivalent weight of the cat weighing just less than it.

Print a list of cats, their weights and the weight difference between them and the nearest lighter cat ordered by weight.

Return: name, weight, weight_to_lose
Order by: weight

SQL Query : select name, weight,coalesce(weight - lag(weight,1) over (order by weight), 0) as weight_to_lose from cats order by weight

Output: 
name	weight	weight_to_lose
Tigger	3.8	0.0
Molly	4.2	0.4
Ashes	4.5	0.3
Charlie	4.8	0.3
Smudge	4.9	0.1
Felix	5.0	0.1
Puss	5.1	0.1
Millie	5.4	0.3
Alfie	5.5	0.1
Misty	5.7	0.2
Oscar	6.1	0.4
Smokey	6.1	0.0

Question 6 : The cats now want to lose weight according to their breed. Each cat would like to lose weight to be the equivalent weight of the cat in the same breed weighing just less than it.

Print a list of cats, their breeds, weights and the weight difference between them and the nearest lighter cat of the same breed.

Return: name, breed, weight, weight_to_lose
Order by: weight

SQL Query : select name, breed, weight, coalesce(weight - lag(weight,1) over (partition by breed order by weight), 0) as weight_to_lose from cats order by weight

Output: 
name	breed	weight	weight_to_lose
Tigger	British Shorthair	3.8	0.0
Molly	Persian	4.2	0.0
Ashes	Persian	4.5	0.3
Charlie	British Shorthair	4.8	1.0
Smudge	British Shorthair	4.9	0.1
Felix	Persian	5.0	0.5
Puss	Maine Coon	5.1	0.0
Millie	Maine Coon	5.4	0.3
Alfie	Siamese	5.5	0.0
Misty	Maine Coon	5.7	0.3
Oscar	Siamese	6.1	0.6
Smokey	Maine Coon	6.1	0.4

Question 7 : Cats are vain. Each cat would like to pretend it has the lowest weight for its color.

Print cat name, color and the minimum weight of cats with that color.

Return: name, color, lowest_weight_by_color
Order by: color, name


SQL Query : select name, color, min(weight) over(partition by color) as weight_by_color from cats order by color, name

output: 
name	color	weight_by_color
Ashes	Black	4.2
Charlie	Black	4.2
Molly	Black	4.2
Oscar	Black	4.2
Smudge	Black	4.2
Alfie	Brown	5.5
Misty	Brown	5.5
Smokey	Brown	5.5
Felix	Tortoiseshell	3.8
Millie	Tortoiseshell	3.8
Puss	Tortoiseshell	3.8
Tigger	Tortoiseshell	3.8

Question 8 : Each cat would like to see the next heaviest cat's weight when grouped by breed. If there is no heavier cat print 'fattest cat'

Print a list of cats, their weights and either the next heaviest cat's weight or 'fattest cat'

Return: name, weight, breed, next_heaviest
Order by: weight

SQL : select name, weight, breed, coalesce(cast(lead(weight,1) over(partition by breed order by weight) as varchar), 'fattest cat') as next_heaviest from cats order by weight

Output : 
name	weight	breed	next_heaviest
Tigger	3.8	British Shorthair	4.8
Molly	4.2	Persian	4.5
Ashes	4.5	Persian	5
Charlie	4.8	British Shorthair	4.9
Smudge	4.9	British Shorthair	fattest cat
Felix	5.0	Persian	fattest cat
Puss	5.1	Maine Coon	5.4
Millie	5.4	Maine Coon	5.7
Alfie	5.5	Siamese	6.1
Misty	5.7	Maine Coon	6.1
Oscar	6.1	Siamese	fattest cat
Smokey	6.1	Maine Coon	fattest cat

Question 9 : The cats have decided the correct weight is the same as the 4th lightest cat. All cats shall have this weight. Except in a fit of jealous rage they decide to set the weight of the lightest three to 99.9

Print a list of cats, their weights and their imagined weight

Return: name, weight, imagined_weight
Order by: weight

SQL Query : select name, weight, coalesce(nth_value(weight, 4) over (order by weight), 99.9) as imagined_weight from cats order by weight

Output:
name	weight	imagined_weight
Tigger	3.8	99.9
Molly	4.2	99.9
Ashes	4.5	99.9
Charlie	4.8	4.8
Smudge	4.9	4.8
Felix	5.0	4.8
Puss	5.1	4.8
Millie	5.4	4.8
Alfie	5.5	4.8
Misty	5.7	4.8
Oscar	6.1	4.8
Smokey	6.1	4.8

Question 10 : The cats want to show their weight by breed. The cats agree that they should show the second lightest cat's weight (so as not to make other cats feel bad)

Print a list of breeds, and the second lightest weight of that breed

Return: breed, imagined_weight
Order by: breed

SQL Query : select distinct(breed), nth_value(weight,2) over(partition by breed order by weight RANGE BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) as imagined_weight from cats order by breed

Output: 
breed	imagined_weight
British Shorthair	4.8
Maine Coon	5.4
Persian	4.5
Siamese	6.1


'''




