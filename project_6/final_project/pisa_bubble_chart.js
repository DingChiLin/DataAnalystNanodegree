function Chart(){

  var myChart;

  this.init = function(data){

    var svg = dimple.newSvg("#chartContainer", '100%', '100%');
    var mathData = []
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

        if(s_index==0){ // set the selecor option only once
          $('#highlightCountrySelector .selectpicker').append($('<option>', {
            value: index,
            text: data[index]['Country']
          }))
        }
      }
    }

    $('.selectpicker').selectpicker('refresh');

    // Title
    svg.append("text")
       .attr("x", 60)
       .attr("y", 70)
       .attr("text-anchor", "left")
       .style("font-size", "25px")
       .style("font-weight", "bold")
       .text("Awesome charting from Dimple.js")

    // ICT Resource Legend
    svg.append("text")
       .attr("x", 600)
       .attr("y", 70)
       .attr("text-anchor", "left")
       .style("font-size", "15px")
       .style("font-weight", "bold")
       .text("ICT Resource (A highest ~ E lowest)")


    myChart = new dimple.chart(svg)
    myChart.setBounds(60, 130, 800, 500)

    var x = myChart.addMeasureAxis("x", "Score")
    x.overrideMin = 360
    x.overrideMax = 600
    x.title = 'Score (plausible value)'

    //上課時數
    var y = myChart.addMeasureAxis("y", "LearningTime")
    y.overrideMin = 100
    y.overrideMax = 400
    y.title = 'Learning Time ( min / week )'

    //控制大小
    var z = myChart.addMeasureAxis("z", "Size")
    z.overrideMin = 5
    z.overrideMax = 30

    //['國家', ‘科技使用程度’]
    var s = myChart.addSeries(["Country", "ICTResourcesClass"], dimple.plot.bubble)
    s.stacked = false
    s.addOrderRule(['ICTResourcesClass'], true)

    myChart.addLegend(560, 90, 300, 20, "right")

    /**
     * Update Data and Draw
     */

    updateData(splitData[0], true)
    updateHighlightCountry('chinese-taipei', 'rgb(197, 52, 48)')
  }

  this.changeSubject = function(index){
    updateData(splitData[index])
  }

  this.changeHighlightCountry = function(id, color){
    var country = $("#" + id + " option:selected").text()
    updateHighlightCountry(parseCountryName(country), color)
  }

  function parseCountryName(name){
    return name.toLowerCase().replace(/\(|\)|\ /g, "-")
  }

  function updateData(data, is_ict){
    myChart.data = data
    updateICTColor(is_ict)
    myChart.draw(1000)
  }

  function updateHighlightCountry(country, color){
    myChart.series[0].afterDraw = function (s, d) {
      if(s.style.stroke == color && s.id.indexOf(country) == -1){
        d3.select(s)
          .style('stroke', s.style.fill)
      }

      if(s.id.indexOf(country) > -1){
        d3.select(s)
          .style('stroke', color)
      }

      d3.select(s)
        .style('stroke-width', '3px')
    }

    myChart.draw(1000)
  }

  function updateICTColor(is_ict){
    if(is_ict){
      myChart.assignColor("A", "#808080", "#808080", 0.6);
      myChart.assignColor("B", "#808080", "#808080", 0.6);
      myChart.assignColor("C", "#808080", "#808080", 0.6);
      myChart.assignColor("D", "#808080", "#808080", 0.6);
      myChart.assignColor("E", "#808080", "#808080", 0.6);
    }else{
      myChart.assignColor("A", "#063870", "#063870", 1);
      myChart.assignColor("B", "#0D51B0", "#0D51B0", 1);
      myChart.assignColor("C", "#3188E8", "#3188E8", 1);
      myChart.assignColor("D", "#6CB0F8", "#6CB0F8", 1);
      myChart.assignColor("E", "#B3D9FD", "#B3D9FD", 1);
    }

    myChart.draw(1000)
  }

}

var chart = new Chart();

