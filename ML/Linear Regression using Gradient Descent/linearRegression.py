from numpy import genfromtxt, array


# computes the error function
def compute_error(b, m, points):
    totalError = 0
    # get the square distance between the actual and the predicted value
    for i in xrange(0, len(points)):
        y = points[i, 1]
        x = points[i, 0]
        totalError += (y - (x * m + b)) ** 2
    return totalError / float(len(points))


# for each iteration get closer to the local minimum  value
def gradient_descent_steps(b, m, points, learningRate):
    # we initialize new values as we want to loop through the points with the original given b and m
    gradient_b = 0
    gradient_m = 0
    N = float(len(points))
    for i in xrange(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        # formula for gradient
        gradient_b -= 2/N * (y - (x * m + b))
        gradient_m -= 2/N * x * (y - (x * m + b))
    # calculate the new b and m
    new_b = b - (learningRate * gradient_b)
    new_m = m - (learningRate * gradient_m)
    return new_b, new_m


# runs gradient descent algorithm
def gradient_descent(b, m, points, iterationTimes, learningRate):
    # for each b and m go step closer to the local minimum
    for i in xrange(iterationTimes):
        b, m = gradient_descent_steps(b, m, points, learningRate)
    return b, m


def main():
    # get the training data
    points = genfromtxt('data.csv', delimiter=',')
    # hyper parameters
    learningRate = 0.0001

    # y = mx + b
    initial_b = 0
    initial_m = 0

    # static iteration times that fits the size of our data
    iterationTimes = 1000

    print "Starting gradient descent at b = {0}, m = {1}, error = {2}"\
        .format(initial_b, initial_m, compute_error(initial_b, initial_m, points))
    b, m = gradient_descent(initial_b, initial_m, array(points), iterationTimes, learningRate)
    print "After iteration 1000 times ..  gradient descent at b = {0}, m = {1}, error = {2}"\
        .format(b, m, compute_error(b, m, points))


if __name__ == '__main__':
    main()
