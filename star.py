nums = [5,2,7,6,8,7,2,2,1]
target = 9

for i in nums:
	if (target-i) in nums:
		# nums.index(target-i,(nums.index(i)+1),(len(nums)))
		j = str(nums.index(target-i))
		print("["+str(nums.index(i))+","+j+"]")
		
	
	
