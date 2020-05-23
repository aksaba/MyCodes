function makeDemo1(){
  d3.tsv("example1.tsv")
    .then(function(data){
      d3.select("svg")
        .selectAll("circle")
          .data(data)
          .enter()
          .append("circle")
          .attr("r",8)
          .attr("fill","red")
          .attr("cx",function(d){return d["x"]})
          .attr("cy",function(d){return d["y"]});
    });
}
