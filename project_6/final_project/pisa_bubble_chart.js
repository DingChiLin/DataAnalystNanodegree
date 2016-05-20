function Chart(){

  var svg = dimple.newSvg("#chartContainer", 1000, 800);

  this.init = function(data){
    var mathData = [];
    var languageData = [];
    var scienceData = [];

    subjectList = ['Math', 'Language', 'Science']
    splitData = [];

    for(var s_index in subjectList){
      splitData[s_index] = []
      for(var index in data){
        splitData[s_index][index] = {}
        splitData[s_index][index]['Country'] = data[index]['Country']
        splitData[s_index][index]['ICTResourcesClass'] = data[index]['ICTResourcesClass']
        splitData[s_index][index]['LearningTime'] = data[index][ subjectList[s_index] + 'LearningTime']
        splitData[s_index][index]['Score'] = data[index][ subjectList[s_index] + 'Score']
        splitData[s_index][index]['Size'] = 10
      }
    }

    svg.append("text")
       .attr("x", 460)
       .attr("y", 64)
       .attr("text-anchor", "middle")
       .style("font-size", "20px")
       .style("font-weight", "bold")
       .text("Awesome charting from Dimple.js")

    var myChart = new dimple.chart(svg)
    myChart.setBounds(60, 100, 800, 500)

    var x = myChart.addMeasureAxis("x", "Score")
    x.overrideMin = 350
    x.overrideMax = 600
    console.log(x.totle)
    x.title = 'Score (plausible value)'

    //上課時數
    var y = myChart.addMeasureAxis("y", "LearningTime")
    y.overrideMin = 100
    y.overrideMax = 400
    y.title = 'Learning Time ( min / week )'

    //控制大小
    var z = myChart.addMeasureAxis("z", "Size")
    z.overrideMin = 5
    z.overrideMax = 40

    //['國家', ‘科技使用程度’]
    var s = myChart.addSeries(["Country", "ICTResourcesClass"], dimple.plot.bubble)
    s.stacked = false
    s.addOrderRule(['ICTResourcesClass'])

    myChart.addLegend(900, 100, 50, 100, "right")

    /**
     * Update Data and Draw
     */

    update(myChart, splitData[0])

    setTimeout(function(){
      //update(myChart, splitData[2])
    }, 4000);

  }

  function update(myChart, data, highlight_countries, is_ict){
    myChart.data = data

    // highlight choosed country (red, yellow, green)
    myChart.series[0].afterDraw = function (s, d) {
      //console.log(s)
      //console.log(d)

      d3.select('#dimple-chinese-taipei-b----')
      .style('stroke', 'red')
      .attr('stroke-width', '2px')
    }

    // add color for different ICT Resource Class
    myChart.assignColor("A", "#063870", "#063870", 1);
    myChart.assignColor("B", "#0D51B0", "#0D51B0", 1);
    myChart.assignColor("C", "#3188E8", "#3188E8", 1);
    myChart.assignColor("D", "#6CB0F8", "#6CB0F8", 1);
    myChart.assignColor("E", "#B3D9FD", "#B3D9FD", 1);

    myChart.draw(1000)
  }

  function changeStyle(){
          // 增大方塊size
    d3.selectAll("circle.dimple-series-0")
      .attr("r", 10)

    // 國家 Highlight 直接改
    //d3.select('#dimple-chinese-taipei-----')
    //  .style('fill', 'red')

    d3.select('#dimple-chinese-taipei-b----')
      .style('stroke', 'red')
      .attr('stroke-width', '2px')

    d3.selectAll('text.dimple-axis')
      .style("font-size", "15px")

    //$(".dimple-legend").hide()
  }
}
