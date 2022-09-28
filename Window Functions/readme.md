Windows function applies aggregate and ranking functions over a particular window i.e rows which are defined by OVER clause. OVER clause does two things : 

1. Patition rows into set of rows using partition clause (PARTITION BY)
2. order rows within those partitions into a particular order (ORDER BY)

Three important functions inside windows function

1. Row Number() : give sequential integer to every row within its partition
2. Rank() : It is used for ranking records
3. First_Value() : Returns the value of specific expression with respect to the first row in a window


Types of Window functions
1. Aggregate Window Functions : SUM(), MAX(), MIN(), AVG(). COUNT()
2. Ranking Window Functions: RANK(), DENSE_RANK(), ROW_NUMBER(), NTILE()
3. Value Window Functions : LAG(), LEAD(), FIRST_VALUE(), LAST_VALUE()


# Syntax

window_function ( [ ALL ] expression ) 
OVER ( [ PARTITION BY partition_list ] [ ORDER BY order_list] )

