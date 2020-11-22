# **This is a path finding programer which allows us to find the shortest past from our self selected starting and end point.**

We use the A* Path Finding Algorithm to find the shortest path between our self designated start(colour: orange) and end(colour: Turquoise) points with black cells indicating barriers or walls in the puzzle, the A* algorithm is explained below.\
\
**A(*) Algorithm explanation:**\
A* is an informed search algorithm, or a best-first search, meaning that it is formulated in terms of weighted graphs: starting from a specific starting node/cell of a graph, it aims to find a path to the given goal node having the smallest cost (least distance travelled, shortest time, etc.). It does this by maintaining a tree of paths originating at the start node and extending those paths one edge at a time until its termination criterion is satisfied, here the termination criteria is reaching the end point or taking out the end point from the open set.\
\
we use a function F which is equivalent to the sum of functions G and H (called heuristic): \
**F = G + H** \
G = *movement cost/distance of the path generated from the start point to the end point*\
H = *approximate movement cost/distance from start point to the end point*\
H or the heuristics function can be calculated using various methods which cann be exact(require more complex computations) or approximations such as the Diagonal distance, Eucledian distance or the Manhattan distance which we use here, the later two can be studied using the google search, let us focus on the Manhattan distance which is used here.\
\
In Mnahattan distance we are allowed to move from one cell to another in only four directions; that is North, South, East and West.\
Manhattan distance thus is equivalent:  absolute value of (x1 - x2) + absolute value of (y1 - y2)\
here (x1, y1) are the co-ordinates of start cell/node and (x2, y2) are the co-ordinates of end cell/node\
![alt text](https://www.researchgate.net/profile/Peter_Trebua/publication/257725676/figure/fig2/AS:669278277734402@1536579784333/Manhattan-distance-of-points-xi-1-2-a-xj-5-5-c-Chebyshev-distance-a-metric-that.png)\
\
Our open set keeps teck of nodes we want to look at.
- we start by looking at the neighbouring cells of our start point, and look for cells which are at North, South, East and West of our cell (we repeat the step for every cell we move to)  
- We always pick the node/cell from the open set which has the least value of calculated F.
- as soon as we pick the end node/cell we from the open set, the algorithm is complete as we have reached our goal and we exit the program
\
**Graphical User Interface** \
for the GUI part of the program, Pygame is used, which allows us to create our cells and add colours to diofferent cells, key bindings to our program is also done with pygame functions. 
