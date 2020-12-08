from bokeh.plotting import output_file,save,figure
from bokeh.models import HoverTool
from bokeh.layouts import column
import pandas as pd
import numpy as np
output_file('vbar2.html')
col_list = ["Date", "Pos_count","Daily_pos_count"]
data = pd.read_csv("Book1.csv",usecols = col_list)



label = data["Date"]
y1 = data["Pos_count"]
y2 = data["Daily_pos_count"]

plot1 = figure(x_range=label,y_range=(0,max(y1)+20),plot_width=600,plot_height=400,title="Number of positive cases (Cumulative))")

plot1.vbar(label, top=y1, width=0.85, color="red")

plot1.title.text_font_size = "20pt"

plot1.xaxis.major_label_text_font_size = "10pt"
plot1.xaxis.major_label_orientation = np.pi/2
plot1.xaxis.axis_label_text_font_size = "15pt"

plot1.yaxis.axis_label = "No. of Cases"
plot1.yaxis.axis_label_text_font = "times"
plot1.yaxis.axis_label_text_font_style = "normal"
plot1.yaxis.major_label_text_font_size = "10pt"
plot1.yaxis.axis_label_text_font_size = "15pt"


plot1.add_tools(HoverTool(tooltips=[('No. of cases', '@data')]))


plot2 = figure(x_range=label,y_range=(0,max(y2)+20),tools = 'hover', plot_width=600,plot_height=400,title="Number of daily positive cases")

plot2.vbar(label, top=y2, width=0.85, color="blue")

plot2.title.text_font_size = "20pt"

plot2.xaxis.major_label_text_font_size = "10pt"
plot2.xaxis.major_label_orientation = np.pi/2
plot2.xaxis.axis_label_text_font_size = "15pt"

plot2.yaxis.axis_label = "No. of Cases"
plot2.yaxis.axis_label_text_font = "times"
plot2.yaxis.axis_label_text_font_style = "normal"
plot2.yaxis.major_label_text_font_size = "10pt"
plot2.yaxis.axis_label_text_font_size = "15pt"


save(column(plot1,plot2))
#save(plot2)
