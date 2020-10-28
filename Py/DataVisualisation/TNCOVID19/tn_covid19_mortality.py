########################################################################
## Bar plot and line plot in one graph
## Secondary y-axis for the line plot
## Interactive tooltips
########################################################################

from bokeh.plotting import output_file,save,figure,show
from bokeh.models import HoverTool,ColumnDataSource,FactorRange,Range1d,LinearAxis,DatetimeTickFormatter,ranges, SingleIntervalTicker, Label
import csv
import numpy as np
output_file('vbar_mortality.html')
with open("Book2.csv") as csvfile:
    csvdata = list(csv.reader(csvfile))

DATE = [item[0] for item in csvdata]
DEATH_COUNT = [item[9] for item in csvdata]
DEATH_PERCENT = [item[10] for item in csvdata]
data = {'DATE' : DATE,
        'DEATH_COUNT': DEATH_COUNT,
        'DEATH_PERCENT':DEATH_PERCENT}
x = data['DATE']
death_counts = data['DEATH_COUNT']
death_percent = data['DEATH_PERCENT']
ymax = int(death_counts[len(death_counts)-1])+10
source = ColumnDataSource(data=dict(x=x, death_counts=death_counts,death_percent=death_percent))

mytext1_ypos = int(death_counts[len(death_counts)-1])-5
mytext1 = Label(x=1, y=mytext1_ypos, text='Day 0 (first detected case): 07 March 2020')

plot1 = figure(x_range=x,y_range=(0,ymax),plot_width=700,plot_height=350,title="Number of deaths (Cumulative) and % mortality rate")
plot1.extra_y_ranges = {"foo": Range1d(start=0, end=5)}
plot1.vbar('x', top='death_counts', width=0.9, source=source)
plot1.yaxis.axis_label = "Count"
plot1.line(x,death_percent,y_range_name = "foo",line_color="red", line_width = 3.5,alpha = 0.75, legend_label = "% mortality rate")
plot1.add_layout(LinearAxis(y_range_name="foo",axis_label="%"), 'right')
plot1.title.text_font_size = "15pt"
plot1.xaxis.axis_label = "Day"
plot1.xaxis.axis_label_text_font = "times"
plot1.xaxis.axis_label_text_font_style = "normal"
plot1.xaxis.major_label_text_font_size = "10pt"
plot1.xaxis.major_label_orientation = np.pi/2
plot1.xaxis.axis_label_text_font_size = "15pt"
plot1.xaxis.ticker = SingleIntervalTicker(interval=4)
plot1.yaxis.axis_label_text_font = "times"
plot1.yaxis.axis_label_text_font_style = "normal"
plot1.yaxis.major_label_text_font_size = "10pt"
plot1.yaxis.axis_label_text_font_size = "15pt"
legend_ypos = float(death_counts[len(death_counts)-1])+15  # Decrease number
plot1.legend.location = (1,legend_ypos)
plot1.add_tools(HoverTool(tooltips=[("DATE", "@x"), ("No. of deaths","@death_counts"),("% mortality", "@death_percent")]))
plot1.add_layout(mytext1)

save(plot1)
