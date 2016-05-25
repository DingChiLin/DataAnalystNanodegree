function Chart(){

  var myChart;
  var subjectList = ['Math', 'Language', 'Science']
  var splitData = []
  var reservedColors = ['rgb(34, 238, 91)', 'rgb(237, 156, 41)', 'rgb(197, 52, 48)']

  this.init = function(data){

    var svg = dimple.newSvg("#chart-container", '100%', '100%');

    // Title
    svg.append("text")
       .attr("x", 60)
       .attr("y", 70)
       .attr("text-anchor", "left")
       .style("font-size", "25px")
       .style("font-weight", "bold")
       .text("Awesome charting from Dimple.js")

    // Parse Data
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
          $('#highlight-country-selector .selectpicker').append($('<option>', {
            value: data[index]['Country'],
            text: data[index]['Country']
          }))
        }
      }
    }

    // Default Select
    $('.selectpicker').selectpicker('refresh');
    $('#country-select-green').selectpicker('val', ['Chinese Taipei'])
    $('#country-select-yellow').selectpicker('val', ['China-Shanghai'])
    $('#country-select-red').selectpicker('val', ['Massachusetts (USA)'])

    // Set ICT Switch Button
    $(".ict-checkbox").bootstrapSwitch();
    $('.ict-checkbox').on('switchChange.bootstrapSwitch', function (event, state) {
      updateICTColor(state)
    })

    // ICT Resource Legend
    svg.append("text")
       .attr("x", 600)
       .attr("y", 70)
       .attr("text-anchor", "left")
       .attr("id", "ict-title")
       .style("font-size", "15px")
       .style("font-weight", "bold")
       .text("ICT Resource (A highest ~ E lowest)")

    // Main Chart
    myChart = new dimple.chart(svg)
    myChart.setBounds(60, 130, 800, 500)

    // Score
    var x = myChart.addMeasureAxis("x", "Score")
    x.overrideMin = 360
    x.overrideMax = 600
    x.title = 'Score (plausible value)'

    // Learning Time
    var y = myChart.addMeasureAxis("y", "LearningTime")
    y.overrideMin = 100
    y.overrideMax = 400
    y.title = 'Learning Time ( min / week )'

    // Size
    var z = myChart.addMeasureAxis("z", "Size")
    z.overrideMin = 5
    z.overrideMax = 27

    // Group
    var s = myChart.addSeries(["Country", "ICTResourcesClass"], dimple.plot.bubble)
    s.stacked = false
    s.addOrderRule(['ICTResourcesClass'], true)

    myChart.addLegend(560, 90, 300, 20, "right")

    // Update Data and Draw
    updateData(splitData[0])
    updateHighlightCountry('chinese-taipei', reservedColors[0])
    updateHighlightCountry('china-shanghai', reservedColors[1])
    updateHighlightCountry('massachusetts--usa-', reservedColors[2])
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

  function updateData(data){
    myChart.data = data

    myChart.assignColor("A", "#063870", "#063870", 0.9);
    myChart.assignColor("B", "#0D51B0", "#0D51B0", 0.9);
    myChart.assignColor("C", "#3188E8", "#3188E8", 0.9);
    myChart.assignColor("D", "#6CB0F8", "#6CB0F8", 0.9);
    myChart.assignColor("E", "#B3D9FD", "#B3D9FD", 0.9);

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
        .style('stroke-width', '2.5px')
    }

    myChart.draw()
  }

  function updateICTColor(is_ict){
    myChart.series[0].afterDraw = function (s, d) {
      if(is_ict){

        $('.dimple-legend').show()
        $('#ict-title').show()

        var level = d.key.split('/')[1][0]
        var color

        switch(level){
          case 'A':
            color = "#063870"
            break
          case 'B':
            color = "#0D51B0"
            break
          case 'C':
            color = "#3188E8"
            break
          case 'D':
            color = "#6CB0F8"
            break
          case 'E':
            color = "#B3D9FD"
            break
        }

        d3.select(s)
          .style('fill', color)
          .attr('opacity', 0.9)

        if(reservedColors.indexOf(d3.select(s).style('stroke')) == -1 ){
          d3.select(s)
           .style('stroke', color)
        }

      }else{
        $('.dimple-legend').hide()
        $('#ict-title').hide()

        d3.select(s)
          .style('fill', '#808080')
          .attr('opacity', 0.6)

        if(reservedColors.indexOf(d3.select(s).style('stroke')) == -1 ){
          d3.select(s)
            .style('stroke', '#808080')
        }
      }
    }

    myChart.draw(1)

  }

}

var chart = new Chart();

