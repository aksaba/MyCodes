########################################################################
## Three line plots in the same graph
## Secondary y-axis for one of the plots
## Interactive tooltips for each plot
########################################################################

from bokeh.plotting import output_file,save,figure,show
from bokeh.models import HoverTool,ColumnDataSource,FactorRange,Range1d,LinearAxis,Label,SingleIntervalTicker
import csv
import numpy as np
output_file('vbar_samples.html')
with open("Book2.csv") as csvfile:
    csvdata = list(csv.reader(csvfile))

DATE = [item[0] for item in csvdata]
SAMPLES = [item[3] for item in csvdata]
PERCENT_POS = [item[4] for item in csvdata]
PERCENT_ACT = [item[5] for item in csvdata]
data = {'DATE' : DATE,
        'SAMPLES': SAMPLES,
        'PERCENT_POS':PERCENT_POS,
        'PERCENT_ACT':PERCENT_ACT}
x = data['DATE']
samples = data['SAMPLES']
percent_pos = data['PERCENT_POS']
percent_act = data['PERCENT_ACT']

mytext1_ypos = float(samples[len(samples)-1])-40  # decrease number
mytext1 = Label(x=1, y=mytext1_ypos, text='Day 0 (first detected case): 07 March 2020')
ymax = float(samples[len(samples)-1])+5

plot1 = figure(x_range=x,y_range=(0,ymax),plot_width=700,plot_height=350,title="Samples processed and percentage of positive samples")
plot1.extra_y_ranges = {"foo": Range1d(start=0, end=15)}
plot1.line(x,samples,line_color="green", line_width = 3.5,alpha = 0.75, legend_label = "Processed samples")
plot1.yaxis.axis_label = "No. of Samples (in thousands)"
plot1.add_tools(HoverTool(tooltips=[("DATE", "@x"), ("Value", "@y")]))
plot1.line(x,percent_pos,y_range_name = "foo",line_color="red",line_width = 3.5,alpha = 0.75, legend_label = "% total positive cases")
plot1.line(x,percent_act,y_range_name = "foo",line_color="blue",line_width = 3.5,alpha = 0.75, legend_label = "% active positive cases")
plot1.add_layout(LinearAxis(y_range_name="foo",axis_label="%"), 'right')
plot1.title.text_font_size = "15pt"
plot1.xaxis.axis_label = "Day"
plot1.xaxis.axis_label_text_font = "times"
plot1.xaxis.axis_label_text_font_style = "normal"
plot1.xaxis.ticker = SingleIntervalTicker(interval=4)
plot1.xaxis.major_label_text_font_size = "10pt"
plot1.xaxis.major_label_orientation = np.pi/2
plot1.xaxis.axis_label_text_font_size = "15pt"
plot1.yaxis.axis_label_text_font = "times"
plot1.yaxis.axis_label_text_font_style = "normal"
plot1.yaxis.major_label_text_font_size = "10pt"
plot1.yaxis.axis_label_text_font_size = "15pt"
plot1.add_layout(mytext1)
legend_ypos = float(samples[len(samples)-1])-350  # Decrease number
plot1.legend.location = (1,legend_ypos)
plot1.ygrid.visible = False

save(plot1)
