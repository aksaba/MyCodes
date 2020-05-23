########################################################################
## Multiple bar plots
## Selection box allows user to select an option among several
## Interactive tooltips
########################################################################


from bokeh.plotting import output_file,save,figure,show
from bokeh.models import HoverTool,ColumnDataSource,FactorRange,DatetimeTickFormatter,ranges,Select
from bokeh.models.callbacks import CustomJS
from bokeh.layouts import row
import csv
import numpy as np
output_file('vbar_districts.html')

with open("districts.csv") as csvfile:
    csvdata = list(csv.reader(csvfile))

DATE = [item[0] for item in csvdata]
i = 0
y = []
while i < 37 :
     y.append([item[i+1] for item in csvdata])
     i=i+1
data = {'DATE' : DATE}
x = data['DATE']
source = ColumnDataSource(data=dict(x=x, y=y[0],y0=y[0],y1=y[1],y2=y[2],y3=y[3],y4=y[4],y5=y[5],y6=y[6],y7=y[7],y8=y[8],y9=y[9],y10=y[10],y11=y[11],y12=y[12],y13=y[13],y14=y[14],y15=y[15],y16=y[16],y17=y[17],y18=y[18],y19=y[19],y20=y[20],y21=y[21],y22=y[22],y23=y[23],y24=y[24],y25=y[25],y26=y[26],y27=y[27],y28=y[28],y29=y[29],y30=y[30],y31=y[31],y32=y[32],y33=y[33],y34=y[34],y35=y[35],y36=y[36]))

plot1 = figure(x_range=x,plot_width=550,plot_height=350,title="Number of active cases in the last 21 days")
plot1.vbar('x', top='y', source=source,width = 0.8)
plot1.title.text_font_size = "12pt"
plot1.xaxis.major_label_text_font_size = "10pt"
plot1.xaxis.major_label_orientation = np.pi/2
plot1.xaxis.axis_label_text_font_size = "15pt"
plot1.yaxis.axis_label = "No. of Cases"
plot1.yaxis.axis_label_text_font = "times"
plot1.yaxis.axis_label_text_font_style = "normal"
plot1.yaxis.major_label_text_font_size = "10pt"
plot1.yaxis.axis_label_text_font_size = "15pt"
plot1.add_tools(HoverTool(tooltips=[("DATE", "@x"), ("No. of cases", "@y")]))

callback = CustomJS(args=dict(source=source),code="""
        var data = source.data;
        var f = cb_obj.value
        if(f=="Ariyalur") {source.data['y'] = source.data['y0'];}
        else if(f=="Ariyalur") {source.data['y'] = source.data['y0'];}
        else if(f=="Chengalpattu") {source.data['y'] = source.data['y1'];}
        else if(f=="Chennai") {source.data['y'] = source.data['y2'];}
        else if(f=="Coimbatore") {source.data['y'] = source.data['y3'];}
        else if(f=="Cuddalore") {source.data['y'] = source.data['y4'];}
        else if(f=="Dharmapuri") {source.data['y'] = source.data['y5'];}
        else if(f=="Dindigul") {source.data['y'] = source.data['y6'];}
        else if(f=="Erode") {source.data['y'] = source.data['y7'];}
        else if(f=="Kallakurichi") {source.data['y'] = source.data['y8'];}
        else if(f=="Kancheepuram") {source.data['y'] = source.data['y9'];}
        else if(f=="Kanyakumari") {source.data['y'] = source.data['y10'];}
        else if(f=="Karur") {source.data['y'] = source.data['y11'];}
        else if(f=="Krishnagiri") {source.data['y'] = source.data['y12'];}
        else if(f=="Madurai") {source.data['y'] = source.data['y13'];}
        else if(f=="Nagapattinam") {source.data['y'] = source.data['y14'];}
        else if(f=="Namakkal") {source.data['y'] = source.data['y15'];}
        else if(f=="Nilgiris") {source.data['y'] = source.data['y16'];}
        else if(f=="Perambalur") {source.data['y'] = source.data['y17'];}
        else if(f=="Pudukottai") {source.data['y'] = source.data['y18'];}
        else if(f=="Ramnad") {source.data['y'] = source.data['y19'];}
        else if(f=="Ranipet") {source.data['y'] = source.data['y20'];}
        else if(f=="Salem") {source.data['y'] = source.data['y21'];}
        else if(f=="Sivagangai") {source.data['y'] = source.data['y22'];}
        else if(f=="Tenkasi") {source.data['y'] = source.data['y23'];}
        else if(f=="Thanjavur") {source.data['y'] = source.data['y24'];}
        else if(f=="Theni") {source.data['y'] = source.data['y25'];}
        else if(f=="Thirupathur") {source.data['y'] = source.data['y26'];}
        else if(f=="Thiruvallur") {source.data['y'] = source.data['y27'];}
        else if(f=="Thiruvannamalai") {source.data['y'] = source.data['y28'];}
        else if(f=="Thiruvarur") {source.data['y'] = source.data['y29'];}
        else if(f=="Thoothukudi") {source.data['y'] = source.data['y30'];}
        else if(f=="Tirunelveli") {source.data['y'] = source.data['y31'];}
        else if(f=="Tiruppur") {source.data['y'] = source.data['y32'];}
        else if(f=="Trichy") {source.data['y'] = source.data['y33'];}
        else if(f=="Vellore") {source.data['y'] = source.data['y34'];}
        else if(f=="Villupuram") {source.data['y'] = source.data['y35'];}
        else if(f=="Virudhunagar") {source.data['y'] = source.data['y36'];}
        source.change.emit();

    """)

select = Select(title="Select District:", width =140, value="Ariyalur", options=["Ariyalur","Chengalpattu","Chennai","Coimbatore","Cuddalore","Dharmapuri","Dindigul","Erode","Kallakurichi","Kancheepuram","Kanyakumari","Karur","Krishnagiri","Madurai","Nagapattinam","Namakkal","Nilgiris","Perambalur","Pudukottai","Ramnad","Ranipet","Salem","Sivagangai","Tenkasi","Thanjavur","Theni","Thirupathur","Thiruvallur","Thiruvannamalai","Thiruvarur","Thoothukudi","Tirunelveli","Tiruppur","Trichy","Vellore","Villupuram","Virudhunagar"])
select.js_on_change('value', callback)
save(row(select,plot1))
