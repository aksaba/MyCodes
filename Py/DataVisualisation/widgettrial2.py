from bokeh.plotting import output_file,save,figure,show
from bokeh.models import HoverTool,ColumnDataSource,FactorRange
from bokeh.layouts import column,row
from bokeh.models import DatetimeTickFormatter,ranges
from bokeh.models import Select
from bokeh.models.callbacks import CustomJS
import csv
import numpy as np
output_file('vbar_trial.html')


y1 = [5,10,15,20,25]
y2 = [25,20,15,10,5]
x = [1,2,3,4,5]
source = ColumnDataSource(data=dict(x=x, y=y1, y1=y1, y2=y2))

plot1 = figure(x_range=(0,max(x)),plot_width=500,plot_height=400,title="Number of positive cases (Cumulative) in the last 10 days")
plot1.vbar('x', top='y', source=source,width = 0.5)

plot1.title.text_font_size = "10pt"
plot1.xaxis.major_label_text_font_size = "10pt"
plot1.xaxis.major_label_orientation = np.pi/2
plot1.xaxis.axis_label_text_font_size = "15pt"

plot1.yaxis.axis_label = "No. of Cases"
plot1.yaxis.axis_label_text_font = "times"
plot1.yaxis.axis_label_text_font_style = "normal"
plot1.yaxis.major_label_text_font_size = "10pt"
plot1.yaxis.axis_label_text_font_size = "15pt"

callback = CustomJS(args=dict(source=source),code="""
        var data = source.data;
        var f = cb_obj.value
        if(f=="B") {
            source.data['y'] = source.data['y2'];
            }
        source.change.emit();

    """)

select = Select(title="Select District:", width =120, value="1", options=["A","B"])
select.js_on_change('value', callback)
save(row(select,plot1))
