from bokeh.plotting import figure, output_file, show

# prepare some data
x = [1, 2, 3, 4, 5]
y = [60, 70, 25, 44, 50]

# output to static HTML file
output_file("lines.html")

# create a new plot with a title and axis labels
p = figure(title="simple line example", x_axis_label='Sexy Girls', y_axis_label='Sexyness')

# add a line renderer with legend and line thickness
p.line(x, y, legend_label="Temp.", line_width=4)

# show the results
show(p)
