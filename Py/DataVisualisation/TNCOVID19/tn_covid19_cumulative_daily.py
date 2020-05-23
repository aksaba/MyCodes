########################################################################
## Two bar graphs arranged one below the other
## Interactive tooltips
########################################################################

from bokeh.plotting import output_file,save,figure,show
from bokeh.layouts import column
from bokeh.models import DatetimeTickFormatter,ranges,Dropdown, SingleIntervalTicker,Label,HoverTool,ColumnDataSource,FactorRange

import csv
import numpy as np
output_file('vbar_cumulative_daily.html')
with open("Book2.csv") as csvfile:  ## Read csv file
    csvdata = list(csv.reader(csvfile))

DATE = [item[0] for item in csvdata]
POS_COUNT = [item[1] for item in csvdata]
DAILY_POS_COUNT = [item[2] for item in csvdata]
data = {'DATE' : DATE,
        'POS_COUNT': POS_COUNT,
        'DAILY_POS_COUNT':DAILY_POS_COUNT}
x = data['DATE']
pos_counts = data['POS_COUNT']
daily_counts = data['DAILY_POS_COUNT']

source = ColumnDataSource(data=dict(x=x, pos_counts=pos_counts,daily_counts=daily_counts))

mytext1_ypos = int(pos_counts[len(pos_counts)-1])-600
mytext1 = Label(x=1, y=mytext1_ypos, text='Day 0 (first detected case): 07 March 2020')

plot1 = figure(x_range=FactorRange(*x),plot_width=700,plot_height=350,title="Number of positive cases (Cumulative)")
plot1.vbar('x', top='pos_counts', width=0.9, source=source)
plot1.title.text_font_size = "15pt"
plot1.xaxis.axis_label = "Day"
plot1.xaxis.axis_label_text_font = "times"
plot1.xaxis.axis_label_text_font_style = "normal"
plot1.xaxis.major_label_text_font_size = "10pt"
plot1.xaxis.major_label_orientation = np.pi/2
plot1.xaxis.axis_label_text_font_size = "15pt"
plot1.xaxis.ticker = SingleIntervalTicker(interval=2)
plot1.yaxis.axis_label = "No. of Cases"
plot1.yaxis.axis_label_text_font = "times"
plot1.yaxis.axis_label_text_font_style = "normal"
plot1.yaxis.major_label_text_font_size = "10pt"
plot1.yaxis.axis_label_text_font_size = "15pt"
plot1.add_tools(HoverTool(tooltips=[("DATE", "@x"), ("No. of cases", "@pos_counts")]))
plot1.add_layout(mytext1)

mytext2_ypos = int(daily_counts[len(daily_counts)-1])+20
mytext2 = Label(x=1, y=mytext2_ypos, text='Day 0 (first detected case): 07 March 2020')

plot2 = figure(x_range=x, plot_width=700,plot_height=350,title="Number of daily positive cases")
plot2.vbar(x='x', top='daily_counts', width=0.9, source=source)
plot2.title.text_font_size = "15pt"
plot2.xaxis.axis_label = "Day"
plot2.xaxis.axis_label_text_font = "times"
plot2.xaxis.axis_label_text_font_style = "normal"
plot2.xaxis.major_label_text_font_size = "10pt"
plot2.xaxis.major_label_orientation = np.pi/2
plot2.xaxis.axis_label_text_font_size = "15pt"
plot2.xaxis.ticker = SingleIntervalTicker(interval=2)
plot2.yaxis.axis_label = "No. of Cases"
plot2.yaxis.axis_label_text_font = "times"
plot2.yaxis.axis_label_text_font_style = "normal"
plot2.yaxis.major_label_text_font_size = "10pt"
plot2.yaxis.axis_label_text_font_size = "15pt"
plot2.add_tools(HoverTool(tooltips=[("DATE", "@x"), ("No. of cases", "@daily_counts")]))
plot2.add_layout(mytext2)

save(column(plot1,plot2))
