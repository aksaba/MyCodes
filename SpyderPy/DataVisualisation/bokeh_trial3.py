from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange
from bokeh.plotting import figure
from bokeh.models import HoverTool
import csv


output_file("bars.html")


with open("Book2.csv") as csvfile:
    csvdata = list(csv.reader(csvfile))

DATE = [item[0] for item in csvdata]
POS_COUNT = [item[1] for item in csvdata]
#print(DATE2)


#DATE = ['01-Mar','02-Mar','03-Mar','04-Mar']
#print(DATE)
#POS_COUNT = [10,20,30,40]

data = {'DATE' : DATE,
        'POS_COUNT': POS_COUNT}



x = data['DATE']
counts = data['POS_COUNT']


source = ColumnDataSource(data=dict(x=x, counts=counts))

print(data)

p = figure(x_range=FactorRange(*x), plot_height=600, plot_width=990, title="NPS Locations by Security Checks",
           tools="pan,wheel_zoom,box_zoom,reset, save")

p.xaxis.axis_label_text_font_size = "5pt"
p.xaxis.axis_label_text_font_style='bold'

p.vbar(x='x', top='counts', width=0.9, source=source)

p.add_tools(HoverTool(tooltips=[("DATE", "@x"), ("POS_COUNT", "@counts")]))

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
