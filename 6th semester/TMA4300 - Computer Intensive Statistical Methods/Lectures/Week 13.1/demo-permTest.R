# Read data
source("permdata.txt")

# permdata$y contains the y datapoints supposed to 
# come from F1
# permdata$z contains the z datapoints supposed to 
# come from F2


# Prepare data
fData = c(permdata$y,permdata$z)
m = length(permdata$y)
n = length(permdata$z)
theta0 = abs(mean(permdata$y)-mean(permdata$z))
thetaAlt0 = abs(sum(permdata$y)^2/(m*sum(permdata$y^2))-
    sum(permdata$z)^2/(n*sum(permdata$z^2)))

# Number of permutations
B = 1500 # 1500

# Initialize storage
tot = 0
totAlt = 0

sTMP1 = rep(0, B)
sTMP2 = sTMP1

# Permutation test
for(i in 1:B){
	# generate a random permutation of the elements of x (or 1:x).
	x = sample(fData, size=length(fData), replace=FALSE)
	theta = abs(mean(x[1:m])-mean(x[(m+1):(m+n)]))
	thetaAlt = abs(sum(x[1:m])^2/(m*sum(x[1:m]^2))-
        sum(x[(m+1):(m+n)])^2/(n*sum(x[(m+1):(m+n)]^2)))
	if(theta >= theta0){
		tot = tot + 1
	}
	if(thetaAlt >= thetaAlt0){
		totAlt = totAlt + 1
	}
	sTMP1[i] = theta
	sTMP2[i] = thetaAlt
}
tot = tot/B
totAlt = totAlt/B

print('p-value:')
print(tot)
print('p-value:')
print(totAlt)

#Show histogram
par(mfrow=c(1,2))
hist(sTMP1,nclass=20, xlim=c(0, 1))
points(theta0,0,col=2, pch=20)
#Show histogram
hist(sTMP2,nclass=20)
points(thetaAlt0,0,col=2, pch=20)
