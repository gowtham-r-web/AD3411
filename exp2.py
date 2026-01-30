import matplotlib.pyplot as plt a = [1,
2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
plt.plot(a)
# o is for circles and r is # for red
plt.plot(b, &quot;or&quot;) plt.plot(list(range(0, 22, 3)))
# naming the x-axis
plt.xlabel(&#39;Day -&gt;&#39;) #
naming the y-axis
plt.ylabel(&#39;Temp -&gt;&#39;)
c = [4, 2, 6, 8, 3, 20, 13, 15]
plt.plot(c, label = &#39;4th Rep&#39;) # get
current axes command
ax = plt.gca()
# get command over the individual #
boundary line of the graph body
ax.spines[&#39;right&#39;].set_visible(False)
ax.spines[&#39;top&#39;].set_visible(False) # set the
range or the bounds of
# the left boundary line to fixed range
ax.spines[&#39;left&#39;].set_bounds(-3, 40)
# set the interval by which # the
x-axis set the marks
plt.xticks(list(range(-3, 10)))

# set the intervals by which y-axis # set
the marks
plt.yticks(list(range(-3, 20, 3))) # legend
denotes that what color
# signifies what
ax.legend([&#39;1st Rep&#39;, &#39;2nd Rep&#39;, &#39;3rd Rep&#39;, &#39;4th Rep&#39;]) # annotate
command helps to write
# ON THE GRAPH any text xy denotes # the
position on the graph
plt.annotate(&#39;Temperature V / s Days&#39;, xy = (1.01, -2.15)) # gives a
title to the Graph
plt.title(&#39;All Features Discussed&#39;)
plt.show()
